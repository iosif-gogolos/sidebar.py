# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc
import tkinter as tk
from tkinter import font

#UiMainWindow class that contains the QStackedWidget
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(735, 407)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: #19559F;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color:white;\n"
"	height:30px;\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(245, 250, 254);\n"
"	color: #19559F;\n"
"	font-weight:bold\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(16, 16))
        self.label.setMaximumSize(QSize(16, 16))
        self.label.setSizeIncrement(QSize(16, 16))
        self.label.setBaseSize(QSize(16, 16))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u":/images/Colibri-LogoBL.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.home_1 = QPushButton(self.icon_only_widget)
        self.home_1.setObjectName(u"home_1")
        icon = QIcon()
        icon.addFile(u":/images/home_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/home.png", QSize(), QIcon.Normal, QIcon.On)
        self.home_1.setIcon(icon)
        self.home_1.setCheckable(True)

        self.verticalLayout.addWidget(self.home_1)

        self.offlineInstall_1 = QPushButton(self.icon_only_widget)
        self.offlineInstall_1.setObjectName(u"offlineInstall_1")
        icon1 = QIcon()
        icon1.addFile(u":/images/signal_wifi_off_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/signal_wifi_off.png", QSize(), QIcon.Normal, QIcon.On)
        self.offlineInstall_1.setIcon(icon1)
        self.offlineInstall_1.setCheckable(True)

        self.verticalLayout.addWidget(self.offlineInstall_1)

        self.logs_1 = QPushButton(self.icon_only_widget)
        self.logs_1.setObjectName(u"logs_1")
        icon2 = QIcon()
        icon2.addFile(u":/images/view_list_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/view_list.png", QSize(), QIcon.Normal, QIcon.On)
        self.logs_1.setIcon(icon2)
        self.logs_1.setCheckable(True)

        self.verticalLayout.addWidget(self.logs_1)

        self.hideShells_1 = QPushButton(self.icon_only_widget)
        self.hideShells_1.setObjectName(u"hideShells_1")
        icon3 = QIcon()
        icon3.addFile(u":/images/clear_all_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/clear_all.png", QSize(), QIcon.Normal, QIcon.On)
        self.hideShells_1.setIcon(icon3)
        self.hideShells_1.setCheckable(True)

        self.verticalLayout.addWidget(self.hideShells_1)

        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        icon4 = QIcon()
        icon4.addFile(u":/images/settings_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/settings.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_1.setIcon(icon4)
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settings_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.signout_1 = QPushButton(self.icon_only_widget)
        self.signout_1.setObjectName(u"signout_1")
        icon5 = QIcon()
        icon5.addFile(u":/images/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.signout_1.setIcon(icon5)
        self.signout_1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.signout_1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: #19559F;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color:white;\n"
"	text-align:left;\n"
"	height:30px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(245, 250, 254);\n"
"	color: #19559F;\n"
"	font-weight:bold\n"
"}\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(16, 16))
        self.label_2.setMaximumSize(QSize(16, 16))
        self.label_2.setSizeIncrement(QSize(16, 16))
        self.label_2.setBaseSize(QSize(16, 16))
        self.label_2.setPixmap(QPixmap(u":/images/Colibri-LogoBL.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.home_2 = QPushButton(self.icon_name_widget)
        self.home_2.setObjectName(u"home_2")
        self.home_2.setIcon(icon)
        self.home_2.setCheckable(True)
        self.home_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_2)

        self.offlineInstall_2 = QPushButton(self.icon_name_widget)
        self.offlineInstall_2.setObjectName(u"offlineInstall_2")
        self.offlineInstall_2.setIcon(icon1)
        self.offlineInstall_2.setCheckable(True)
        self.offlineInstall_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.offlineInstall_2)

        self.logs_2 = QPushButton(self.icon_name_widget)
        self.logs_2.setObjectName(u"logs_2")
        self.logs_2.setIcon(icon2)
        self.logs_2.setCheckable(True)
        self.logs_2.setAutoRepeat(False)
        self.logs_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.logs_2)

        self.hideShells_2 = QPushButton(self.icon_name_widget)
        self.hideShells_2.setObjectName(u"hideShells_2")
        self.hideShells_2.setIcon(icon3)
        self.hideShells_2.setCheckable(True)
        self.hideShells_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.hideShells_2)

        self.settings_2 = QPushButton(self.icon_name_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setIcon(icon4)
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settings_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 178, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.signout_2 = QPushButton(self.icon_name_widget)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setIcon(icon5)
        self.signout_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.signout_2)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.main_menu)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu = QPushButton(self.widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u":/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon6)
        self.menu.setIconSize(QSize(20, 20))
        self.menu.setCheckable(True)
        self.menu.setAutoExclusive(False)

        self.horizontalLayout_4.addWidget(self.menu)

        self.horizontalSpacer_2 = QSpacerItem(125, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.search = QPushButton(self.widget)
        self.search.setObjectName(u"search")
        icon7 = QIcon()
        icon7.addFile(u":/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon7)

        self.horizontalLayout.addWidget(self.search)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(125, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.profile = QPushButton(self.widget)
        self.profile.setObjectName(u"profile")
        self.profile.setStyleSheet(u"border:none;")
        icon8 = QIcon()
        icon8.addFile(u":/images/bug_report.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.profile)


        self.verticalLayout_5.addWidget(self.widget)

        self.Header_widget = QStackedWidget(self.main_menu)
        self.Header_widget.setObjectName(u"Header_widget")
        self.Header_widget.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self._1_dashboard_page = QWidget()
        self._1_dashboard_page.setObjectName(u"_1_dashboard_page")
        self.Header_widget.addWidget(self._1_dashboard_page)
        self._2_profile_page = QWidget()
        self._2_profile_page.setObjectName(u"_2_profile_page")
        self.label_10 = QLabel(self._2_profile_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 0, 231, 61))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_10.setFont(font1)
        self.Header_widget.addWidget(self._2_profile_page)
        self._4_notifications_page = QWidget()
        self._4_notifications_page.setObjectName(u"_4_notifications_page")
        self.label_6 = QLabel(self._4_notifications_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 0, 231, 61))
        self.label_6.setFont(font1)
        self.Header_widget.addWidget(self._4_notifications_page)
        self._5_settings_page = QWidget()
        self._5_settings_page.setObjectName(u"_5_settings_page")
        self.label_11 = QLabel(self._5_settings_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 20, 231, 61))
        self.label_11.setFont(font1)
        self.Header_widget.addWidget(self._5_settings_page)
        self._3_messages_page = QWidget()
        self._3_messages_page.setObjectName(u"_3_messages_page")
        self.label_5 = QLabel(self._3_messages_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 231, 61))
        self.label_5.setFont(font1)
        self.Header_widget.addWidget(self._3_messages_page)

        self.verticalLayout_5.addWidget(self.Header_widget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.settings_1.toggled.connect(self.settings_2.setChecked)
        self.hideShells_1.toggled.connect(self.hideShells_2.setChecked)
        self.logs_1.toggled.connect(self.logs_2.setChecked)
        self.offlineInstall_1.toggled.connect(self.offlineInstall_2.setChecked)
        self.home_1.toggled.connect(self.home_2.setChecked)
        self.home_2.toggled.connect(self.home_1.setChecked)
        self.offlineInstall_2.toggled.connect(self.offlineInstall_1.setChecked)
        self.logs_2.toggled.connect(self.logs_1.setChecked)
        self.hideShells_2.toggled.connect(self.hideShells_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.signout_1.toggled.connect(MainWindow.close)
        self.signout_2.toggled.connect(MainWindow.close)

        self.Header_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")

        # Add pages to the stacked widget
        self.page_home = QWidget()
        self.page_offlineInstall = QWidget()
        self.page_logs = QWidget()
        self.page_hideShells = QWidget()
        self.page_settings = QWidget()

        self.stackedWidget.addWidget(self.page_home)
        self.stackedWidget.addWidget(self.page_offlineInstall)
        self.stackedWidget.addWidget(self.page_logs)
        self.stackedWidget.addWidget(self.page_hideShells)
        self.stackedWidget.addWidget(self.page_settings)

        self.gridLayout.addWidget(self.stackedWidget, 0, 3, 1, 1)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.home_1.setText("")
        self.offlineInstall_1.setText("")
        self.logs_1.setText("")
        self.hideShells_1.setText("")
        self.settings_1.setText("")
        self.signout_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Updater V2", None))
        self.home_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.offlineInstall_2.setText(QCoreApplication.translate("MainWindow", u"Offline Install ", None))
        self.logs_2.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.hideShells_2.setText(QCoreApplication.translate("MainWindow", u"Hide shells", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.signout_2.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.menu.setText("")
        self.search.setText("")
        self.profile.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Offline Binaries", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Shells Page", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
    # retranslateUi

