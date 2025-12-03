from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_main import Ui_MainWindow   
from sensor_reader import RS485Reader
import cv2
import numpy as np
import time

RTSP_URL = "rtsp://admin:ACLAB2023@192.168.1.50:8554/Streaming/Channels/102"

class CameraThread(QThread):
    """Capture frames from RTSP (OpenCV) and emit QImage for GUI display."""
    frame_ready = Signal(QImage)

    def __init__(self, rtsp_url: str, parent=None):
        super().__init__(parent)
        self.rtsp_url = rtsp_url
        self._running = True
        self.cap = None

    def run(self):
        try:
            self.cap = cv2.VideoCapture(self.rtsp_url)
        except Exception:
            self.cap = None

        if not self.cap or not self.cap.isOpened():
            return

        while self._running:
            ret, frame = self.cap.read()
            if not ret or frame is None:
                # small wait then retry
                time.sleep(0.1)
                continue

            # convert BGR->RGB
            try:
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb.shape
                bytes_per_line = ch * w
                img = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
                # emit a copy to be safe
                self.frame_ready.emit(img.copy())
            except Exception:
                pass

            # throttle capture loop to avoid CPU spike
            time.sleep(0.02)

        try:
            if self.cap:
                self.cap.release()
        except Exception:
            pass

    def stop(self):
        self._running = False
        # ensure capture loop can exit quickly
        try:
            if self.cap:
                self.cap.release()
        except Exception:
            pass
        
    