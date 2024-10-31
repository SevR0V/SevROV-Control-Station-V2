# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        if not settingsDialog.objectName():
            settingsDialog.setObjectName(u"settingsDialog")
        settingsDialog.resize(369, 373)
        self.horizontalLayout_6 = QHBoxLayout(settingsDialog)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox = QGroupBox(settingsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 0))
        self.label.setMaximumSize(QSize(40, 16777215))
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.ipVal = QLineEdit(self.groupBox)
        self.ipVal.setObjectName(u"ipVal")

        self.horizontalLayout_2.addWidget(self.ipVal)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 0))
        self.label_2.setMaximumSize(QSize(40, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.portVal = QLineEdit(self.groupBox)
        self.portVal.setObjectName(u"portVal")

        self.horizontalLayout.addWidget(self.portVal)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_5.addWidget(self.groupBox)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.resetIMUBut = QPushButton(settingsDialog)
        self.resetIMUBut.setObjectName(u"resetIMUBut")

        self.verticalLayout_9.addWidget(self.resetIMUBut)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.groupBox_2 = QGroupBox(settingsDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 24))
        self.label_7.setMaximumSize(QSize(16777215, 24))

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 24))
        self.label_3.setMaximumSize(QSize(16777215, 24))

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 24))
        self.label_4.setMaximumSize(QSize(16777215, 24))

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 24))
        self.label_5.setMaximumSize(QSize(16777215, 24))

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 24))
        self.label_6.setMaximumSize(QSize(16777215, 24))

        self.verticalLayout_3.addWidget(self.label_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 24))
        self.label_8.setMaximumSize(QSize(16777215, 24))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_8)

        self.rollKPval = QDoubleSpinBox(self.groupBox_2)
        self.rollKPval.setObjectName(u"rollKPval")
        self.rollKPval.setMaximum(99999.000000000000000)
        self.rollKPval.setSingleStep(0.100000000000000)

        self.verticalLayout_4.addWidget(self.rollKPval)

        self.pitchKPval = QDoubleSpinBox(self.groupBox_2)
        self.pitchKPval.setObjectName(u"pitchKPval")
        self.pitchKPval.setMaximum(99999.000000000000000)
        self.pitchKPval.setSingleStep(0.100000000000000)

        self.verticalLayout_4.addWidget(self.pitchKPval)

        self.yawKPval = QDoubleSpinBox(self.groupBox_2)
        self.yawKPval.setObjectName(u"yawKPval")
        self.yawKPval.setMaximum(99999.000000000000000)
        self.yawKPval.setSingleStep(0.100000000000000)

        self.verticalLayout_4.addWidget(self.yawKPval)

        self.depthKPval = QDoubleSpinBox(self.groupBox_2)
        self.depthKPval.setObjectName(u"depthKPval")
        self.depthKPval.setMaximum(99999.000000000000000)
        self.depthKPval.setSingleStep(0.100000000000000)

        self.verticalLayout_4.addWidget(self.depthKPval)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 24))
        self.label_9.setMaximumSize(QSize(16777215, 24))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_9)

        self.rollKIval = QDoubleSpinBox(self.groupBox_2)
        self.rollKIval.setObjectName(u"rollKIval")
        self.rollKIval.setMaximum(99999.000000000000000)
        self.rollKIval.setSingleStep(0.100000000000000)

        self.verticalLayout_5.addWidget(self.rollKIval)

        self.pitchKIval = QDoubleSpinBox(self.groupBox_2)
        self.pitchKIval.setObjectName(u"pitchKIval")
        self.pitchKIval.setMaximum(99999.000000000000000)
        self.pitchKIval.setSingleStep(0.100000000000000)

        self.verticalLayout_5.addWidget(self.pitchKIval)

        self.yawKIval = QDoubleSpinBox(self.groupBox_2)
        self.yawKIval.setObjectName(u"yawKIval")
        self.yawKIval.setMaximum(99999.000000000000000)
        self.yawKIval.setSingleStep(0.100000000000000)

        self.verticalLayout_5.addWidget(self.yawKIval)

        self.yawKIval_2 = QDoubleSpinBox(self.groupBox_2)
        self.yawKIval_2.setObjectName(u"yawKIval_2")
        self.yawKIval_2.setMaximum(99999.000000000000000)
        self.yawKIval_2.setSingleStep(0.100000000000000)

        self.verticalLayout_5.addWidget(self.yawKIval_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 24))
        self.label_10.setMaximumSize(QSize(16777215, 24))
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_10)

        self.rollKDval = QDoubleSpinBox(self.groupBox_2)
        self.rollKDval.setObjectName(u"rollKDval")
        self.rollKDval.setMaximum(99999.000000000000000)
        self.rollKDval.setSingleStep(0.010000000000000)

        self.verticalLayout_6.addWidget(self.rollKDval)

        self.pitchKDval = QDoubleSpinBox(self.groupBox_2)
        self.pitchKDval.setObjectName(u"pitchKDval")
        self.pitchKDval.setMaximum(99999.000000000000000)
        self.pitchKDval.setSingleStep(0.010000000000000)

        self.verticalLayout_6.addWidget(self.pitchKDval)

        self.yawKDval = QDoubleSpinBox(self.groupBox_2)
        self.yawKDval.setObjectName(u"yawKDval")
        self.yawKDval.setMaximum(99999.000000000000000)
        self.yawKDval.setSingleStep(0.010000000000000)

        self.verticalLayout_6.addWidget(self.yawKDval)

        self.yawKDval_2 = QDoubleSpinBox(self.groupBox_2)
        self.yawKDval_2.setObjectName(u"yawKDval_2")
        self.yawKDval_2.setMaximum(99999.000000000000000)
        self.yawKDval_2.setSingleStep(0.010000000000000)

        self.verticalLayout_6.addWidget(self.yawKDval_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.updatePIDBut = QPushButton(self.groupBox_2)
        self.updatePIDBut.setObjectName(u"updatePIDBut")

        self.horizontalLayout_4.addWidget(self.updatePIDBut)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.verticalLayout_10.addWidget(self.groupBox_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)


        self.retranslateUi(settingsDialog)

        QMetaObject.connectSlotsByName(settingsDialog)
    # setupUi

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(QCoreApplication.translate("settingsDialog", u"Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("settingsDialog", u"Connection", None))
        self.label.setText(QCoreApplication.translate("settingsDialog", u"ROV IP:", None))
        self.ipVal.setInputMask(QCoreApplication.translate("settingsDialog", u"000.000.000.000", None))
        self.ipVal.setText(QCoreApplication.translate("settingsDialog", u"192.168.0.1", None))
        self.label_2.setText(QCoreApplication.translate("settingsDialog", u"Port:", None))
        self.portVal.setInputMask(QCoreApplication.translate("settingsDialog", u"0000", None))
        self.portVal.setText(QCoreApplication.translate("settingsDialog", u"1337", None))
        self.resetIMUBut.setText(QCoreApplication.translate("settingsDialog", u"Reset IMU", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("settingsDialog", u"PID", None))
        self.label_7.setText("")
        self.label_3.setText(QCoreApplication.translate("settingsDialog", u"Roll:", None))
        self.label_4.setText(QCoreApplication.translate("settingsDialog", u"Pitch:", None))
        self.label_5.setText(QCoreApplication.translate("settingsDialog", u"Yaw:", None))
        self.label_6.setText(QCoreApplication.translate("settingsDialog", u"Depth:", None))
        self.label_8.setText(QCoreApplication.translate("settingsDialog", u"kP", None))
        self.label_9.setText(QCoreApplication.translate("settingsDialog", u"kI", None))
        self.label_10.setText(QCoreApplication.translate("settingsDialog", u"kD", None))
        self.updatePIDBut.setText(QCoreApplication.translate("settingsDialog", u"Update PID", None))
    # retranslateUi

