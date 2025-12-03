import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_main import Ui_MainWindow   
from sensor_reader import RS485Reader
from camera_thread import CameraThread
from camera_thread import RTSP_URL
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI Loading
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # =======================
        # PAGE SWITCH
        # =======================
        self.ui.homeBtn.clicked.connect(lambda: self.switchPage(0, self.ui.homeBtn))
        self.ui.sensorBtn.clicked.connect(lambda: self.switchPage(1, self.ui.sensorBtn))
        self.ui.notiBtn.clicked.connect(lambda: self.switchPage(2, self.ui.notiBtn))
        self.ui.vaBtn.clicked.connect(lambda: self.switchPage(2, self.ui.notiBtn))

        self.ui.menuBtn.clicked.connect(self.toggleMenu)
        self.ui.menuBtn_2.clicked.connect(self.toggleMenu)
        self.ui.menuBtn_3.clicked.connect(self.toggleMenu)

        # Default: Home active
        self.setActiveButton(self.ui.homeBtn)
        self.show()
        
        # Default: Set up warning thresholds
        self._thresholds = {
            "temperature": 50.0,   # °C
            "humidity": 70.0,      # % 
            "pm2_5": 35.0,         # µg/m3 
        }
        # track whether a sensor is currently in alarm state to avoid duplicates
        self.sensor_state = {
            "temperature": False,
            "humidity": False,
            "pm2_5": False,
        }

        # simple in-memory notification buffer (most recent first)
        self._notifications = []
        self._max_notifications = 5

        # Start RS485 reader thread and connect to UI updates
        try:
            # default port is "/dev/serial0" (Raspberry Pi); change if needed
            self.rs485 = RS485Reader(port="COM3", baudrate=9600)
            self.rs485.data_received.connect(self.on_sensor_data)
            self.rs485.start()
        except Exception:
            self.rs485 = None

        # Start Camera thread (RTSP) and connect to UI updates
        self.camera_thread = None
        try:
            if RTSP_URL:
                self.camera_thread = CameraThread(RTSP_URL)
                self.camera_thread.frame_ready.connect(self.update_camera_frame)
                self.camera_thread.start()
        except Exception:
            self.camera_thread = None

    def closeEvent(self, event):
        # Stop RS485 thread 
        if hasattr(self, "rs485") and self.rs485 is not None:
            try:
                self.rs485.stop()
                self.rs485.wait(1500)
            except Exception:
                pass
        # Stop camera thread
        if hasattr(self, "camera_thread") and self.camera_thread is not None:
            try:
                self.camera_thread.stop()
                self.camera_thread.wait(1500)
            except Exception:
                pass
        super().closeEvent(event)

    # =======================
    # CAMERA DISPLAY 
    # =======================
    
    @Slot(QImage)
    def update_camera_frame(self, img: QImage):
        """Receive QImage from CameraThread and display in UI."""
        try:
            # scale to label size while keeping aspect ratio
            lbl = self.ui.camera_stream
            if lbl is None:
                return
            pix = QPixmap.fromImage(img)
            w = lbl.width()
            h = lbl.height()
            if w > 0 and h > 0:
                pix = pix.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            lbl.setPixmap(pix)
        except Exception:
            pass

    # =======================
    # GET DATA VALUE & ADD NOTIFICATION
    # =======================
    
    def on_sensor_data(self, data: dict):
        """Update UI labels from sensor data dict.

        Expected keys: `temperature`, `humidity`, `pm2_5` (values numeric).
        """
        try:
            temp = data.get("temperature")
            if temp is not None:
                self.ui.label.setText(f"{temp} °C")

            hum = data.get("humidity")
            if hum is not None:
                self.ui.label_12.setText(f"{hum} %")

            pm = data.get("pm2_5")
            if pm is not None:
                self.ui.label_6.setText(f"{pm} µg/m³")
        except Exception:
            # ignore UI update errors
            pass

        # --- threshold checks and notifications ---
        try:
            # Temperature
            if temp is not None:
                exceeded = temp > self._thresholds["temperature"]
                if exceeded and not self.sensor_state["temperature"]:
                    self.sensor_state["temperature"] = True
                    # visual alert
                    try:
                        self.ui.label.setStyleSheet("color: red; font-weight: bold;")
                    except Exception:
                        pass
                    self.add_notification(f"Temperature high: {temp} °C", critical=True)
                elif not exceeded and self.sensor_state["temperature"]:
                    # recovered
                    self.sensor_state["temperature"] = False
                    try:
                        self.ui.label.setStyleSheet("")
                    except Exception:
                        pass
                    self.add_notification(f"Temperature back to normal: {temp} °C", critical=False)

            # Humidity 
            if hum is not None:
                exceeded = hum > self._thresholds["humidity"]
                if exceeded and not self.sensor_state["humidity"]:
                    self.sensor_state["humidity"] = True
                    try:
                        self.ui.label_12.setStyleSheet("color: red; font-weight: bold;")
                    except Exception:
                        pass
                    self.add_notification(f"Humidity high: {hum} %", critical=True)
                elif not exceeded and self.sensor_state["humidity"]:
                    self.sensor_state["humidity"] = False
                    try:
                        self.ui.label_12.setStyleSheet("")
                    except Exception:
                        pass
                    self.add_notification(f"Humidity back to normal: {hum} %", critical=False)

            # PM2.5
            if pm is not None:
                exceeded = pm > self._thresholds["pm2_5"]
                if exceeded and not self.sensor_state["pm2_5"]:
                    self.sensor_state["pm2_5"] = True
                    try:
                        self.ui.label_6.setStyleSheet("color: red; font-weight: bold;")
                    except Exception:
                        pass
                    self.add_notification(f"PM2.5 high: {pm}", critical=True)
                elif not exceeded and self.sensor_state["pm2_5"]:
                    self.sensor_state["pm2_5"] = False
                    try:
                        self.ui.label_6.setStyleSheet("")
                    except Exception:
                        pass
                    self.add_notification(f"PM2.5 back to normal: {pm} µg/m³", critical=False)
        except Exception:
            # ignore threshold check errors
            pass

    def add_notification(self, message: str, critical: bool = False):
        """Add a notification to the UI and keep a small buffer.

        If `critical` is True, play a system beep.
        """
        try:
            ts = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
            full = f"[{ts}] {message}"
            # insert to front
            self._notifications.insert(0, full)
            # trim
            if len(self._notifications) > self._max_notifications:
                self._notifications = self._notifications[: self._max_notifications]
            # update notification
            self.ui.label_10.setText("\n".join(self._notifications))
            if critical:
                try:
                    QApplication.beep()
                except Exception:
                    pass
        except Exception:
            pass

    # =======================
    # SET ACTIVE BUTTON
    # =======================
    def setActiveButton(self, btn):
        # Reset style các nút
        for b in [self.ui.homeBtn, self.ui.sensorBtn, self.ui.notiBtn]:
            b.setStyleSheet("")

        # Style active
        btn.setStyleSheet("""
            QPushButton {
                background-color:#fefeff;
                color: #9751c9;
                padding: 5px;
                text-align:left;
                border-top-left-radius:20px;
            }
        """)

    # =======================
    # SWITCH PAGE + ACTIVE
    # =======================
    def switchPage(self, index, btn):
        self.ui.stackedWidget.setCurrentIndex(index)
        self.setActiveButton(btn)

    def toggleMenu(self):
        width = self.ui.leftMenu.width()

        if width > 50:
            new_width = 0      # thu
        else:
            new_width = 180    # mở

        # Animate MIN width
        self.animMin = QPropertyAnimation(self.ui.leftMenu, b"minimumWidth")
        self.animMin.setDuration(250)
        self.animMin.setStartValue(width)
        self.animMin.setEndValue(new_width)
        self.animMin.setEasingCurve(QEasingCurve.InOutQuad)

        # Animate MAX width
        self.animMax = QPropertyAnimation(self.ui.leftMenu, b"maximumWidth")
        self.animMax.setDuration(250)
        self.animMax.setStartValue(width)
        self.animMax.setEndValue(new_width)
        self.animMax.setEasingCurve(QEasingCurve.InOutQuad)

        # Group animation chạy cùng lúc
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.animMin)
        self.group.addAnimation(self.animMax)
        self.group.start()

# =======================
# RUN APP
# =======================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
