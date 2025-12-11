import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_untitled import Ui_MainWindow   # file .ui đã convert

class TimeColumnDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        opt = QStyleOptionViewItem(option)
        self.initStyleOption(opt, index)

        painter.save()

        # Nếu là cột Time → đổi nền
        if index.column() == 3:
            painter.fillRect(opt.rect, QColor("#fef7ff"))   # MÀU TIME  (tím pastel)
        else:
            # nền default cho cột khác
            painter.fillRect(opt.rect, opt.backgroundBrush)

        painter.restore()

        # Vẽ text, focus, v.v.
        super().paint(painter, opt, index)

     
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Load Table
        self.setupTableView_1()   
        self.setupTableView_2()     
  

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
        self.ui.stackedWidget.setCurrentIndex(0)
        self.show()

    # =======================
    # SET ACTIVE BUTTON
    # =======================
    def setActiveButton(self, btn):
        # Reset style các nút
        for b in [self.ui.homeBtn, self.ui.sensorBtn, self.ui.notiBtn, self.ui.vaBtn]:
            b.setStyleSheet("")

        # Style active
        btn.setStyleSheet("""
            QPushButton {
                background-color:#fefeff;
                color: #9751c9;
                padding: 5px;
                text-align:left;
                border-top-left-radius:1s0px;
            }
        """)

    def setupTableView_1(self):
        # Tạo model 2 dòng, 4 cột
        self.model = QStandardItemModel(2, 4)
        self.model.setHorizontalHeaderLabels(["Temp", "Humid", "Pm2.5", "Time"])

        # Dòng 1
        self.model.setItem(0, 0, QStandardItem("60"))
        self.model.setItem(0, 1, QStandardItem("20"))
        self.model.setItem(0, 2, QStandardItem("1.5"))
        self.model.setItem(0, 3, QStandardItem("11:15 AM 02-12-2025"))

        # Dòng 2
        self.model.setItem(1, 0, QStandardItem("60"))
        self.model.setItem(1, 1, QStandardItem("20"))
        self.model.setItem(1, 2, QStandardItem("1.5"))
        self.model.setItem(1, 3, QStandardItem("11:05 AM 02-12-2025"))

        # Gán vào tableView
        self.ui.tableView.setModel(self.model)

        # Giãn cột cho đẹp
        header = self.ui.tableView.horizontalHeader()
        self.ui.tableView.verticalHeader().setVisible(False)

        # Temp, Humid, Pm2.5 = co giãn đều
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        # Time = rộng hơn
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        
        # Không cho sửa
        self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Kẻ line + style
        self.ui.tableView.setStyleSheet("""
            QTableView {
                background-color: #fefeff;        /* nền trắng nhẹ */
                border: 1px solid #ceade6;        /* viền tím nhạt */
                border-radius: 12px;
                gridline-color: #c7b4ea;
                selection-background-color: #ece3ff;
                selection-color: #000;
                padding: 10px;

            }

            QTableView::item {
                padding: 6px;
                border: none;
            }

            QTableView::item:hover {
                background-color: #f3ecff;
            }

            QHeaderView::section {
                background-color: #e9d9ff;
                color: #5b3ea0;
                padding: 10px;
                border: 1px solid #d4c2f5;
                font-weight: bold;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
            }

            QHeaderView::section:horizontal {
                border-left: 1px;
                border-right: 1px solid #d4c2f5;
            }

            QHeaderView::section:last {
                border-right: 0px;
            }

            QTableCornerButton::section {
                background-color: #e9d9ff;
                border: 1px solid #d4c2f5;
                border-top-left-radius: 8px;
            }
        """)
        self.ui.tableView.setItemDelegate(TimeColumnDelegate())

    def setupTableView_2(self):
        # Tạo model 2 dòng, 4 cột
        self.model = QStandardItemModel(2, 4)
        self.model.setHorizontalHeaderLabels(["Temp", "Humid", "Pm2.5", "Time"])

        # Dòng 1
        self.model.setItem(0, 0, QStandardItem("40"))
        self.model.setItem(0, 1, QStandardItem("90"))
        self.model.setItem(0, 2, QStandardItem("1.7"))
        self.model.setItem(0, 3, QStandardItem("11:15 AM 02-12-2025"))

        # Dòng 2
        self.model.setItem(1, 0, QStandardItem("30"))
        self.model.setItem(1, 1, QStandardItem("70"))
        self.model.setItem(1, 2, QStandardItem("1.5"))
        self.model.setItem(1, 3, QStandardItem("11:05 AM 02-12-2025"))

        # Gán vào tableView
        self.ui.tableView_2.setModel(self.model)

        # Giãn cột cho đẹp
        header = self.ui.tableView_2.horizontalHeader()
        self.ui.tableView_2.verticalHeader().setVisible(False)

        # Temp, Humid, Pm2.5 = co giãn đều
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        # Time = rộng hơn
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        
        # Không cho sửa
        self.ui.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Kẻ line + style
        self.ui.tableView_2.setStyleSheet("""
            QTableView {
                background-color: #fefeff;        /* nền trắng nhẹ */
                border: 1px solid #ceade6;        /* viền tím nhạt */
                border-radius: 12px;
                gridline-color: #c7b4ea;
                selection-background-color: #ece3ff;
                selection-color: #000;
                padding: 10px;

            }

            QTableView::item {
                padding: 6px;
                border: none;
            }

            QTableView::item:hover {
                background-color: #f3ecff;
            }

            QHeaderView::section {
                background-color: #e9d9ff;
                color: #5b3ea0;
                padding: 10px;
                border: 1px solid #d4c2f5;
                font-weight: bold;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
            }

            QHeaderView::section:horizontal {
                border-left: 1px;
                border-right: 1px solid #d4c2f5;
            }

            QHeaderView::section:last {
                border-right: 0px;
            }

            QTableCornerButton::section {
                background-color: #e9d9ff;
                border: 1px solid #d4c2f5;
                border-top-left-radius: 8px;
            }
        """)
        self.ui.tableView_2.setItemDelegate(TimeColumnDelegate())

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
