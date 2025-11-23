import serial
import time

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class RS485Reader(QThread):
    """Thread that polls RS485 sensor by sending Modbus-like requests
    and emits a dict of readings via `data_received` signal.
    """
    data_received = Signal(dict)

    def __init__(self, port="COM3", baudrate=9600, parent=None):
        super().__init__(parent)
        self.port = port
        self.baudrate = baudrate
        self._running = True
        self.ser = None

    def run(self):
        try:
            self.ser = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=1,
            )
        except Exception:
            return

        requests = {
            "temperature": bytes([0x15, 0x03, 0x01, 0xF5, 0x00, 0x01, 0x96, 0xD0]),
            "humidity": bytes([0x15, 0x03, 0x01, 0xF4, 0x00, 0x01, 0xC7, 0x10]),
            "pm2p5": bytes([0x15, 0x03, 0x01, 0xF7, 0x00, 0x01, 0x37, 0x10]),
        }

        while self._running:
            results = {}
            for name, cmd in requests.items():
                try:
                    # clear any leftover bytes
                    try:
                        self.ser.reset_input_buffer()
                    except Exception:
                        pass
                    self.ser.write(cmd)
                    self.ser.flush()
                    time.sleep(0.05)
                    resp = self.ser.read(7)
                    if len(resp) >= 5 and resp[1] == 0x03:
                        value = ((resp[3] << 8) | resp[4]) / 10.0
                        results[name] = value
                    else:
                        results[name] = None
                except Exception:
                    results[name] = None
                time.sleep(0.05)

            # normalize keys to match UI expectations
            out = {
                "temperature": results.get("temperature"),
                "humidity": results.get("humidity"),
                "pm2_5": results.get("pm2p5"),
            }
            try:
                self.data_received.emit(out)
            except Exception:
                pass

            # poll interval (1s) but break early if stopped
            for _ in range(10):
                if not self._running:
                    break
                time.sleep(0.1)

        try:
            self.ser.close()
        except Exception:
            pass

    def stop(self):
        self._running = False
