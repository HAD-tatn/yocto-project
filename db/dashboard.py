import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_untitled import Ui_MainWindow   # file .ui đã convert

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
        self.ui.vaBtn.clicked.connect(lambda: self.switchPage(2, self.ui.notiBtn))

        self.ui.menuBtn.clicked.connect(self.toggleMenu)
        self.ui.menuBtn_2.clicked.connect(self.toggleMenu)
        self.ui.menuBtn_3.clicked.connect(self.toggleMenu)

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
