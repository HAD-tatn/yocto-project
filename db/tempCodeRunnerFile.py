import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_main import Ui_MainWindow   

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # =======================
        # PAGE SWITCH
        # =======================
        self.ui.homeBtn.clicked.connect(lambda: self.switchPage(0, self.ui.homeBtn))
        self.ui.sensorBtn.clicked.connect(lambda: self.switchPage(1, self.ui.sensorBtn))
        self.ui.notiBtn.clicked.connect(lambda: self.switchPage(2, self.ui.notiBtn))

        # Mặc định nút Home active
        self.setActiveButton(self.ui.homeBtn)

        self.show()

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


# =======================
# RUN APP
# =======================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
