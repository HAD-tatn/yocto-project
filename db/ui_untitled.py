# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledDQaBVo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(988, 780)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"color:#000;\n"
"border:none;\n"
"}\n"
"\n"
"#leftMenu{\n"
"	background-color:#ceade6;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"#mainBody,#page_1,#page_2,#page_3{\n"
"background-color: #eff9fe;\n"
"border-radius: 30px;\n"
"}\n"
"\n"
"#ss1_list_frame1, #ss1_list_frame2{\n"
"background-color: #eff9fe;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#tableView,#tableView_2{\n"
"background-color: #eff9fe;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background: transparent;\n"
"}\n"
"#labelMenu,#labelTemp,#labelHumid,#labelPM,#labelMenu_2,#labelMenu_3,#labelCamera,#labelNoti,#labelControl{\n"
"color: #9751c9;\n"
"}\n"
"\n"
"#vaBtn{\n"
"color: #fefeff;\n"
"background-color:#ceade6;\n"
"border-radius: 10px;\n"
"padding:3px;\n"
"}\n"
"\n"
"#header_db, #header_ss, #db_frame1_card1,  #db_frame1_card2,  #db_frame1_card3,  #db_frame2_card1 ,  #db_frame2_card2, #db_frame2_card3{\n"
"background-color: #fefeff;\n"
"color: #9751c9;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 50px;\n"
"    height: 50px;\n"
"}\n"
""
                        "\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(\"E:/Study/BTL/DATN/Dashboard/1.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(\"E:/Study/BTL/DATN/Dashboard/2.png\");\n"
"}\n"
"\n"
"#homeBtn,#notiBtn,#sensorBtn{\n"
"	color: #fefeff;\n"
"	text-align:left;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    background: #f7e8ff;\n"
"    border: 2px solid #c29af8;\n"
"    border-radius: 8px;\n"
"    color: #333;\n"
"    font-weight: bold;\n"
"\n"
"    padding: -2px 0px 0px 2px;     /* c\u0103n icon + text */\n"
"}\n"
"#ss_frame1{\n"
"    background: #fefeff;\n"
"    border-radius: 20px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"#scrollContent ,#ss1_list, #ss2_list  {\n"
"    background: #fefeff;\n"
"  \n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_6 = QFrame(self.leftMenu)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(150, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(150, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton(self.frame_7)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(100, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.homeBtn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon-purple/icon-purple/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.homeBtn, 0, Qt.AlignTop)

        self.sensorBtn = QPushButton(self.frame_7)
        self.sensorBtn.setObjectName(u"sensorBtn")
        self.sensorBtn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icon-purple/icon-purple/slack.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sensorBtn.setIcon(icon1)
        self.sensorBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.sensorBtn)

        self.notiBtn = QPushButton(self.frame_7)
        self.notiBtn.setObjectName(u"notiBtn")
        self.notiBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icon-purple/icon-purple/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notiBtn.setIcon(icon2)
        self.notiBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.notiBtn)


        self.verticalLayout_11.addWidget(self.frame_7, 0, Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_6, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        font1 = QFont()
        font1.setPointSize(7)
        self.mainBody.setFont(font1)
        self.mainBody.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.mainBody)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.mainBody)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_12 = QVBoxLayout(self.page_1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.header_db = QWidget(self.page_1)
        self.header_db.setObjectName(u"header_db")
        self.horizontalLayout_2 = QHBoxLayout(self.header_db)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.header_db)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icon-purple/icon-purple/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon3)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuBtn)

        self.labelMenu = QLabel(self.widget)
        self.labelMenu.setObjectName(u"labelMenu")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.labelMenu.setFont(font2)

        self.horizontalLayout_3.addWidget(self.labelMenu)


        self.horizontalLayout_2.addWidget(self.widget, 0, Qt.AlignLeft)

        self.widget_2 = QWidget(self.header_db)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.horizontalLayout_2.addWidget(self.widget_2, 0, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.header_db)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.accountButton = QPushButton(self.widget_3)
        self.accountButton.setObjectName(u"accountButton")
        icon4 = QIcon()
        icon4.addFile(u":/icon-purple/icon-purple/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountButton.setIcon(icon4)
        self.accountButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.accountButton)


        self.horizontalLayout_2.addWidget(self.widget_3, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.header_db)

        self.db_frame1 = QWidget(self.page_1)
        self.db_frame1.setObjectName(u"db_frame1")
        self.db_frame1.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout_7 = QHBoxLayout(self.db_frame1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.db_frame1_card1 = QFrame(self.db_frame1)
        self.db_frame1_card1.setObjectName(u"db_frame1_card1")
        self.db_frame1_card1.setMinimumSize(QSize(200, 0))
        self.db_frame1_card1.setFrameShape(QFrame.StyledPanel)
        self.db_frame1_card1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.db_frame1_card1)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.db_frame1_card1)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)

        self.horizontalLayout_8.addWidget(self.label)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(40, 40))
        self.label_3.setPixmap(QPixmap(u":/icon-iot/icon-iot/thermometer.svg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.labelTemp = QLabel(self.db_frame1_card1)
        self.labelTemp.setObjectName(u"labelTemp")
        self.labelTemp.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setPointSize(7)
        font4.setBold(True)
        font4.setWeight(75)
        self.labelTemp.setFont(font4)

        self.verticalLayout_2.addWidget(self.labelTemp, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.db_frame1_card1)

        self.db_frame1_card2 = QFrame(self.db_frame1)
        self.db_frame1_card2.setObjectName(u"db_frame1_card2")
        self.db_frame1_card2.setMinimumSize(QSize(200, 0))
        self.db_frame1_card2.setFrameShape(QFrame.StyledPanel)
        self.db_frame1_card2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.db_frame1_card2)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.frame_4 = QFrame(self.db_frame1_card2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.horizontalLayout_11.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(40, 40))
        self.label_13.setPixmap(QPixmap(u":/icon-iot/icon-iot/humidity.svg"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_13)


        self.verticalLayout_3.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.labelPM = QLabel(self.db_frame1_card2)
        self.labelPM.setObjectName(u"labelPM")
        self.labelPM.setMaximumSize(QSize(16777215, 40))
        self.labelPM.setFont(font4)

        self.verticalLayout_3.addWidget(self.labelPM, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.db_frame1_card2)

        self.db_frame1_card3 = QFrame(self.db_frame1)
        self.db_frame1_card3.setObjectName(u"db_frame1_card3")
        self.db_frame1_card3.setMinimumSize(QSize(200, 0))
        self.db_frame1_card3.setFrameShape(QFrame.StyledPanel)
        self.db_frame1_card3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.db_frame1_card3)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.frame_2 = QFrame(self.db_frame1_card3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(40, 40))
        self.label_7.setPixmap(QPixmap(u":/icon-iot/icon-iot/dust.svg"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_7)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.labelHumid = QLabel(self.db_frame1_card3)
        self.labelHumid.setObjectName(u"labelHumid")
        self.labelHumid.setMaximumSize(QSize(16777215, 40))
        self.labelHumid.setFont(font4)

        self.verticalLayout_4.addWidget(self.labelHumid, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.db_frame1_card3)


        self.verticalLayout_12.addWidget(self.db_frame1)

        self.db_frame2 = QWidget(self.page_1)
        self.db_frame2.setObjectName(u"db_frame2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.db_frame2.sizePolicy().hasHeightForWidth())
        self.db_frame2.setSizePolicy(sizePolicy)
        self.horizontalLayout_10 = QHBoxLayout(self.db_frame2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.db_frame2_card1 = QFrame(self.db_frame2)
        self.db_frame2_card1.setObjectName(u"db_frame2_card1")
        self.db_frame2_card1.setMinimumSize(QSize(160, 0))
        self.db_frame2_card1.setFrameShape(QFrame.StyledPanel)
        self.db_frame2_card1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.db_frame2_card1)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 11)
        self.frame_13 = QFrame(self.db_frame2_card1)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_23 = QLabel(self.frame_13)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setPixmap(QPixmap(u":/icon-purple/icon-purple/camera.svg"))

        self.horizontalLayout_15.addWidget(self.label_23, 0, Qt.AlignLeft)

        self.labelCamera = QLabel(self.frame_13)
        self.labelCamera.setObjectName(u"labelCamera")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelCamera.sizePolicy().hasHeightForWidth())
        self.labelCamera.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.labelCamera.setFont(font5)

        self.horizontalLayout_15.addWidget(self.labelCamera)


        self.verticalLayout_8.addWidget(self.frame_13)

        self.frame_8 = QFrame(self.db_frame2_card1)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy2)
        self.frame_8.setMinimumSize(QSize(480, 0))
        self.frame_8.setMaximumSize(QSize(16777213, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_8)


        self.horizontalLayout_10.addWidget(self.db_frame2_card1)

        self.db_frame2_card2_all = QFrame(self.db_frame2)
        self.db_frame2_card2_all.setObjectName(u"db_frame2_card2_all")
        self.db_frame2_card2_all.setFrameShape(QFrame.StyledPanel)
        self.db_frame2_card2_all.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.db_frame2_card2_all)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.db_frame2_card2_all2 = QFrame(self.db_frame2_card2_all)
        self.db_frame2_card2_all2.setObjectName(u"db_frame2_card2_all2")
        self.db_frame2_card2_all2.setMinimumSize(QSize(300, 500))
        self.db_frame2_card2_all2.setFrameShape(QFrame.StyledPanel)
        self.db_frame2_card2_all2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.db_frame2_card2_all2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.db_frame2_card2 = QFrame(self.db_frame2_card2_all2)
        self.db_frame2_card2.setObjectName(u"db_frame2_card2")
        self.db_frame2_card2.setMinimumSize(QSize(0, 250))
        self.db_frame2_card2.setFrameShape(QFrame.StyledPanel)
        self.db_frame2_card2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.db_frame2_card2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, -1, -1, 11)
        self.frame_3 = QFrame(self.db_frame2_card2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/icon-purple/icon-purple/bell.svg"))

        self.horizontalLayout_12.addWidget(self.label_4)

        self.labelNoti = QLabel(self.frame_3)
        self.labelNoti.setObjectName(u"labelNoti")
        self.labelNoti.setMinimumSize(QSize(200, 0))
        self.labelNoti.setFont(font5)

        self.horizontalLayout_12.addWidget(self.labelNoti)

        self.vaBtn = QPushButton(self.frame_3)
        self.vaBtn.setObjectName(u"vaBtn")
        self.vaBtn.setEnabled(True)
        self.vaBtn.setMinimumSize(QSize(100, 15))
        font6 = QFont()
        font6.setFamily(u"Segoe UI Emoji")
        font6.setBold(True)
        font6.setWeight(75)
        self.vaBtn.setFont(font6)
        icon5 = QIcon()
        icon5.addFile(u":/icon-purple/icon-purple/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.vaBtn.setIcon(icon5)
        self.vaBtn.setIconSize(QSize(25, 20))

        self.horizontalLayout_12.addWidget(self.vaBtn, 0, Qt.AlignRight)


        self.verticalLayout_15.addWidget(self.frame_3)

        self.frame_9 = QFrame(self.db_frame2_card2)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        font7 = QFont()
        font7.setPointSize(9)
        font7.setBold(False)
        font7.setWeight(50)
        self.label_11.setFont(font7)

        self.gridLayout.addWidget(self.label_11, 1, 1, 1, 1)

        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font7)

        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font7)

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font7)

        self.gridLayout.addWidget(self.label_14, 2, 1, 1, 1)

        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font7)

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_9)

        self.verticalSpacer = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer)


        self.verticalLayout_6.addWidget(self.db_frame2_card2)

        self.db_frame2_card3 = QFrame(self.db_frame2_card2_all2)
        self.db_frame2_card3.setObjectName(u"db_frame2_card3")
        self.db_frame2_card3.setMinimumSize(QSize(0, 0))
        self.db_frame2_card3.setFrameShape(QFrame.StyledPanel)
        self.db_frame2_card3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.db_frame2_card3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 11)
        self.frame_11 = QFrame(self.db_frame2_card3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.frame_11)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setPixmap(QPixmap(u":/icon-purple/icon-purple/monitor.svg"))

        self.horizontalLayout_13.addWidget(self.label_15, 0, Qt.AlignLeft)

        self.labelControl = QLabel(self.frame_11)
        self.labelControl.setObjectName(u"labelControl")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelControl.sizePolicy().hasHeightForWidth())
        self.labelControl.setSizePolicy(sizePolicy3)
        self.labelControl.setMinimumSize(QSize(290, 0))
        self.labelControl.setFont(font5)

        self.horizontalLayout_13.addWidget(self.labelControl)


        self.verticalLayout_7.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.db_frame2_card3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_12)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_2 = QCheckBox(self.frame_12)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_2.addWidget(self.checkBox_2, 1, 2, 1, 1)

        self.label_19 = QLabel(self.frame_12)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setPixmap(QPixmap(u":/icon-purple/icon-purple/toggle-left.svg"))

        self.gridLayout_2.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_18 = QLabel(self.frame_12)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        font8 = QFont()
        font8.setPointSize(8)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_18.setFont(font8)

        self.gridLayout_2.addWidget(self.label_18, 0, 1, 1, 1)

        self.label_20 = QLabel(self.frame_12)
        self.label_20.setObjectName(u"label_20")
        font9 = QFont()
        font9.setBold(True)
        font9.setWeight(75)
        self.label_20.setFont(font9)

        self.gridLayout_2.addWidget(self.label_20, 1, 1, 1, 1)

        self.checkBox = QCheckBox(self.frame_12)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)
        self.checkBox.setMinimumSize(QSize(0, 0))
        font10 = QFont()
        font10.setPointSize(6)
        font10.setBold(False)
        font10.setWeight(50)
        self.checkBox.setFont(font10)
        self.checkBox.setStyleSheet(u"")
        self.checkBox.setIconSize(QSize(60, 60))

        self.gridLayout_2.addWidget(self.checkBox, 0, 2, 1, 1, Qt.AlignRight)

        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(40, 0))
        self.label_17.setPixmap(QPixmap(u":/icon-purple/icon-purple/toggle-left.svg"))

        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1, Qt.AlignLeft)

        self.checkBox_3 = QCheckBox(self.frame_12)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_2.addWidget(self.checkBox_3, 2, 2, 1, 1)

        self.label_21 = QLabel(self.frame_12)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font9)

        self.gridLayout_2.addWidget(self.label_21, 2, 1, 1, 1)

        self.label_22 = QLabel(self.frame_12)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setPixmap(QPixmap(u":/icon-purple/icon-purple/toggle-left.svg"))

        self.gridLayout_2.addWidget(self.label_22, 2, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_12)


        self.verticalLayout_6.addWidget(self.db_frame2_card3)


        self.horizontalLayout_14.addWidget(self.db_frame2_card2_all2)


        self.horizontalLayout_10.addWidget(self.db_frame2_card2_all)

        self.horizontalLayout_10.setStretch(0, 1)

        self.verticalLayout_12.addWidget(self.db_frame2)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_14 = QVBoxLayout(self.page_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.header_ss = QWidget(self.page_2)
        self.header_ss.setObjectName(u"header_ss")
        self.horizontalLayout_5 = QHBoxLayout(self.header_ss)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.header_ss)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.menuBtn_2 = QPushButton(self.widget_4)
        self.menuBtn_2.setObjectName(u"menuBtn_2")
        icon6 = QIcon()
        icon6.addFile(u":/icon blue/icon blue/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn_2.setIcon(icon6)
        self.menuBtn_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.menuBtn_2)

        self.labelMenu_2 = QLabel(self.widget_4)
        self.labelMenu_2.setObjectName(u"labelMenu_2")
        self.labelMenu_2.setFont(font2)

        self.horizontalLayout_16.addWidget(self.labelMenu_2)


        self.horizontalLayout_5.addWidget(self.widget_4, 0, Qt.AlignLeft)

        self.widget_5 = QWidget(self.header_ss)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")

        self.horizontalLayout_5.addWidget(self.widget_5, 0, Qt.AlignHCenter)

        self.widget_6 = QWidget(self.header_ss)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.accountButton_2 = QPushButton(self.widget_6)
        self.accountButton_2.setObjectName(u"accountButton_2")
        icon7 = QIcon()
        icon7.addFile(u":/icon blue/icon blue/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountButton_2.setIcon(icon7)
        self.accountButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_18.addWidget(self.accountButton_2)


        self.horizontalLayout_5.addWidget(self.widget_6, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.header_ss)

        self.ss_frame1 = QFrame(self.page_2)
        self.ss_frame1.setObjectName(u"ss_frame1")
        sizePolicy.setHeightForWidth(self.ss_frame1.sizePolicy().hasHeightForWidth())
        self.ss_frame1.setSizePolicy(sizePolicy)
        self.ss_frame1.setStyleSheet(u"")
        self.ss_frame1.setFrameShape(QFrame.StyledPanel)
        self.ss_frame1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.ss_frame1)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.scrollView = QScrollArea(self.ss_frame1)
        self.scrollView.setObjectName(u"scrollView")
        self.scrollView.setStyleSheet(u"")
        self.scrollView.setWidgetResizable(True)
        self.scrollContent = QWidget()
        self.scrollContent.setObjectName(u"scrollContent")
        self.scrollContent.setGeometry(QRect(0, 0, 727, 634))
        self.scrollContent.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.scrollContent)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.toolBox = QToolBox(self.scrollContent)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setEnabled(True)
        self.toolBox.setMinimumSize(QSize(0, 0))
        font11 = QFont()
        font11.setPointSize(11)
        font11.setBold(True)
        font11.setWeight(75)
        self.toolBox.setFont(font11)
        self.toolBox.setStyleSheet(u"")
        self.ss1_list = QWidget()
        self.ss1_list.setObjectName(u"ss1_list")
        self.ss1_list.setGeometry(QRect(0, 0, 705, 536))
        self.horizontalLayout_24 = QHBoxLayout(self.ss1_list)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.ss1_list_frame1 = QFrame(self.ss1_list)
        self.ss1_list_frame1.setObjectName(u"ss1_list_frame1")
        self.ss1_list_frame1.setFrameShape(QFrame.StyledPanel)
        self.ss1_list_frame1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.ss1_list_frame1)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.tableView = QTableView(self.ss1_list_frame1)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout_27.addWidget(self.tableView)


        self.horizontalLayout_24.addWidget(self.ss1_list_frame1)

        icon8 = QIcon()
        icon8.addFile(u":/icon-purple/icon-purple/chevron-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.ss1_list, icon8, u"Sensor 1")
        self.ss2_list = QWidget()
        self.ss2_list.setObjectName(u"ss2_list")
        self.ss2_list.setGeometry(QRect(0, 0, 705, 536))
        self.horizontalLayout_25 = QHBoxLayout(self.ss2_list)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.ss1_list_frame2 = QFrame(self.ss2_list)
        self.ss1_list_frame2.setObjectName(u"ss1_list_frame2")
        self.ss1_list_frame2.setFrameShape(QFrame.StyledPanel)
        self.ss1_list_frame2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.ss1_list_frame2)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.tableView_2 = QTableView(self.ss1_list_frame2)
        self.tableView_2.setObjectName(u"tableView_2")

        self.horizontalLayout_26.addWidget(self.tableView_2)


        self.horizontalLayout_25.addWidget(self.ss1_list_frame2)

        self.toolBox.addItem(self.ss2_list, icon8, u"Sensor 2")

        self.verticalLayout_5.addWidget(self.toolBox)

        self.scrollView.setWidget(self.scrollContent)

        self.horizontalLayout_23.addWidget(self.scrollView)


        self.verticalLayout_14.addWidget(self.ss_frame1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_16 = QVBoxLayout(self.page_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.headerFrame_3 = QWidget(self.page_3)
        self.headerFrame_3.setObjectName(u"headerFrame_3")
        self.horizontalLayout_19 = QHBoxLayout(self.headerFrame_3)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.headerFrame_3)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.menuBtn_3 = QPushButton(self.widget_7)
        self.menuBtn_3.setObjectName(u"menuBtn_3")
        self.menuBtn_3.setIcon(icon6)
        self.menuBtn_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.menuBtn_3)

        self.labelMenu_3 = QLabel(self.widget_7)
        self.labelMenu_3.setObjectName(u"labelMenu_3")
        self.labelMenu_3.setFont(font2)

        self.horizontalLayout_20.addWidget(self.labelMenu_3)


        self.horizontalLayout_19.addWidget(self.widget_7, 0, Qt.AlignLeft)

        self.widget_8 = QWidget(self.headerFrame_3)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")

        self.horizontalLayout_19.addWidget(self.widget_8, 0, Qt.AlignHCenter)

        self.widget_9 = QWidget(self.headerFrame_3)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.accountButton_3 = QPushButton(self.widget_9)
        self.accountButton_3.setObjectName(u"accountButton_3")
        self.accountButton_3.setIcon(icon7)
        self.accountButton_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_22.addWidget(self.accountButton_3)


        self.horizontalLayout_19.addWidget(self.widget_9, 0, Qt.AlignRight)


        self.verticalLayout_16.addWidget(self.headerFrame_3)

        self.card9 = QFrame(self.page_3)
        self.card9.setObjectName(u"card9")
        sizePolicy.setHeightForWidth(self.card9.sizePolicy().hasHeightForWidth())
        self.card9.setSizePolicy(sizePolicy)
        self.card9.setFrameShape(QFrame.StyledPanel)
        self.card9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.card9)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(8)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.sensorBtn.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.notiBtn.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.menuBtn.setText("")
        self.labelMenu.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.accountButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"60 \u00b0C", None))
        self.label_3.setText("")
        self.labelTemp.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"70 %", None))
        self.label_13.setText("")
        self.labelPM.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_7.setText("")
        self.labelHumid.setText(QCoreApplication.translate("MainWindow", u"PM2.5", None))
        self.label_23.setText("")
        self.labelCamera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.label_4.setText("")
        self.labelNoti.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.vaBtn.setText(QCoreApplication.translate("MainWindow", u"View All", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Humidity is low", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Temperature is high", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"No.1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"No.2", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"PM2.5 > 0.5", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"No.3", None))
        self.label_15.setText("")
        self.labelControl.setText(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.checkBox_2.setText("")
        self.label_19.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"BUTTON 1", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"BUTTON 2", None))
        self.checkBox.setText("")
        self.label_17.setText("")
        self.checkBox_3.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"BUTTON 3", None))
        self.label_22.setText("")
        self.menuBtn_2.setText("")
        self.labelMenu_2.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.accountButton_2.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.ss1_list), QCoreApplication.translate("MainWindow", u"Sensor 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.ss2_list), QCoreApplication.translate("MainWindow", u"Sensor 2", None))
        self.menuBtn_3.setText("")
        self.labelMenu_3.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.accountButton_3.setText("")
    # retranslateUi

