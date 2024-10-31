# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSplitter,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(375, 490)
        MainWindow.setMinimumSize(QSize(375, 490))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.connectButton = QPushButton(self.groupBox)
        self.connectButton.setObjectName(u"connectButton")

        self.horizontalLayout_2.addWidget(self.connectButton)

        self.onlineStatus = QLabel(self.groupBox)
        self.onlineStatus.setObjectName(u"onlineStatus")

        self.horizontalLayout_2.addWidget(self.onlineStatus)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.masterButton = QPushButton(self.groupBox)
        self.masterButton.setObjectName(u"masterButton")

        self.horizontalLayout.addWidget(self.masterButton)

        self.masterStatus = QLabel(self.groupBox)
        self.masterStatus.setObjectName(u"masterStatus")

        self.horizontalLayout.addWidget(self.masterStatus)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.powerTargetVal = QDoubleSpinBox(self.groupBox_3)
        self.powerTargetVal.setObjectName(u"powerTargetVal")
        self.powerTargetVal.setMaximum(1.000000000000000)
        self.powerTargetVal.setSingleStep(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.powerTargetVal)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.positionResetBut = QPushButton(self.groupBox_3)
        self.positionResetBut.setObjectName(u"positionResetBut")

        self.verticalLayout_3.addWidget(self.positionResetBut)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.splitter.addWidget(self.layoutWidget)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stabOn = QRadioButton(self.groupBox_2)
        self.stabOn.setObjectName(u"stabOn")

        self.verticalLayout_2.addWidget(self.stabOn)

        self.rollStabOn = QRadioButton(self.groupBox_2)
        self.rollStabOn.setObjectName(u"rollStabOn")

        self.verticalLayout_2.addWidget(self.rollStabOn)

        self.pitchStabOn = QRadioButton(self.groupBox_2)
        self.pitchStabOn.setObjectName(u"pitchStabOn")

        self.verticalLayout_2.addWidget(self.pitchStabOn)

        self.yawStabOn = QRadioButton(self.groupBox_2)
        self.yawStabOn.setObjectName(u"yawStabOn")

        self.verticalLayout_2.addWidget(self.yawStabOn)

        self.depthStabOn = QRadioButton(self.groupBox_2)
        self.depthStabOn.setObjectName(u"depthStabOn")

        self.verticalLayout_2.addWidget(self.depthStabOn)

        self.splitter.addWidget(self.groupBox_2)

        self.verticalLayout_10.addWidget(self.splitter)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(70, 0))
        self.label_9.setMaximumSize(QSize(70, 16777215))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(90, 0))
        self.label_2.setMaximumSize(QSize(90, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.rollVal = QLineEdit(self.groupBox_4)
        self.rollVal.setObjectName(u"rollVal")
        self.rollVal.setEnabled(True)
        self.rollVal.setMinimumSize(QSize(60, 0))
        self.rollVal.setMaximumSize(QSize(60, 16777215))
        self.rollVal.setReadOnly(True)
        self.rollVal.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.rollVal)

        self.rollSPVal = QLineEdit(self.groupBox_4)
        self.rollSPVal.setObjectName(u"rollSPVal")
        self.rollSPVal.setEnabled(True)
        self.rollSPVal.setMinimumSize(QSize(60, 0))
        self.rollSPVal.setMaximumSize(QSize(60, 16777215))
        self.rollSPVal.setReadOnly(True)
        self.rollSPVal.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.rollSPVal)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(90, 0))
        self.label_3.setMaximumSize(QSize(90, 16777215))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.pitchVal = QLineEdit(self.groupBox_4)
        self.pitchVal.setObjectName(u"pitchVal")
        self.pitchVal.setEnabled(True)
        self.pitchVal.setMinimumSize(QSize(60, 0))
        self.pitchVal.setMaximumSize(QSize(60, 16777215))
        self.pitchVal.setReadOnly(True)
        self.pitchVal.setClearButtonEnabled(False)

        self.horizontalLayout_7.addWidget(self.pitchVal)

        self.pitchSPVal = QLineEdit(self.groupBox_4)
        self.pitchSPVal.setObjectName(u"pitchSPVal")
        self.pitchSPVal.setEnabled(True)
        self.pitchSPVal.setMinimumSize(QSize(60, 0))
        self.pitchSPVal.setMaximumSize(QSize(60, 16777215))
        self.pitchSPVal.setReadOnly(True)
        self.pitchSPVal.setClearButtonEnabled(False)

        self.horizontalLayout_7.addWidget(self.pitchSPVal)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(90, 0))
        self.label_5.setMaximumSize(QSize(90, 16777215))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.yawVal = QLineEdit(self.groupBox_4)
        self.yawVal.setObjectName(u"yawVal")
        self.yawVal.setEnabled(True)
        self.yawVal.setMinimumSize(QSize(60, 0))
        self.yawVal.setMaximumSize(QSize(60, 16777215))
        self.yawVal.setReadOnly(True)
        self.yawVal.setClearButtonEnabled(False)

        self.horizontalLayout_8.addWidget(self.yawVal)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(90, 0))
        self.label_6.setMaximumSize(QSize(90, 16777215))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.depthVal = QLineEdit(self.groupBox_4)
        self.depthVal.setObjectName(u"depthVal")
        self.depthVal.setEnabled(True)
        self.depthVal.setMinimumSize(QSize(60, 0))
        self.depthVal.setMaximumSize(QSize(60, 16777215))
        self.depthVal.setReadOnly(True)
        self.depthVal.setClearButtonEnabled(False)

        self.horizontalLayout_9.addWidget(self.depthVal)

        self.horizontalSpacer_3 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(90, 0))
        self.label_4.setMaximumSize(QSize(90, 16777215))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_4)

        self.chargeVal = QLineEdit(self.groupBox_4)
        self.chargeVal.setObjectName(u"chargeVal")
        self.chargeVal.setEnabled(True)
        self.chargeVal.setMinimumSize(QSize(60, 0))
        self.chargeVal.setMaximumSize(QSize(60, 16777215))
        self.chargeVal.setReadOnly(True)
        self.chargeVal.setClearButtonEnabled(False)

        self.horizontalLayout_10.addWidget(self.chargeVal)

        self.horizontalSpacer_4 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(90, 0))
        self.label_7.setMaximumSize(QSize(90, 16777215))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_7)

        self.voltageVal = QLineEdit(self.groupBox_4)
        self.voltageVal.setObjectName(u"voltageVal")
        self.voltageVal.setEnabled(True)
        self.voltageVal.setMinimumSize(QSize(60, 0))
        self.voltageVal.setMaximumSize(QSize(60, 16777215))
        self.voltageVal.setReadOnly(True)
        self.voltageVal.setClearButtonEnabled(False)

        self.horizontalLayout_11.addWidget(self.voltageVal)

        self.horizontalSpacer_5 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(90, 0))
        self.label_8.setMaximumSize(QSize(90, 16777215))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_8)

        self.currentVal = QLineEdit(self.groupBox_4)
        self.currentVal.setObjectName(u"currentVal")
        self.currentVal.setEnabled(True)
        self.currentVal.setMinimumSize(QSize(60, 0))
        self.currentVal.setMaximumSize(QSize(60, 16777215))
        self.currentVal.setReadOnly(True)
        self.currentVal.setClearButtonEnabled(False)

        self.horizontalLayout_12.addWidget(self.currentVal)

        self.horizontalSpacer_6 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)


        self.horizontalLayout_6.addWidget(self.groupBox_4)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.controlsBut = QPushButton(self.centralwidget)
        self.controlsBut.setObjectName(u"controlsBut")

        self.verticalLayout_9.addWidget(self.controlsBut)

        self.settingsBut = QPushButton(self.centralwidget)
        self.settingsBut.setObjectName(u"settingsBut")

        self.verticalLayout_9.addWidget(self.settingsBut)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SevROV Control Station v2", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"ROV", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.onlineStatus.setText(QCoreApplication.translate("MainWindow", u"OFFLINE", None))
        self.masterButton.setText(QCoreApplication.translate("MainWindow", u"MASTER", None))
        self.masterStatus.setText(QCoreApplication.translate("MainWindow", u"SAFE", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Power Target:", None))
        self.positionResetBut.setText(QCoreApplication.translate("MainWindow", u"Reset Position", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Stabilization", None))
        self.stabOn.setText(QCoreApplication.translate("MainWindow", u"Enable Stabilization", None))
        self.rollStabOn.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.pitchStabOn.setText(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.yawStabOn.setText(QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.depthStabOn.setText(QCoreApplication.translate("MainWindow", u"Depth", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Telemetry", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Setpoints", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Roll:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pitch:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Heading:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Depth:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Battery Charge:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Battery Voltage:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Battery Current:", None))
        self.controlsBut.setText(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.settingsBut.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

