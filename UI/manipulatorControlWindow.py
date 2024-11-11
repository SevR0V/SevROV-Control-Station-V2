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
        Form.resize(247, 729)
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

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(150, 0))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.manEnableControl = QCheckBox(Form)
        self.manEnableControl.setObjectName(u"manEnableControl")

        self.verticalLayout_7.addWidget(self.manEnableControl)

        self.groupBox_5 = QGroupBox(Form)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
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
        self.axis1ControlDial.setTracking(False)
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


        self.verticalLayout_5.addWidget(self.groupBox)

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
        self.axis2ControlDial.setTracking(False)
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


        self.verticalLayout_5.addWidget(self.groupBox_2)

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
        self.axis3ControlDial.setTracking(False)
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


        self.verticalLayout_5.addWidget(self.groupBox_3)


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
        self.label_5.setText(QCoreApplication.translate("Form", u"OFFLINE", None))
        self.manEnableControl.setText(QCoreApplication.translate("Form", u"Enable manual control", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"Manipulator Control", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Axis 1", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Axis 2", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Axis 3", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"Grip Control", None))
        self.gripOpenButton.setText(QCoreApplication.translate("Form", u"Open", None))
        self.gripCloseButton.setText(QCoreApplication.translate("Form", u"Close", None))
        self.parkButton.setText(QCoreApplication.translate("Form", u"Park", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Parking settings", None))
        self.label.setText(QCoreApplication.translate("Form", u"Axis 1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Axis 2", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Axis 3", None))
    # retranslateUi

