# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controls.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_controlsDialog(object):
    def setupUi(self, controlsDialog):
        if not controlsDialog.objectName():
            controlsDialog.setObjectName(u"controlsDialog")
        controlsDialog.resize(496, 1087)
        controlsDialog.setMinimumSize(QSize(496, 852))
        controlsDialog.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.verticalLayout_2 = QVBoxLayout(controlsDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.layput = QVBoxLayout()
        self.layput.setObjectName(u"layput")
        self.inputProgressBar = QProgressBar(controlsDialog)
        self.inputProgressBar.setObjectName(u"inputProgressBar")
        self.inputProgressBar.setMaximumSize(QSize(16777215, 10))
        self.inputProgressBar.setMaximum(5000)
        self.inputProgressBar.setValue(0)
        self.inputProgressBar.setTextVisible(False)

        self.layput.addWidget(self.inputProgressBar)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label = QLabel(controlsDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label)

        self.primaryDeviceList = QComboBox(controlsDialog)
        self.primaryDeviceList.setObjectName(u"primaryDeviceList")
        self.primaryDeviceList.setMinimumSize(QSize(370, 0))

        self.horizontalLayout_23.addWidget(self.primaryDeviceList)


        self.layput.addLayout(self.horizontalLayout_23)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(controlsDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.secondaryDeviceList = QComboBox(controlsDialog)
        self.secondaryDeviceList.setObjectName(u"secondaryDeviceList")
        self.secondaryDeviceList.setMinimumSize(QSize(370, 0))

        self.horizontalLayout.addWidget(self.secondaryDeviceList)


        self.layput.addLayout(self.horizontalLayout)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_3 = QLabel(controlsDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(140, 0))
        self.label_3.setMaximumSize(QSize(140, 16777215))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_3)

        self.label_4 = QLabel(controlsDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(133, 0))
        self.label_4.setMaximumSize(QSize(133, 16777215))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_4)

        self.label_5 = QLabel(controlsDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(20, 16))
        self.label_5.setMaximumSize(QSize(16, 16))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_5)

        self.label_7 = QLabel(controlsDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(133, 0))
        self.label_7.setMaximumSize(QSize(133, 16))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_7)

        self.label_6 = QLabel(controlsDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_6)


        self.layput.addLayout(self.horizontalLayout_22)

        self.label_31 = QLabel(controlsDialog)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layput.addWidget(self.label_31)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(controlsDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(140, 0))
        self.label_8.setMaximumSize(QSize(140, 16777215))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.primaryForward = QLineEdit(controlsDialog)
        self.primaryForward.setObjectName(u"primaryForward")
        self.primaryForward.setMinimumSize(QSize(0, 0))
        self.primaryForward.setMaximumSize(QSize(16777215, 16777215))
        self.primaryForward.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryForward.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryForward.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.primaryForward)

        self.primaryForwardInv = QCheckBox(controlsDialog)
        self.primaryForwardInv.setObjectName(u"primaryForwardInv")
        self.primaryForwardInv.setMinimumSize(QSize(16, 0))
        self.primaryForwardInv.setMaximumSize(QSize(16, 20))
        self.primaryForwardInv.setChecked(False)

        self.horizontalLayout_2.addWidget(self.primaryForwardInv)

        self.secondaryForward = QLineEdit(controlsDialog)
        self.secondaryForward.setObjectName(u"secondaryForward")
        self.secondaryForward.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryForward.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryForward.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.secondaryForward)

        self.secondaryForwardInv = QCheckBox(controlsDialog)
        self.secondaryForwardInv.setObjectName(u"secondaryForwardInv")
        self.secondaryForwardInv.setMinimumSize(QSize(20, 0))
        self.secondaryForwardInv.setMaximumSize(QSize(20, 20))
        self.secondaryForwardInv.setChecked(False)

        self.horizontalLayout_2.addWidget(self.secondaryForwardInv)


        self.layput.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(controlsDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(140, 0))
        self.label_9.setMaximumSize(QSize(140, 16777215))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.primaryStrafe = QLineEdit(controlsDialog)
        self.primaryStrafe.setObjectName(u"primaryStrafe")
        self.primaryStrafe.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryStrafe.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryStrafe.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.primaryStrafe)

        self.primaryStrafeInv = QCheckBox(controlsDialog)
        self.primaryStrafeInv.setObjectName(u"primaryStrafeInv")
        self.primaryStrafeInv.setMinimumSize(QSize(16, 0))
        self.primaryStrafeInv.setMaximumSize(QSize(16, 20))
        self.primaryStrafeInv.setChecked(False)

        self.horizontalLayout_3.addWidget(self.primaryStrafeInv)

        self.secondaryStrafe = QLineEdit(controlsDialog)
        self.secondaryStrafe.setObjectName(u"secondaryStrafe")
        self.secondaryStrafe.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryStrafe.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryStrafe.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.secondaryStrafe)

        self.secondaryStrafeInv = QCheckBox(controlsDialog)
        self.secondaryStrafeInv.setObjectName(u"secondaryStrafeInv")
        self.secondaryStrafeInv.setMinimumSize(QSize(20, 0))
        self.secondaryStrafeInv.setMaximumSize(QSize(20, 20))
        self.secondaryStrafeInv.setChecked(False)

        self.horizontalLayout_3.addWidget(self.secondaryStrafeInv)


        self.layput.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(controlsDialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(140, 0))
        self.label_10.setMaximumSize(QSize(140, 16777215))
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.primaryVertical = QLineEdit(controlsDialog)
        self.primaryVertical.setObjectName(u"primaryVertical")
        self.primaryVertical.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryVertical.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryVertical.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.primaryVertical)

        self.primaryVerticalInv = QCheckBox(controlsDialog)
        self.primaryVerticalInv.setObjectName(u"primaryVerticalInv")
        self.primaryVerticalInv.setMinimumSize(QSize(16, 0))
        self.primaryVerticalInv.setMaximumSize(QSize(16, 20))
        self.primaryVerticalInv.setChecked(False)

        self.horizontalLayout_4.addWidget(self.primaryVerticalInv)

        self.secondaryVertical = QLineEdit(controlsDialog)
        self.secondaryVertical.setObjectName(u"secondaryVertical")
        self.secondaryVertical.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryVertical.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryVertical.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.secondaryVertical)

        self.secondaryVerticalInv = QCheckBox(controlsDialog)
        self.secondaryVerticalInv.setObjectName(u"secondaryVerticalInv")
        self.secondaryVerticalInv.setMinimumSize(QSize(20, 0))
        self.secondaryVerticalInv.setMaximumSize(QSize(20, 20))
        self.secondaryVerticalInv.setChecked(False)

        self.horizontalLayout_4.addWidget(self.secondaryVerticalInv)


        self.layput.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(controlsDialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(140, 0))
        self.label_11.setMaximumSize(QSize(140, 16777215))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_11)

        self.primaryYaw = QLineEdit(controlsDialog)
        self.primaryYaw.setObjectName(u"primaryYaw")
        self.primaryYaw.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryYaw.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryYaw.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.primaryYaw)

        self.primaryYawInv = QCheckBox(controlsDialog)
        self.primaryYawInv.setObjectName(u"primaryYawInv")
        self.primaryYawInv.setMinimumSize(QSize(16, 0))
        self.primaryYawInv.setMaximumSize(QSize(16, 20))
        self.primaryYawInv.setChecked(False)

        self.horizontalLayout_5.addWidget(self.primaryYawInv)

        self.secondaryYaw = QLineEdit(controlsDialog)
        self.secondaryYaw.setObjectName(u"secondaryYaw")
        self.secondaryYaw.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryYaw.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryYaw.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.secondaryYaw)

        self.secondaryYawInv = QCheckBox(controlsDialog)
        self.secondaryYawInv.setObjectName(u"secondaryYawInv")
        self.secondaryYawInv.setMinimumSize(QSize(20, 0))
        self.secondaryYawInv.setMaximumSize(QSize(20, 20))
        self.secondaryYawInv.setChecked(False)

        self.horizontalLayout_5.addWidget(self.secondaryYawInv)


        self.layput.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(controlsDialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(140, 0))
        self.label_12.setMaximumSize(QSize(140, 16777215))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_12)

        self.primaryRoll = QLineEdit(controlsDialog)
        self.primaryRoll.setObjectName(u"primaryRoll")
        self.primaryRoll.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryRoll.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryRoll.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.primaryRoll)

        self.primaryRollInv = QCheckBox(controlsDialog)
        self.primaryRollInv.setObjectName(u"primaryRollInv")
        self.primaryRollInv.setMinimumSize(QSize(16, 0))
        self.primaryRollInv.setMaximumSize(QSize(16, 20))
        self.primaryRollInv.setChecked(False)

        self.horizontalLayout_6.addWidget(self.primaryRollInv)

        self.secondaryRoll = QLineEdit(controlsDialog)
        self.secondaryRoll.setObjectName(u"secondaryRoll")
        self.secondaryRoll.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryRoll.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryRoll.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.secondaryRoll)

        self.secondaryRollInv = QCheckBox(controlsDialog)
        self.secondaryRollInv.setObjectName(u"secondaryRollInv")
        self.secondaryRollInv.setMinimumSize(QSize(20, 0))
        self.secondaryRollInv.setMaximumSize(QSize(20, 20))
        self.secondaryRollInv.setChecked(False)

        self.horizontalLayout_6.addWidget(self.secondaryRollInv)


        self.layput.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_13 = QLabel(controlsDialog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(140, 0))
        self.label_13.setMaximumSize(QSize(140, 16777215))
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.primaryPitch = QLineEdit(controlsDialog)
        self.primaryPitch.setObjectName(u"primaryPitch")
        self.primaryPitch.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryPitch.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryPitch.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.primaryPitch)

        self.primaryPitchInv = QCheckBox(controlsDialog)
        self.primaryPitchInv.setObjectName(u"primaryPitchInv")
        self.primaryPitchInv.setMinimumSize(QSize(16, 0))
        self.primaryPitchInv.setMaximumSize(QSize(16, 20))
        self.primaryPitchInv.setChecked(False)

        self.horizontalLayout_7.addWidget(self.primaryPitchInv)

        self.secondaryPitch = QLineEdit(controlsDialog)
        self.secondaryPitch.setObjectName(u"secondaryPitch")
        self.secondaryPitch.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryPitch.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryPitch.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.secondaryPitch)

        self.secondaryPitchInv = QCheckBox(controlsDialog)
        self.secondaryPitchInv.setObjectName(u"secondaryPitchInv")
        self.secondaryPitchInv.setMinimumSize(QSize(20, 0))
        self.secondaryPitchInv.setMaximumSize(QSize(20, 20))
        self.secondaryPitchInv.setChecked(False)

        self.horizontalLayout_7.addWidget(self.secondaryPitchInv)


        self.layput.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_18 = QLabel(controlsDialog)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(140, 0))
        self.label_18.setMaximumSize(QSize(140, 16777215))
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_18)

        self.primaryCamAngle = QLineEdit(controlsDialog)
        self.primaryCamAngle.setObjectName(u"primaryCamAngle")
        self.primaryCamAngle.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryCamAngle.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryCamAngle.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.primaryCamAngle)

        self.primaryCamAngleInv = QCheckBox(controlsDialog)
        self.primaryCamAngleInv.setObjectName(u"primaryCamAngleInv")
        self.primaryCamAngleInv.setMinimumSize(QSize(16, 0))
        self.primaryCamAngleInv.setMaximumSize(QSize(16, 20))
        self.primaryCamAngleInv.setChecked(False)

        self.horizontalLayout_12.addWidget(self.primaryCamAngleInv)

        self.secondaryCamAngle = QLineEdit(controlsDialog)
        self.secondaryCamAngle.setObjectName(u"secondaryCamAngle")
        self.secondaryCamAngle.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryCamAngle.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryCamAngle.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.secondaryCamAngle)

        self.secondaryCamAngleInv = QCheckBox(controlsDialog)
        self.secondaryCamAngleInv.setObjectName(u"secondaryCamAngleInv")
        self.secondaryCamAngleInv.setMinimumSize(QSize(20, 0))
        self.secondaryCamAngleInv.setMaximumSize(QSize(20, 20))
        self.secondaryCamAngleInv.setChecked(False)

        self.horizontalLayout_12.addWidget(self.secondaryCamAngleInv)


        self.layput.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_19 = QLabel(controlsDialog)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(140, 0))
        self.label_19.setMaximumSize(QSize(140, 16777215))
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_19)

        self.primaryManRot = QLineEdit(controlsDialog)
        self.primaryManRot.setObjectName(u"primaryManRot")
        self.primaryManRot.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryManRot.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryManRot.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.primaryManRot)

        self.primaryManRotInv = QCheckBox(controlsDialog)
        self.primaryManRotInv.setObjectName(u"primaryManRotInv")
        self.primaryManRotInv.setMinimumSize(QSize(16, 0))
        self.primaryManRotInv.setMaximumSize(QSize(16, 20))
        self.primaryManRotInv.setChecked(False)

        self.horizontalLayout_13.addWidget(self.primaryManRotInv)

        self.secondaryManRot = QLineEdit(controlsDialog)
        self.secondaryManRot.setObjectName(u"secondaryManRot")
        self.secondaryManRot.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryManRot.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryManRot.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.secondaryManRot)

        self.secondaryManRotInv = QCheckBox(controlsDialog)
        self.secondaryManRotInv.setObjectName(u"secondaryManRotInv")
        self.secondaryManRotInv.setMinimumSize(QSize(20, 0))
        self.secondaryManRotInv.setMaximumSize(QSize(20, 20))
        self.secondaryManRotInv.setChecked(False)

        self.horizontalLayout_13.addWidget(self.secondaryManRotInv)


        self.layput.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_22 = QLabel(controlsDialog)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(140, 0))
        self.label_22.setMaximumSize(QSize(140, 16777215))
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_22)

        self.primaryManGrip = QLineEdit(controlsDialog)
        self.primaryManGrip.setObjectName(u"primaryManGrip")
        self.primaryManGrip.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryManGrip.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryManGrip.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.primaryManGrip)

        self.primaryManGripInv = QCheckBox(controlsDialog)
        self.primaryManGripInv.setObjectName(u"primaryManGripInv")
        self.primaryManGripInv.setMinimumSize(QSize(16, 0))
        self.primaryManGripInv.setMaximumSize(QSize(16, 20))
        self.primaryManGripInv.setChecked(False)

        self.horizontalLayout_16.addWidget(self.primaryManGripInv)

        self.secondaryManGrip = QLineEdit(controlsDialog)
        self.secondaryManGrip.setObjectName(u"secondaryManGrip")
        self.secondaryManGrip.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryManGrip.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryManGrip.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.secondaryManGrip)

        self.secondaryManGripInv = QCheckBox(controlsDialog)
        self.secondaryManGripInv.setObjectName(u"secondaryManGripInv")
        self.secondaryManGripInv.setMinimumSize(QSize(20, 0))
        self.secondaryManGripInv.setMaximumSize(QSize(20, 20))
        self.secondaryManGripInv.setChecked(False)

        self.horizontalLayout_16.addWidget(self.secondaryManGripInv)


        self.layput.addLayout(self.horizontalLayout_16)

        self.label_32 = QLabel(controlsDialog)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMouseTracking(False)
        self.label_32.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layput.addWidget(self.label_32)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_33 = QLabel(controlsDialog)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(140, 0))
        self.label_33.setMaximumSize(QSize(140, 16777215))
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_27.addWidget(self.label_33)

        self.primaryForwardBut = QLineEdit(controlsDialog)
        self.primaryForwardBut.setObjectName(u"primaryForwardBut")
        self.primaryForwardBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryForwardBut.setReadOnly(True)

        self.horizontalLayout_27.addWidget(self.primaryForwardBut)

        self.secondaryForwardBut = QLineEdit(controlsDialog)
        self.secondaryForwardBut.setObjectName(u"secondaryForwardBut")
        self.secondaryForwardBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryForwardBut.setReadOnly(True)

        self.horizontalLayout_27.addWidget(self.secondaryForwardBut)


        self.layput.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_34 = QLabel(controlsDialog)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(140, 0))
        self.label_34.setMaximumSize(QSize(140, 16777215))
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.label_34)

        self.primaryBackwardsBut = QLineEdit(controlsDialog)
        self.primaryBackwardsBut.setObjectName(u"primaryBackwardsBut")
        self.primaryBackwardsBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryBackwardsBut.setReadOnly(True)

        self.horizontalLayout_28.addWidget(self.primaryBackwardsBut)

        self.secondaryBackwardsBut = QLineEdit(controlsDialog)
        self.secondaryBackwardsBut.setObjectName(u"secondaryBackwardsBut")
        self.secondaryBackwardsBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryBackwardsBut.setReadOnly(True)

        self.horizontalLayout_28.addWidget(self.secondaryBackwardsBut)


        self.layput.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_35 = QLabel(controlsDialog)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(140, 0))
        self.label_35.setMaximumSize(QSize(140, 16777215))
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_35)

        self.primaryLeftBut = QLineEdit(controlsDialog)
        self.primaryLeftBut.setObjectName(u"primaryLeftBut")
        self.primaryLeftBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryLeftBut.setReadOnly(True)

        self.horizontalLayout_29.addWidget(self.primaryLeftBut)

        self.secondaryLeftBut = QLineEdit(controlsDialog)
        self.secondaryLeftBut.setObjectName(u"secondaryLeftBut")
        self.secondaryLeftBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryLeftBut.setReadOnly(True)

        self.horizontalLayout_29.addWidget(self.secondaryLeftBut)


        self.layput.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_36 = QLabel(controlsDialog)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(140, 0))
        self.label_36.setMaximumSize(QSize(140, 16777215))
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.label_36)

        self.primaryRightBut = QLineEdit(controlsDialog)
        self.primaryRightBut.setObjectName(u"primaryRightBut")
        self.primaryRightBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryRightBut.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.primaryRightBut)

        self.secondaryRightBut = QLineEdit(controlsDialog)
        self.secondaryRightBut.setObjectName(u"secondaryRightBut")
        self.secondaryRightBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryRightBut.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.secondaryRightBut)


        self.layput.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_37 = QLabel(controlsDialog)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(140, 0))
        self.label_37.setMaximumSize(QSize(140, 16777215))
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label_37)

        self.primaryRotLeftBut = QLineEdit(controlsDialog)
        self.primaryRotLeftBut.setObjectName(u"primaryRotLeftBut")
        self.primaryRotLeftBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryRotLeftBut.setReadOnly(True)

        self.horizontalLayout_31.addWidget(self.primaryRotLeftBut)

        self.secondaryRotLeftBut = QLineEdit(controlsDialog)
        self.secondaryRotLeftBut.setObjectName(u"secondaryRotLeftBut")
        self.secondaryRotLeftBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryRotLeftBut.setReadOnly(True)

        self.horizontalLayout_31.addWidget(self.secondaryRotLeftBut)


        self.layput.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_38 = QLabel(controlsDialog)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(140, 0))
        self.label_38.setMaximumSize(QSize(140, 16777215))
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_38)

        self.primaryRotRightBut = QLineEdit(controlsDialog)
        self.primaryRotRightBut.setObjectName(u"primaryRotRightBut")
        self.primaryRotRightBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryRotRightBut.setReadOnly(True)

        self.horizontalLayout_32.addWidget(self.primaryRotRightBut)

        self.secondaryRotRightBut = QLineEdit(controlsDialog)
        self.secondaryRotRightBut.setObjectName(u"secondaryRotRightBut")
        self.secondaryRotRightBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryRotRightBut.setReadOnly(True)

        self.horizontalLayout_32.addWidget(self.secondaryRotRightBut)


        self.layput.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_39 = QLabel(controlsDialog)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(140, 0))
        self.label_39.setMaximumSize(QSize(140, 16777215))
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.label_39)

        self.primaryDownBut = QLineEdit(controlsDialog)
        self.primaryDownBut.setObjectName(u"primaryDownBut")
        self.primaryDownBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryDownBut.setReadOnly(True)

        self.horizontalLayout_33.addWidget(self.primaryDownBut)

        self.secondaryDownBut = QLineEdit(controlsDialog)
        self.secondaryDownBut.setObjectName(u"secondaryDownBut")
        self.secondaryDownBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryDownBut.setReadOnly(True)

        self.horizontalLayout_33.addWidget(self.secondaryDownBut)


        self.layput.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_40 = QLabel(controlsDialog)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(140, 0))
        self.label_40.setMaximumSize(QSize(140, 16777215))
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_34.addWidget(self.label_40)

        self.primaryUpBut = QLineEdit(controlsDialog)
        self.primaryUpBut.setObjectName(u"primaryUpBut")
        self.primaryUpBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryUpBut.setReadOnly(True)

        self.horizontalLayout_34.addWidget(self.primaryUpBut)

        self.secondaryUpBut = QLineEdit(controlsDialog)
        self.secondaryUpBut.setObjectName(u"secondaryUpBut")
        self.secondaryUpBut.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryUpBut.setReadOnly(True)

        self.horizontalLayout_34.addWidget(self.secondaryUpBut)


        self.layput.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_14 = QLabel(controlsDialog)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(140, 0))
        self.label_14.setMaximumSize(QSize(140, 16777215))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_14)

        self.primaryRollInc = QLineEdit(controlsDialog)
        self.primaryRollInc.setObjectName(u"primaryRollInc")
        self.primaryRollInc.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryRollInc.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.primaryRollInc)

        self.secondaryRollInc = QLineEdit(controlsDialog)
        self.secondaryRollInc.setObjectName(u"secondaryRollInc")
        self.secondaryRollInc.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryRollInc.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.secondaryRollInc)


        self.layput.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_15 = QLabel(controlsDialog)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(140, 0))
        self.label_15.setMaximumSize(QSize(140, 16777215))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_15)

        self.primaryRollDec = QLineEdit(controlsDialog)
        self.primaryRollDec.setObjectName(u"primaryRollDec")
        self.primaryRollDec.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryRollDec.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryRollDec.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.primaryRollDec)

        self.secondaryRollDec = QLineEdit(controlsDialog)
        self.secondaryRollDec.setObjectName(u"secondaryRollDec")
        self.secondaryRollDec.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryRollDec.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryRollDec.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.secondaryRollDec)


        self.layput.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_29 = QLabel(controlsDialog)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(140, 0))
        self.label_29.setMaximumSize(QSize(140, 16777215))
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_29)

        self.primaryPitchInc = QLineEdit(controlsDialog)
        self.primaryPitchInc.setObjectName(u"primaryPitchInc")
        self.primaryPitchInc.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryPitchInc.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryPitchInc.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.primaryPitchInc)

        self.secondaryPitchInc = QLineEdit(controlsDialog)
        self.secondaryPitchInc.setObjectName(u"secondaryPitchInc")
        self.secondaryPitchInc.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryPitchInc.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryPitchInc.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.secondaryPitchInc)


        self.layput.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_30 = QLabel(controlsDialog)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(140, 0))
        self.label_30.setMaximumSize(QSize(140, 16777215))
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.label_30)

        self.primaryPitchDec = QLineEdit(controlsDialog)
        self.primaryPitchDec.setObjectName(u"primaryPitchDec")
        self.primaryPitchDec.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryPitchDec.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryPitchDec.setReadOnly(True)

        self.horizontalLayout_26.addWidget(self.primaryPitchDec)

        self.secondaryPitchDec = QLineEdit(controlsDialog)
        self.secondaryPitchDec.setObjectName(u"secondaryPitchDec")
        self.secondaryPitchDec.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryPitchDec.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryPitchDec.setReadOnly(True)

        self.horizontalLayout_26.addWidget(self.secondaryPitchDec)


        self.layput.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(controlsDialog)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(140, 0))
        self.label_16.setMaximumSize(QSize(140, 16777215))
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_16)

        self.primaryCamUp = QLineEdit(controlsDialog)
        self.primaryCamUp.setObjectName(u"primaryCamUp")
        self.primaryCamUp.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryCamUp.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryCamUp.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.primaryCamUp)

        self.secondaryCamUp = QLineEdit(controlsDialog)
        self.secondaryCamUp.setObjectName(u"secondaryCamUp")
        self.secondaryCamUp.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryCamUp.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryCamUp.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.secondaryCamUp)


        self.layput.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_17 = QLabel(controlsDialog)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(140, 0))
        self.label_17.setMaximumSize(QSize(140, 16777215))
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_17)

        self.primaryCamDown = QLineEdit(controlsDialog)
        self.primaryCamDown.setObjectName(u"primaryCamDown")
        self.primaryCamDown.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryCamDown.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryCamDown.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.primaryCamDown)

        self.secondaryCamDown = QLineEdit(controlsDialog)
        self.secondaryCamDown.setObjectName(u"secondaryCamDown")
        self.secondaryCamDown.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryCamDown.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryCamDown.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.secondaryCamDown)


        self.layput.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_20 = QLabel(controlsDialog)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(140, 0))
        self.label_20.setMaximumSize(QSize(140, 16777215))
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_20)

        self.primaryManLeft = QLineEdit(controlsDialog)
        self.primaryManLeft.setObjectName(u"primaryManLeft")
        self.primaryManLeft.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryManLeft.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryManLeft.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.primaryManLeft)

        self.secondaryManLeft = QLineEdit(controlsDialog)
        self.secondaryManLeft.setObjectName(u"secondaryManLeft")
        self.secondaryManLeft.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryManLeft.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryManLeft.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.secondaryManLeft)


        self.layput.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_21 = QLabel(controlsDialog)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(140, 0))
        self.label_21.setMaximumSize(QSize(140, 16777215))
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_21)

        self.primaryManRight = QLineEdit(controlsDialog)
        self.primaryManRight.setObjectName(u"primaryManRight")
        self.primaryManRight.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryManRight.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryManRight.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.primaryManRight)

        self.secondaryManRight = QLineEdit(controlsDialog)
        self.secondaryManRight.setObjectName(u"secondaryManRight")
        self.secondaryManRight.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryManRight.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryManRight.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.secondaryManRight)


        self.layput.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_23 = QLabel(controlsDialog)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(140, 0))
        self.label_23.setMaximumSize(QSize(140, 16777215))
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_23)

        self.primaryManClose = QLineEdit(controlsDialog)
        self.primaryManClose.setObjectName(u"primaryManClose")
        self.primaryManClose.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryManClose.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryManClose.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.primaryManClose)

        self.secondaryManClose = QLineEdit(controlsDialog)
        self.secondaryManClose.setObjectName(u"secondaryManClose")
        self.secondaryManClose.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryManClose.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryManClose.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.secondaryManClose)


        self.layput.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_24 = QLabel(controlsDialog)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(140, 0))
        self.label_24.setMaximumSize(QSize(140, 16777215))
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_24)

        self.primaryManOpen = QLineEdit(controlsDialog)
        self.primaryManOpen.setObjectName(u"primaryManOpen")
        self.primaryManOpen.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryManOpen.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryManOpen.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.primaryManOpen)

        self.secondaryManOpen = QLineEdit(controlsDialog)
        self.secondaryManOpen.setObjectName(u"secondaryManOpen")
        self.secondaryManOpen.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryManOpen.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryManOpen.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.secondaryManOpen)


        self.layput.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_25 = QLabel(controlsDialog)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(140, 0))
        self.label_25.setMaximumSize(QSize(140, 16777215))
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_25)

        self.primaryLightsOn = QLineEdit(controlsDialog)
        self.primaryLightsOn.setObjectName(u"primaryLightsOn")
        self.primaryLightsOn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryLightsOn.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryLightsOn.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.primaryLightsOn)

        self.secondaryLightsOn = QLineEdit(controlsDialog)
        self.secondaryLightsOn.setObjectName(u"secondaryLightsOn")
        self.secondaryLightsOn.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryLightsOn.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryLightsOn.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.secondaryLightsOn)


        self.layput.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_26 = QLabel(controlsDialog)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(140, 0))
        self.label_26.setMaximumSize(QSize(140, 16777215))
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_26)

        self.primaryPosReset = QLineEdit(controlsDialog)
        self.primaryPosReset.setObjectName(u"primaryPosReset")
        self.primaryPosReset.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryPosReset.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryPosReset.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.primaryPosReset)

        self.secondaryPosReset = QLineEdit(controlsDialog)
        self.secondaryPosReset.setObjectName(u"secondaryPosReset")
        self.secondaryPosReset.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryPosReset.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryPosReset.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.secondaryPosReset)


        self.layput.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_27 = QLabel(controlsDialog)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(140, 0))
        self.label_27.setMaximumSize(QSize(140, 16777215))
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_27)

        self.primaryMaster = QLineEdit(controlsDialog)
        self.primaryMaster.setObjectName(u"primaryMaster")
        self.primaryMaster.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryMaster.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.primaryMaster.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.primaryMaster)

        self.secondaryMaster = QLineEdit(controlsDialog)
        self.secondaryMaster.setObjectName(u"secondaryMaster")
        self.secondaryMaster.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryMaster.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.secondaryMaster.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.secondaryMaster)


        self.layput.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_28 = QLabel(controlsDialog)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_24.addWidget(self.label_28)

        self.profileNameVal = QLineEdit(controlsDialog)
        self.profileNameVal.setObjectName(u"profileNameVal")

        self.horizontalLayout_24.addWidget(self.profileNameVal)

        self.saveProfileBut = QPushButton(controlsDialog)
        self.saveProfileBut.setObjectName(u"saveProfileBut")

        self.horizontalLayout_24.addWidget(self.saveProfileBut)

        self.loadProfileMan = QPushButton(controlsDialog)
        self.loadProfileMan.setObjectName(u"loadProfileMan")

        self.horizontalLayout_24.addWidget(self.loadProfileMan)


        self.layput.addLayout(self.horizontalLayout_24)


        self.verticalLayout_2.addLayout(self.layput)


        self.retranslateUi(controlsDialog)

        QMetaObject.connectSlotsByName(controlsDialog)
    # setupUi

    def retranslateUi(self, controlsDialog):
        controlsDialog.setWindowTitle(QCoreApplication.translate("controlsDialog", u"Controls", None))
        self.inputProgressBar.setFormat(QCoreApplication.translate("controlsDialog", u"%p%", None))
        self.label.setText(QCoreApplication.translate("controlsDialog", u"Primary Device:", None))
        self.label_2.setText(QCoreApplication.translate("controlsDialog", u"Secondary Device:", None))
        self.label_3.setText(QCoreApplication.translate("controlsDialog", u"Control", None))
        self.label_4.setText(QCoreApplication.translate("controlsDialog", u"Primary input", None))
        self.label_5.setText(QCoreApplication.translate("controlsDialog", u"Inv", None))
        self.label_7.setText(QCoreApplication.translate("controlsDialog", u"Secondary input", None))
        self.label_6.setText(QCoreApplication.translate("controlsDialog", u"Inv", None))
        self.label_31.setText(QCoreApplication.translate("controlsDialog", u"Axes", None))
        self.label_8.setText(QCoreApplication.translate("controlsDialog", u"Forward", None))
        self.primaryForwardInv.setText("")
        self.secondaryForwardInv.setText("")
        self.label_9.setText(QCoreApplication.translate("controlsDialog", u"Strafe", None))
        self.primaryStrafeInv.setText("")
        self.secondaryStrafeInv.setText("")
        self.label_10.setText(QCoreApplication.translate("controlsDialog", u"Vertical", None))
        self.primaryVerticalInv.setText("")
        self.secondaryVerticalInv.setText("")
        self.label_11.setText(QCoreApplication.translate("controlsDialog", u"Yaw", None))
        self.primaryYawInv.setText("")
        self.secondaryYawInv.setText("")
        self.label_12.setText(QCoreApplication.translate("controlsDialog", u"Roll", None))
        self.primaryRollInv.setText("")
        self.secondaryRollInv.setText("")
        self.label_13.setText(QCoreApplication.translate("controlsDialog", u"Pitch", None))
        self.primaryPitchInv.setText("")
        self.secondaryPitchInv.setText("")
        self.label_18.setText(QCoreApplication.translate("controlsDialog", u"Camera angle (alt)", None))
        self.primaryCamAngleInv.setText("")
        self.secondaryCamAngleInv.setText("")
        self.label_19.setText(QCoreApplication.translate("controlsDialog", u"Manipalator rotate", None))
        self.primaryManRotInv.setText("")
        self.secondaryManRotInv.setText("")
        self.label_22.setText(QCoreApplication.translate("controlsDialog", u"Manipulator grip", None))
        self.primaryManGripInv.setText("")
        self.secondaryManGripInv.setText("")
        self.label_32.setText(QCoreApplication.translate("controlsDialog", u"Buttons", None))
        self.label_33.setText(QCoreApplication.translate("controlsDialog", u"Move forward", None))
        self.label_34.setText(QCoreApplication.translate("controlsDialog", u"Move backwards", None))
        self.label_35.setText(QCoreApplication.translate("controlsDialog", u"Move left", None))
        self.label_36.setText(QCoreApplication.translate("controlsDialog", u"Move right", None))
        self.label_37.setText(QCoreApplication.translate("controlsDialog", u"Rotate left", None))
        self.label_38.setText(QCoreApplication.translate("controlsDialog", u"Rotate right", None))
        self.label_39.setText(QCoreApplication.translate("controlsDialog", u"Move down", None))
        self.label_40.setText(QCoreApplication.translate("controlsDialog", u"Move up", None))
        self.label_14.setText(QCoreApplication.translate("controlsDialog", u"Roll increment", None))
        self.label_15.setText(QCoreApplication.translate("controlsDialog", u"Roll decrement", None))
        self.label_29.setText(QCoreApplication.translate("controlsDialog", u"Pitch increment", None))
        self.label_30.setText(QCoreApplication.translate("controlsDialog", u"Pitch decrement", None))
        self.label_16.setText(QCoreApplication.translate("controlsDialog", u"Camera rotate up", None))
        self.label_17.setText(QCoreApplication.translate("controlsDialog", u"Camera rotate down", None))
        self.label_20.setText(QCoreApplication.translate("controlsDialog", u"Manipalator rotate left", None))
        self.label_21.setText(QCoreApplication.translate("controlsDialog", u"Manipalator rotate right", None))
        self.label_23.setText(QCoreApplication.translate("controlsDialog", u"Manipulator grip close", None))
        self.label_24.setText(QCoreApplication.translate("controlsDialog", u"Manipulator grip open", None))
        self.label_25.setText(QCoreApplication.translate("controlsDialog", u"Lights on/off", None))
        self.label_26.setText(QCoreApplication.translate("controlsDialog", u"Reset position", None))
        self.label_27.setText(QCoreApplication.translate("controlsDialog", u"Master switch", None))
        self.label_28.setText(QCoreApplication.translate("controlsDialog", u"Profile Name:", None))
        self.profileNameVal.setText(QCoreApplication.translate("controlsDialog", u"default", None))
        self.saveProfileBut.setText(QCoreApplication.translate("controlsDialog", u"Save Profile", None))
        self.loadProfileMan.setText(QCoreApplication.translate("controlsDialog", u"Load Profile", None))
    # retranslateUi

