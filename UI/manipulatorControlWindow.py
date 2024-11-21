# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manipulator.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDial, QDoubleSpinBox,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(466, 759)
        self.verticalLayout_7 = QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(110, 0))
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)

        self.manStatusLabel = QLabel(Form)
        self.manStatusLabel.setObjectName(u"manStatusLabel")
        self.manStatusLabel.setMinimumSize(QSize(150, 0))
        self.manStatusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.manStatusLabel)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.manEnableControl = QCheckBox(Form)
        self.manEnableControl.setObjectName(u"manEnableControl")

        self.verticalLayout_7.addWidget(self.manEnableControl)

        self.groupBox_5 = QGroupBox(Form)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox = QGroupBox(self.groupBox_5)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(221, 131))
        self.groupBox.setMaximumSize(QSize(221, 131))
        self.axis1RealValDial = QDial(self.groupBox)
        self.axis1RealValDial.setObjectName(u"axis1RealValDial")
        self.axis1RealValDial.setEnabled(False)
        self.axis1RealValDial.setGeometry(QRect(0, 10, 121, 121))
        self.axis1RealValDial.setMinimumSize(QSize(121, 121))
        self.axis1RealValDial.setMaximumSize(QSize(121, 121))
        self.axis1RealValDial.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis1RealValDial.setMaximum(3600)
        self.axis1RealValDial.setValue(0)
        self.axis1RealValDial.setWrapping(True)
        self.axis1RealValDial.setNotchTarget(0.100000000000000)
        self.axis1RealValDial.setNotchesVisible(False)
        self.axis1ControlDial = QDial(self.groupBox)
        self.axis1ControlDial.setObjectName(u"axis1ControlDial")
        self.axis1ControlDial.setEnabled(True)
        self.axis1ControlDial.setGeometry(QRect(10, 20, 101, 101))
        self.axis1ControlDial.setMinimumSize(QSize(101, 101))
        self.axis1ControlDial.setMaximumSize(QSize(101, 101))
        self.axis1ControlDial.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#if QT_CONFIG(tooltip)
        self.axis1ControlDial.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.axis1ControlDial.setMaximum(3600)
        self.axis1ControlDial.setValue(0)
        self.axis1ControlDial.setTracking(True)
        self.axis1ControlDial.setWrapping(True)
        self.axis1ControlDial.setNotchTarget(1.000000000000000)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(120, 40, 90, 61))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.axis1ControlVal = QDoubleSpinBox(self.layoutWidget)
        self.axis1ControlVal.setObjectName(u"axis1ControlVal")
        self.axis1ControlVal.setMinimumSize(QSize(88, 0))
        self.axis1ControlVal.setMaximumSize(QSize(88, 16777215))
        self.axis1ControlVal.setWrapping(True)
        self.axis1ControlVal.setMaximum(360.000000000000000)
        self.axis1ControlVal.setSingleStep(0.100000000000000)

        self.verticalLayout.addWidget(self.axis1ControlVal)

        self.axis1RealVal = QLineEdit(self.layoutWidget)
        self.axis1RealVal.setObjectName(u"axis1RealVal")
        self.axis1RealVal.setMinimumSize(QSize(88, 0))
        self.axis1RealVal.setMaximumSize(QSize(88, 16777215))
        self.axis1RealVal.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis1RealVal.setReadOnly(True)

        self.verticalLayout.addWidget(self.axis1RealVal)


        self.horizontalLayout_8.addWidget(self.groupBox)

        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.groupBox_7)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.axis1PhaseACur = QLineEdit(self.groupBox_7)
        self.axis1PhaseACur.setObjectName(u"axis1PhaseACur")
        self.axis1PhaseACur.setMinimumSize(QSize(88, 0))
        self.axis1PhaseACur.setMaximumSize(QSize(88, 16777215))
        self.axis1PhaseACur.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis1PhaseACur.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.axis1PhaseACur)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.axis1PhaseBCur = QLineEdit(self.groupBox_7)
        self.axis1PhaseBCur.setObjectName(u"axis1PhaseBCur")
        self.axis1PhaseBCur.setMinimumSize(QSize(88, 0))
        self.axis1PhaseBCur.setMaximumSize(QSize(88, 16777215))
        self.axis1PhaseBCur.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis1PhaseBCur.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.axis1PhaseBCur)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.groupBox_7)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.axis1Voltage = QLineEdit(self.groupBox_7)
        self.axis1Voltage.setObjectName(u"axis1Voltage")
        self.axis1Voltage.setMinimumSize(QSize(88, 0))
        self.axis1Voltage.setMaximumSize(QSize(88, 16777215))
        self.axis1Voltage.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis1Voltage.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.axis1Voltage)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_8.addWidget(self.groupBox_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.groupBox_2 = QGroupBox(self.groupBox_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(221, 131))
        self.groupBox_2.setMaximumSize(QSize(221, 131))
        self.axis2RealValDial = QDial(self.groupBox_2)
        self.axis2RealValDial.setObjectName(u"axis2RealValDial")
        self.axis2RealValDial.setEnabled(False)
        self.axis2RealValDial.setGeometry(QRect(0, 10, 121, 121))
        self.axis2RealValDial.setMinimumSize(QSize(121, 121))
        self.axis2RealValDial.setMaximumSize(QSize(121, 121))
        self.axis2RealValDial.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis2RealValDial.setMaximum(3600)
        self.axis2RealValDial.setValue(0)
        self.axis2RealValDial.setWrapping(True)
        self.axis2RealValDial.setNotchTarget(0.100000000000000)
        self.axis2RealValDial.setNotchesVisible(False)
        self.axis2ControlDial = QDial(self.groupBox_2)
        self.axis2ControlDial.setObjectName(u"axis2ControlDial")
        self.axis2ControlDial.setEnabled(True)
        self.axis2ControlDial.setGeometry(QRect(10, 20, 101, 101))
        self.axis2ControlDial.setMinimumSize(QSize(101, 101))
        self.axis2ControlDial.setMaximumSize(QSize(101, 101))
        self.axis2ControlDial.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#if QT_CONFIG(tooltip)
        self.axis2ControlDial.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.axis2ControlDial.setMaximum(3600)
        self.axis2ControlDial.setValue(0)
        self.axis2ControlDial.setTracking(True)
        self.axis2ControlDial.setWrapping(True)
        self.axis2ControlDial.setNotchTarget(1.000000000000000)
        self.layoutWidget_2 = QWidget(self.groupBox_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(120, 40, 90, 61))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.axis2ControlVal = QDoubleSpinBox(self.layoutWidget_2)
        self.axis2ControlVal.setObjectName(u"axis2ControlVal")
        self.axis2ControlVal.setMinimumSize(QSize(88, 0))
        self.axis2ControlVal.setMaximumSize(QSize(88, 16777215))
        self.axis2ControlVal.setWrapping(True)
        self.axis2ControlVal.setMaximum(360.000000000000000)
        self.axis2ControlVal.setSingleStep(0.100000000000000)

        self.verticalLayout_2.addWidget(self.axis2ControlVal)

        self.axis2RealVal = QLineEdit(self.layoutWidget_2)
        self.axis2RealVal.setObjectName(u"axis2RealVal")
        self.axis2RealVal.setMinimumSize(QSize(88, 0))
        self.axis2RealVal.setMaximumSize(QSize(88, 16777215))
        self.axis2RealVal.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis2RealVal.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.axis2RealVal)


        self.horizontalLayout_16.addWidget(self.groupBox_2)

        self.groupBox_8 = QGroupBox(self.groupBox_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.groupBox_8)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.axis2PhaseACur = QLineEdit(self.groupBox_8)
        self.axis2PhaseACur.setObjectName(u"axis2PhaseACur")
        self.axis2PhaseACur.setMinimumSize(QSize(88, 0))
        self.axis2PhaseACur.setMaximumSize(QSize(88, 16777215))
        self.axis2PhaseACur.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis2PhaseACur.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.axis2PhaseACur)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.groupBox_8)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.axis2PhaseBCur = QLineEdit(self.groupBox_8)
        self.axis2PhaseBCur.setObjectName(u"axis2PhaseBCur")
        self.axis2PhaseBCur.setMinimumSize(QSize(88, 0))
        self.axis2PhaseBCur.setMaximumSize(QSize(88, 16777215))
        self.axis2PhaseBCur.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis2PhaseBCur.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.axis2PhaseBCur)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.groupBox_8)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.axis2Voltage = QLineEdit(self.groupBox_8)
        self.axis2Voltage.setObjectName(u"axis2Voltage")
        self.axis2Voltage.setMinimumSize(QSize(88, 0))
        self.axis2Voltage.setMaximumSize(QSize(88, 16777215))
        self.axis2Voltage.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis2Voltage.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.axis2Voltage)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_16.addWidget(self.groupBox_8)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.groupBox_3 = QGroupBox(self.groupBox_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(221, 131))
        self.groupBox_3.setMaximumSize(QSize(221, 131))
        self.axis3RealValDial = QDial(self.groupBox_3)
        self.axis3RealValDial.setObjectName(u"axis3RealValDial")
        self.axis3RealValDial.setEnabled(False)
        self.axis3RealValDial.setGeometry(QRect(0, 10, 121, 121))
        self.axis3RealValDial.setMinimumSize(QSize(121, 121))
        self.axis3RealValDial.setMaximumSize(QSize(121, 121))
        self.axis3RealValDial.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis3RealValDial.setMaximum(3600)
        self.axis3RealValDial.setValue(0)
        self.axis3RealValDial.setWrapping(True)
        self.axis3RealValDial.setNotchTarget(0.100000000000000)
        self.axis3RealValDial.setNotchesVisible(False)
        self.axis3ControlDial = QDial(self.groupBox_3)
        self.axis3ControlDial.setObjectName(u"axis3ControlDial")
        self.axis3ControlDial.setEnabled(True)
        self.axis3ControlDial.setGeometry(QRect(10, 20, 101, 101))
        self.axis3ControlDial.setMinimumSize(QSize(101, 101))
        self.axis3ControlDial.setMaximumSize(QSize(101, 101))
        self.axis3ControlDial.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#if QT_CONFIG(tooltip)
        self.axis3ControlDial.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.axis3ControlDial.setMaximum(3600)
        self.axis3ControlDial.setValue(0)
        self.axis3ControlDial.setTracking(True)
        self.axis3ControlDial.setWrapping(True)
        self.axis3ControlDial.setNotchTarget(1.000000000000000)
        self.layoutWidget_3 = QWidget(self.groupBox_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(120, 40, 90, 54))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.axis3ControlVal = QDoubleSpinBox(self.layoutWidget_3)
        self.axis3ControlVal.setObjectName(u"axis3ControlVal")
        self.axis3ControlVal.setMinimumSize(QSize(88, 0))
        self.axis3ControlVal.setMaximumSize(QSize(88, 16777215))
        self.axis3ControlVal.setWrapping(True)
        self.axis3ControlVal.setMaximum(360.000000000000000)
        self.axis3ControlVal.setSingleStep(0.100000000000000)

        self.verticalLayout_3.addWidget(self.axis3ControlVal)

        self.axis3RealVal = QLineEdit(self.layoutWidget_3)
        self.axis3RealVal.setObjectName(u"axis3RealVal")
        self.axis3RealVal.setMinimumSize(QSize(88, 0))
        self.axis3RealVal.setMaximumSize(QSize(88, 16777215))
        self.axis3RealVal.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis3RealVal.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.axis3RealVal)


        self.horizontalLayout_15.addWidget(self.groupBox_3)

        self.groupBox_9 = QGroupBox(self.groupBox_5)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.groupBox_9)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.axis3PhaseACur = QLineEdit(self.groupBox_9)
        self.axis3PhaseACur.setObjectName(u"axis3PhaseACur")
        self.axis3PhaseACur.setMinimumSize(QSize(88, 0))
        self.axis3PhaseACur.setMaximumSize(QSize(88, 16777215))
        self.axis3PhaseACur.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis3PhaseACur.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.axis3PhaseACur)


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.groupBox_9)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.axis3PhaseBCur = QLineEdit(self.groupBox_9)
        self.axis3PhaseBCur.setObjectName(u"axis3PhaseBCur")
        self.axis3PhaseBCur.setMinimumSize(QSize(88, 0))
        self.axis3PhaseBCur.setMaximumSize(QSize(88, 16777215))
        self.axis3PhaseBCur.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis3PhaseBCur.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.axis3PhaseBCur)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(self.groupBox_9)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_14.addWidget(self.label_13)

        self.axis3Voltage = QLineEdit(self.groupBox_9)
        self.axis3Voltage.setObjectName(u"axis3Voltage")
        self.axis3Voltage.setMinimumSize(QSize(88, 0))
        self.axis3Voltage.setMaximumSize(QSize(88, 16777215))
        self.axis3Voltage.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.axis3Voltage.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.axis3Voltage)


        self.verticalLayout_9.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_15.addWidget(self.groupBox_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)


        self.verticalLayout_7.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(Form)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gripOpenButton = QPushButton(self.groupBox_6)
        self.gripOpenButton.setObjectName(u"gripOpenButton")

        self.horizontalLayout.addWidget(self.gripOpenButton)

        self.gripCloseButton = QPushButton(self.groupBox_6)
        self.gripCloseButton.setObjectName(u"gripCloseButton")

        self.horizontalLayout.addWidget(self.gripCloseButton)


        self.verticalLayout_7.addWidget(self.groupBox_6)

        self.parkButton = QPushButton(Form)
        self.parkButton.setObjectName(u"parkButton")

        self.verticalLayout_7.addWidget(self.parkButton)

        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(151, 0))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.axis1ParkingVal = QDoubleSpinBox(self.groupBox_4)
        self.axis1ParkingVal.setObjectName(u"axis1ParkingVal")
        self.axis1ParkingVal.setWrapping(True)
        self.axis1ParkingVal.setMaximum(360.000000000000000)
        self.axis1ParkingVal.setSingleStep(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.axis1ParkingVal)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.axis2ParkingVal = QDoubleSpinBox(self.groupBox_4)
        self.axis2ParkingVal.setObjectName(u"axis2ParkingVal")
        self.axis2ParkingVal.setWrapping(True)
        self.axis2ParkingVal.setMaximum(360.000000000000000)
        self.axis2ParkingVal.setSingleStep(0.100000000000000)

        self.horizontalLayout_4.addWidget(self.axis2ParkingVal)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.axis3ParkingVal = QDoubleSpinBox(self.groupBox_4)
        self.axis3ParkingVal.setObjectName(u"axis3ParkingVal")
        self.axis3ParkingVal.setWrapping(True)
        self.axis3ParkingVal.setMaximum(360.000000000000000)
        self.axis3ParkingVal.setSingleStep(0.100000000000000)

        self.horizontalLayout_5.addWidget(self.axis3ParkingVal)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_7.addWidget(self.groupBox_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Manipulator", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Manipulator status:", None))
        self.manStatusLabel.setText(QCoreApplication.translate("Form", u"OFFLINE", None))
        self.manEnableControl.setText(QCoreApplication.translate("Form", u"Enable manual control", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"Manipulator Control and Telemetry", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Axis 1 angle control", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"Axis 1 Telemetry", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Phase A current", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Phase B current", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Voltage", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Axis 2 angle control", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Form", u"Axis 2 Telemetry", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Phase A current", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Phase B current", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Voltage", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Axis 3 angle control", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Form", u"Axis 3 Telemetry", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Phase A current", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Phase B current", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Voltage", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"Grip Control", None))
        self.gripOpenButton.setText(QCoreApplication.translate("Form", u"Open", None))
        self.gripCloseButton.setText(QCoreApplication.translate("Form", u"Close", None))
        self.parkButton.setText(QCoreApplication.translate("Form", u"Park", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Parking settings", None))
        self.label.setText(QCoreApplication.translate("Form", u"Axis 1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Axis 2", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Axis 3", None))
    # retranslateUi

