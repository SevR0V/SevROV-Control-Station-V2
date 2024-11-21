from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer
from UI.manipulatorControlWindow import Ui_Form
from enum import IntEnum
import copy

class GripState(IntEnum):
    UWMANIPULATOR_GRIP_OPEN = 0
    UWMANIPULATOR_GRIP_CLOSE = 1
    UWMANIPULATOR_GRIP_STOP = 2

class ManipulatorControlWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.manStatusLabel.setStyleSheet("color:red;")
        self.ui.manEnableControl.setCheckable(False)
        
        self.manControlEnabled = False
        self.manFlags = [False]*4
        self.manAngles = [0.0]*3
        self.tManAngles = [0.0]*3
        self.manPhaseCurrents = [[0.0]*2]*3
        self.manVoltages = [0.0]*3
        self.gripState = GripState.UWMANIPULATOR_GRIP_STOP
        self.manTelemetryObtained = False
        self.manTelemetryFirstTime = True

        self.dial1ToValFlag = False
        self.val1ToDialFlag = False
        self.dial2ToValFlag = False
        self.val2ToDialFlag = False
        self.dial3ToValFlag = False
        self.val3ToDialFlag = False
        self.axis1ValInputWaitTimer = QTimer()
        self.axis1ValInputWaitTimer.timeout.connect(self.axis1ControlVal_collectAngle)
        self.axis2ValInputWaitTimer = QTimer()
        self.axis2ValInputWaitTimer.timeout.connect(self.axis2ControlVal_collectAngle)
        self.axis3ValInputWaitTimer = QTimer()
        self.axis3ValInputWaitTimer.timeout.connect(self.axis3ControlVal_collectAngle)

        self.setup_connections()
    
    def setup_connections(self):
        self.ui.axis1ControlDial.valueChanged.connect(self.axis1ControlDial_valueChanged)
        self.ui.axis2ControlDial.valueChanged.connect(self.axis2ControlDial_valueChanged)
        self.ui.axis3ControlDial.valueChanged.connect(self.axis3ControlDial_valueChanged)

        self.ui.gripOpenButton.pressed.connect(self.gripOpenButton_pressed)
        self.ui.gripOpenButton.released.connect(self.gripOpenCloseButton_release)

        self.ui.gripCloseButton.pressed.connect(self.gripCloseButton_pressed)
        self.ui.gripCloseButton.released.connect(self.gripOpenCloseButton_release)

        self.ui.axis1ControlVal.valueChanged.connect(self.axis1ControlVal_valueChanged)
        self.ui.axis2ControlVal.valueChanged.connect(self.axis2ControlVal_valueChanged)
        self.ui.axis3ControlVal.valueChanged.connect(self.axis3ControlVal_valueChanged)
        
        self.ui.manEnableControl.stateChanged.connect(self.manEnableControl_state_changed)

    def axis1ControlDial_valueChanged(self):
        if self.val1ToDialFlag:
            self.val1ToDialFlag = False
            return
        self.manAngles[0] = self.ui.axis1ControlDial.value()/10
        self.manFlags[0] = True
        self.dial1ToValFlag = True
        self.ui.axis1ControlVal.setValue(self.manAngles[0])

    def axis1ControlVal_valueChanged(self):
        if self.dial1ToValFlag:
            self.dial1ToValFlag = False
            return
        if self.axis1ValInputWaitTimer.isActive:
            self.axis1ValInputWaitTimer.stop()
        self.axis1ValInputWaitTimer.start(1000)
        self.val1ToDialFlag = True
        self.ui.axis1ControlDial.setValue(self.ui.axis1ControlVal.value()*10)

    def axis1ControlVal_collectAngle(self):
        self.manAngles[0] = self.ui.axis1ControlVal.value()
        self.manFlags[0] = True
        self.axis1ValInputWaitTimer.stop()
        
    def axis2ControlDial_valueChanged(self):
        if self.val2ToDialFlag:
            self.val2ToDialFlag = False
            return
        self.manAngles[1] = self.ui.axis2ControlDial.value()/10
        self.manFlags[1] = True
        self.dial2ToValFlag = True
        self.ui.axis2ControlVal.setValue(self.manAngles[1])

    def axis2ControlVal_valueChanged(self):
        if self.dial2ToValFlag:
            self.dial2ToValFlag = False
            return
        if self.axis2ValInputWaitTimer.isActive:
            self.axis2ValInputWaitTimer.stop()
        self.axis2ValInputWaitTimer.start(1000)
        self.val2ToDialFlag = True
        self.ui.axis2ControlDial.setValue(self.ui.axis2ControlVal.value()*10)

    def axis2ControlVal_collectAngle(self):
        self.manAngles[1] = self.ui.axis2ControlVal.value()
        self.manFlags[1] = True
        self.axis2ValInputWaitTimer.stop()
    
    def axis3ControlDial_valueChanged(self):
        if self.val3ToDialFlag:
            self.val3ToDialFlag = False
            return
        self.manAngles[2] = self.ui.axis3ControlDial.value()/10
        self.manFlags[2] = True
        self.dial3ToValFlag = True
        self.ui.axis3ControlVal.setValue(self.manAngles[2])

    def axis3ControlVal_valueChanged(self):
        if self.dial3ToValFlag:
            self.dial3ToValFlag = False
            return
        if self.axis3ValInputWaitTimer.isActive:
            self.axis3ValInputWaitTimer.stop()
        self.axis3ValInputWaitTimer.start(1000)
        self.val3ToDialFlag = True
        self.ui.axis3ControlDial.setValue(self.ui.axis3ControlVal.value()*10)

    def axis3ControlVal_collectAngle(self):
        self.manAngles[2] = self.ui.axis3ControlVal.value()
        self.manFlags[2] = True
        self.axis3ValInputWaitTimer.stop()
    
    def gripOpenButton_pressed(self):
        self.gripState = GripState.UWMANIPULATOR_GRIP_OPEN
        self.manFlags[3] = True
        print("grip open")

    def gripCloseButton_pressed(self):
        self.gripState = GripState.UWMANIPULATOR_GRIP_CLOSE
        self.manFlags[3] = True
        print("grip close")

    def gripOpenCloseButton_release(self):
        self.gripState = GripState.UWMANIPULATOR_GRIP_STOP
        self.manFlags[3] = True
        print("grip stop")

    def window_Update(self):
        self.ui.axis1RealVal.setText(str("%.2f"%self.tManAngles[0]))
        self.ui.axis2RealVal.setText(str("%.2f"%self.tManAngles[1]))
        self.ui.axis3RealVal.setText(str("%.2f"%self.tManAngles[2]))
        self.ui.axis1RealValDial.setValue(int(self.tManAngles[0]*10))
        self.ui.axis2RealValDial.setValue(int(self.tManAngles[1]*10))
        self.ui.axis3RealValDial.setValue(int(self.tManAngles[2]*10))
        self.ui.axis1PhaseACur.setText(str("%.2f"%self.manPhaseCurrents[0][0]))
        self.ui.axis1PhaseBCur.setText(str("%.2f"%self.manPhaseCurrents[0][1]))
        self.ui.axis1Voltage.setText(str("%.2f"%self.manVoltages[0]))
        self.ui.axis2PhaseACur.setText(str("%.2f"%self.manPhaseCurrents[1][0]))
        self.ui.axis2PhaseBCur.setText(str("%.2f"%self.manPhaseCurrents[1][1]))
        self.ui.axis2Voltage.setText(str("%.2f"%self.manVoltages[1]))
        self.ui.axis3PhaseACur.setText(str("%.2f"%self.manPhaseCurrents[2][0]))
        self.ui.axis3PhaseBCur.setText(str("%.2f"%self.manPhaseCurrents[2][1]))
        self.ui.axis3Voltage.setText(str("%.2f"%self.manVoltages[2]))

        if self.manTelemetryObtained:
            self.ui.manStatusLabel.setText("ONLINE")
            self.ui.manStatusLabel.setStyleSheet("color:green;")
            self.ui.manEnableControl.setCheckable(True)
            if self.manTelemetryFirstTime:
                self.manAngles = copy.copy(self.tManAngles)
                self.ui.axis1ControlDial.setValue(self.manAngles[0]*10)
                self.ui.axis2ControlDial.setValue(self.manAngles[1]*10)
                self.ui.axis3ControlDial.setValue(self.manAngles[2]*10)
                self.manTelemetryFirstTime = False
        else:
            self.ui.manStatusLabel.setText("OFFLINE")
            self.ui.manStatusLabel.setStyleSheet("color:red;")
            self.ui.manEnableControl.setCheckable(False)
            self.ui.manEnableControl.setChecked(False)
            self.manControlEnabled = False

    def manEnableControl_state_changed(self):
        self.manControlEnabled = self.ui.manEnableControl.isChecked()
