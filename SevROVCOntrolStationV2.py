import sys, pygame, time, struct
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from AsyncioThread import AsyncioThread
from SettingsDialog import SettingsDialog
from ControlsDialog import ControlsDialog
from UI.main_window import Ui_MainWindow
from ManipulatorControlWindow import ManipulatorControlWindow, GripState
import numpy as np
import time
# controlFlags, forward, strafe, vertical, rotation, rollInc, pitchInc, powerTarget, cameraRotate, manipulatorGrip, manipulatorRotate, rollKp, rollKi, rollKd, pitchKp, pitchKi, pitchKd, yawKp, yawKi, yawKd, depthKp, depthKi, depthKd
# flags = MASTER, lightState, stabRoll, stabPitch, stabYaw, stabDepth, resetPosition, resetIMU, updatePID

#ERRORFLAGS, roll, pitch, yaw, depth, batVoltage, batCharge, batCurrent, rollSP, pitchSP

JOYSTICK_DEADZONE = 0.03
TIMER_PERIOD_MS = 50

UDP_FLAGS_MASTERx = np.uint64(1 << 0)
UDP_FLAGS_LIGHT_STATEx = np.uint64(1 << 1)
UDP_FLAGS_STAB_ROLLx = np.uint64(1 << 2)
UDP_FLAGS_STAB_PITCHx = np.uint64(1 << 3)
UDP_FLAGS_STAB_YAWx = np.uint64(1 << 4)
UDP_FLAGS_STAB_DEPTHx = np.uint64(1 << 5)
UDP_FLAGS_RESET_POSITIONx = np.uint64(1 << 6)
UDP_FLAGS_RESET_IMUx = np.uint64(1 << 7)
UDP_FLAGS_UPDATE_PIDx = np.uint64(1 << 8)
UDP_FLAGS_MANIPULATOR_ANGLE_1_UPDATE = np.uint64(1 << 9)
UDP_FLAGS_MANIPULATOR_ANGLE_2_UPDATE = np.uint64(1 << 10)
UDP_FLAGS_MANIPULATOR_ANGLE_3_UPDATE = np.uint64(1 << 11)
UDP_FLAGS_MANIPULATOR_GRIP_UPDATE = np.uint64(1 << 12)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.masterStatus.setStyleSheet("color:green;")
        self.ui.onlineStatus.setStyleSheet("color:red;")
        self.primaryIdx = -1
        self.secondaryIdx = -1
        pygame.init()
        pygame.joystick.init()
        self.primaryJoystick = None
        self.secondaryJoystick = None            
        
        self.settingsDialog = SettingsDialog()
        self.settingsDialog.load_settings()
        self.remoteIP = ""
        self.remotePort = 0
        self.update_settings()
        self.controlsDialog = ControlsDialog(self)    
        self.controlsDialog.profileName = self.settingsDialog.settings["Control Profile"]    
        self.controlsDialog.load_control_profile(self.controlsDialog.profileName)

        self.manipulatorControlWindow = ManipulatorControlWindow()

        self.stabEnable = False        
        self.connected = False
        self.connectionTimeout = 0
        self.maxTimeout = 1000/TIMER_PERIOD_MS

        # ROV control data
        self.cControlFlags = np.uint64(0)
        self.cForwardThrust = 0.0
        self.cStrafeThrust = 0.0
        self.cVerticalThrust = 0.0
        self.cYawThrust = 0.0
        self.cRollInc = 0.0
        self.cPitchInc = 0.0
        self.cPowerTarget = 0.0
        self.cCamRotate = 0.0
        self.cManGrip = 0.0
        self.cManRotate = 0.0
        self.cRollPid = [0.0, 0.0, 0.0]     # kP,kI,kD
        self.cPitchPid = [0.0, 0.0, 0.0]
        self.cYawPid = [0.0, 0.0, 0.0]
        self.cDepthPid = [0.0, 0.0, 0.0]
        self.cflagMaster = False
        self.cflagResetIMU = False
        self.cflagResetStab = False
        self.cflagRollStab = False
        self.cflagPitchStab = False
        self.cflagYawStab = False
        self.cflagDepthStab = False
        self.cflagUpdatePID = False
        self.cflagLights = False
        self.cManFlags = [False, False, False, False]
        self.cManAngles = [0.0, 0.0, 0.0]
        self.cGripState = GripState.UWMANIPULATOR_GRIP_STOP

        # ROV telemetry data
        self.tErrorsFlags = np.uint64(0) 
        self.tRoll = 0.0
        self.tPitch = 0.0
        self.tYaw = 0.0
        self.tDepth = 0.0 
        self.tCharge = 0.0
        self.tVolts = 0.0
        self.tAmps = 0.0
        self.tRollSP = 0.0
        self.tPitchSP = 0.0
        self.tThrusterPhaseCurrent = [[0.0]*3]*6

        self.manTelemetryObtained = False
        self.manControl = False
        
        self.udp_thread = AsyncioThread(self.remoteIP, self.remotePort)
        self.udp_thread.start()
        
        self.setup_connections()

        self.controlTimer = QTimer()
        self.controlTimer.timeout.connect(self.sendControl)   
        self.controlTimer.start(TIMER_PERIOD_MS)
        self.masterChangeFlag = False
        self.lightsChangeFlag =False
        self.masterChangeCounter = 0
        self.lightsChangeCounter = 0
        self.firstTime = 0
        self.secondTime = 0

    def onSettingsClose(self):
        self.update_settings()
        
    def update_settings(self):        
        self.remoteIP = self.settingsDialog.settings["IP address"]
        self.remotePort = self.settingsDialog.settings["Port"]
    
    def telemetryUpdate(self):
        self.ui.rollVal.setText(str("%.2f"%self.udp_thread.udpServer.tRoll))
        self.ui.pitchVal.setText(str("%.2f"%self.udp_thread.udpServer.tPitch))
        self.ui.yawVal.setText(str("%.2f"%self.udp_thread.udpServer.tYaw))
        self.ui.depthVal.setText(str("%.2f"%self.udp_thread.udpServer.tDepth))
        self.ui.voltageVal.setText(str("%.2f"%self.udp_thread.udpServer.tVolts))
        self.ui.chargeVal.setText(str("%.2f"%self.udp_thread.udpServer.tCharge))
        self.ui.currentVal.setText(str("%.2f"%self.udp_thread.udpServer.tAmps))
        self.ui.rollSPVal.setText(str("%.2f"%self.udp_thread.udpServer.tRollSP))
        self.ui.pitchSPVal.setText(str("%.2f"%self.udp_thread.udpServer.tPitchSP))
        
        self.manTelemetryObtained = self.udp_thread.udpServer.manTelemetryObtained
        self.tThrusterPhaseCurrent = self.udp_thread.udpServer.tThrusterPhaseCurrent
        self.manipulatorControlWindow.manPhaseCurrents = self.udp_thread.udpServer.tManPhaseCurrents
        self.manipulatorControlWindow.tManAngles = self.udp_thread.udpServer.tManAngles
        self.manipulatorControlWindow.manVoltages = self.udp_thread.udpServer.tManVoltages
        self.manipulatorControlWindow.manTelemetryObtained = self.manTelemetryObtained
        self.manipulatorControlWindow.window_Update()

    def setup_connections(self):
        self.ui.settingsBut.clicked.connect(self.settings_button_click)
        self.ui.controlsBut.clicked.connect(self.controlsButtonClick)
        self.ui.connectButton.clicked.connect(self.connectionButtonClick)
        self.settingsDialog.finished.connect(self.onSettingsClose)
        self.controlsDialog.finished.connect(self.onControlsFinished)
        self.ui.masterButton.clicked.connect(self.onMasterSwitchClick)
        self.ui.positionResetBut.clicked.connect(self.resetPositionButtonClick)
        self.ui.manipulatorButton.clicked.connect(self.manipulatorNuttonClick)

    def closeEvent(self, event):
        self.manipulatorControlWindow.close()
        event.accept()

    def manipulatorNuttonClick(self):
        self.manipulatorControlWindow.show()
    
    def onControlsFinished(self):
        self.primaryIdx = -1
        self.secondaryIdx = -1
        self.primaryIdx = self.getJoystickIndex(self.controlsDialog.controlProfile["Primary Device"])
        self.secondaryIdx = self.getJoystickIndex(self.controlsDialog.controlProfile["Secondary Device"])
        if pygame.joystick.get_count() == 0:
            print("No joysticks available")
            return
        self.primaryJoystick = pygame.joystick.Joystick(self.primaryIdx)
        self.secondaryJoystick = pygame.joystick.Joystick(self.secondaryIdx)
        self.primaryJoystick.init()
        self.secondaryJoystick.init()
        pygame.event.pump()
        print("Joystick applied")

    def settings_button_click(self):
        self.settingsDialog.exec()
        
    def resetPositionButtonClick(self):
        self.cflagResetStab = True

    def connectionButtonClick(self):
        print('Connection attempt to: ' + self.remoteIP + ':' + str(self.remotePort)) 
        self.connectToRemote()
        self.connected = True
        self.controlTimer.start(TIMER_PERIOD_MS)

    def controlsButtonClick(self):
        self.controlsDialog.exec()
        
    def connectToRemote(self):
        startPacket = struct.pack("=BB", 0xAA, 0xFF)
        if self.udp_thread.isFinished:
            self.udp_thread.start()
        self.udp_thread.transport.sendto(startPacket, (self.remoteIP, self.remotePort))
        

    def joystickDeadzone(self, val, deadzone):
        if abs(val) <= deadzone:
            return 0
        if val > 0:
            dzval = (val - deadzone) * (1/(1-deadzone))
        else:
            dzval = (val + deadzone) * (1/(1-deadzone))
        return dzval

    def getJoystickIndex(self, joystickName):
        joystickIndex = -1        
        if not pygame.get_init():
            pygame.init()
        joyCount = pygame.joystick.get_count()
        if joyCount == 0:
            print("No joysticks found")
            return
        for i in range(joyCount):
            joystick = pygame.joystick.Joystick(i)
            if not joystick.get_init():
                joystick.init()
            joyAxes = joystick.get_numaxes()
            joyButtons = joystick.get_numbuttons()
            try:
                joyName = joystick.get_name()
            except Exception as ex:
                print(ex)
                print("There is problem with joystick")
            if joystickName == joyName:
                joystickIndex = i
                break
            joystick.quit()
        return joystickIndex

    def control3(self, primaryJoystick, secondaryJoystick, control, altControl1, altControl2):
        primaryValue = 0
        secondaryValue = 0        
        altVal1 = 0
        altVal2 = 0
        altSecondaryValue = 0
        altPrimaryValue = 0
        primaryInversion = False
        secondaryInversion = False
        mapping = self.controlsDialog.controlProfile[control]
        altMapping1 = self.controlsDialog.controlProfile[altControl1]
        altMapping2 = self.controlsDialog.controlProfile[altControl2]
        altPrimaryControl1 = altMapping1["Primary"]["Control"]
        altSecondaryControl1 = altMapping1["Secondary"]["Control"]
        altPrimaryControl2 = altMapping2["Primary"]["Control"]
        altSecondaryControl2 = altMapping2["Secondary"]["Control"]
        primaryControl = mapping["Primary"]["Control"]
        secondaryControl = mapping["Secondary"]["Control"]
        primaryInversion = mapping["Primary"]["Inverted"]
        secondaryInversion = mapping["Secondary"]["Inverted"]
        if primaryControl:
            primaryValue = self.getControlValue(primaryJoystick, primaryControl, primaryInversion)
        if secondaryControl:
            secondaryValue = self.getControlValue(secondaryJoystick, secondaryControl, secondaryInversion) if secondaryJoystick else 0
        if altPrimaryControl1 and altPrimaryControl2:
            altVal1 = self.getControlValue(primaryJoystick, altPrimaryControl1)
            altVal2 = self.getControlValue(primaryJoystick, altPrimaryControl2)
            altPrimaryValue = altVal1 - altVal2
        if altSecondaryControl1 and altSecondaryControl2:
            altVal1 = self.getControlValue(secondaryJoystick, altSecondaryControl1) if secondaryJoystick else 0
            altVal2 = self.getControlValue(secondaryJoystick, altSecondaryControl2) if secondaryJoystick else 0
            altSecondaryValue = altVal1 - altVal2

        primaryValue = self.joystickDeadzone(primaryValue, JOYSTICK_DEADZONE)
        secondaryValue = self.joystickDeadzone(secondaryValue, JOYSTICK_DEADZONE)
        controlValue = altSecondaryValue if altSecondaryValue else 0
        controlValue = altPrimaryValue if altPrimaryValue else controlValue
        controlValue = secondaryValue if secondaryValue else controlValue
        controlValue = primaryValue if primaryValue else controlValue
        return controlValue
    
    def buttonsControl2(self, primaryJoystick, secondaryJoystick, Control1, Control2):    
        Val1 = 0
        Val2 = 0
        SecondaryValue = 0
        PrimaryValue = 0
        Mapping1 = self.controlsDialog.controlProfile[Control1]
        Mapping2 = self.controlsDialog.controlProfile[Control2]
        PrimaryControl1 = Mapping1["Primary"]["Control"]
        SecondaryControl1 = Mapping1["Secondary"]["Control"]
        PrimaryControl2 = Mapping2["Primary"]["Control"]
        SecondaryControl2 = Mapping2["Secondary"]["Control"]
        if PrimaryControl1 and PrimaryControl2:
            Val1 = self.getControlValue(primaryJoystick, PrimaryControl1)
            Val2 = self.getControlValue(primaryJoystick, PrimaryControl2)
            PrimaryValue = Val1 - Val2
        if SecondaryControl1 and SecondaryControl2:
            Val1 = self.getControlValue(secondaryJoystick, SecondaryControl1) if secondaryJoystick else 0
            Val2 = self.getControlValue(secondaryJoystick, SecondaryControl2) if secondaryJoystick else 0
            SecondaryValue = Val1 - Val2
        controlValue = SecondaryValue if SecondaryValue else 0
        controlValue = PrimaryValue if PrimaryValue else controlValue
        return controlValue
    
    def triggersControlToOneVal(self, joystick, control):
        # ONLY FOR JOYSTICKS WITH TRIGGERS 
        secondaryValue = 0
        primaryValue = 0
        resultValue = 0 
        primaryInversion = False
        secondaryInversion = False
        mapping = self.controlsDialog.controlProfile[control]
        PrimaryControl = mapping["Primary"]["Control"]
        SecondaryControl = mapping["Secondary"]["Control"]        
        primaryInversion = mapping["Primary"]["Inverted"]
        secondaryInversion = mapping["Secondary"]["Inverted"]
        if control:
            secondaryValue = self.getControlValue(joystick, SecondaryControl, secondaryInversion)
            primaryValue = self.getControlValue(joystick, PrimaryControl, primaryInversion)        
        resultValue = primaryValue - secondaryValue
        return resultValue/2
    
    def getJoystickControl(self): 
             
        if not pygame.get_init():
            pygame.init()
            pygame.joystick.init()
        
        pygame.event.pump()
        controlProfile = self.controlsDialog.controlProfile
        primaryJoystickName = controlProfile["Primary Device"]
        secondaryJoystickName = controlProfile["Secondary Device"]
        if primaryJoystickName == "Keyboard":
            print("Keyboard input is not supported for now")
            return
        if secondaryJoystickName == "Keyboard":
            print("Keyboard (Secondary) input is not supported for now")
        if self.primaryIdx == -1:
            self.primaryIdx = self.getJoystickIndex(primaryJoystickName)
        if self.secondaryIdx == -1:
            self.secondaryIdx = self.getJoystickIndex(secondaryJoystickName)
        
        self.firstTime = time.time()  
        if self.primaryIdx == -1:
            print("Primary joystick not found")
            return
        if not pygame.joystick.get_init():
            return
        else:
            if self.primaryJoystick:
                if not self.primaryJoystick.get_init():
                    self.primaryJoystick.init()
                curPrimaryJoyName = self.primaryJoystick.get_name()
                if not (curPrimaryJoyName == primaryJoystickName):
                    self.primaryJoystick = pygame.joystick.Joystick(self.primaryIdx)
            else:
                if self.primaryIdx is not None:
                    self.primaryJoystick = pygame.joystick.Joystick(self.primaryIdx)
                else:
                    return
        if self.secondaryIdx == -1:
            print("Secondary joystick not found")
        else:
            if self.secondaryJoystick:
                if not self.secondaryJoystick.get_init():
                    self.secondaryJoystick.init()
                if not (self.secondaryJoystick.get_name() == secondaryJoystickName):
                    self.secondaryJoystick = pygame.joystick.Joystick(self.secondaryIdx)
            else: 
                self.secondaryJoystick = pygame.joystick.Joystick(self.secondaryIdx)
        self.secondTime = time.time()
        if not self.primaryJoystick.get_init():
            self.primaryJoystick.init()
        if not self.secondaryJoystick.get_init():
            self.secondaryJoystick.init()
        
        # Forward thrust
        self.cForwardThrust = self.control3(self.primaryJoystick, self.secondaryJoystick,
                                            "Forward", "Move forward", "Move backwards")
        # Strafe thrust
        self.cStrafeThrust = self.control3(self.primaryJoystick, self.secondaryJoystick,
                                            "Strafe", "Move right", "Move left")
        # Vertical thrust
        self.cVerticalThrust = self.control3(self.primaryJoystick, self.secondaryJoystick,
                                            "Vertical", "Move up", "Move down")
        # Yaw thrust
        self.cYawThrust = self.control3(self.primaryJoystick, self.secondaryJoystick,
                                            "Yaw", "Rotate right", "Rotate left")
        # Roll thrust (increment)
        self.cRollInc = self.control3(self.primaryJoystick, self.secondaryJoystick,
                                            "Roll", "Roll increment", "Roll decrement") * 3
        # Pitch thrust (increment)
        self.cPitchInc = self.control3(self.primaryJoystick, self.secondaryJoystick,
                                            "Pitch", "Pitch increment", "Pitch decrement") * 3
        # Camera rotate
        self.cCamRotate = self.control3(self.primaryJoystick, self.secondaryJoystick,
                                            "Camera angle","Camera rotate up", "Camera rotate down")
        # Manipulator rotate
        if ((primaryJoystickName == secondaryJoystickName) 
            and ((primaryJoystickName.lower().find("xbox") >= 0) 
            or (primaryJoystickName.lower().find("dualsense") >= 0) 
            or (primaryJoystickName.lower().find("dualshock") >= 0))
            and controlProfile["Manipulator rotate"]["Primary"]["Control"]
            and controlProfile["Manipulator rotate"]["Secondary"]["Control"]):
            self.cManRotate = self.triggersControlToOneVal(self.primaryJoystick, "Manipulator rotate")
        else:
            self.cManRotate = self.control3(self.primaryJoystick, self.secondaryJoystick,
                                            "Manipulator rotate", "Manipulator rotate right", "Manipulator rotate left")
        # Manipulator grip
        if ((primaryJoystickName == secondaryJoystickName) 
            and ((primaryJoystickName.lower().find("xbox") >= 0) 
            or (primaryJoystickName.lower().find("dualsense") >= 0) 
            or (primaryJoystickName.lower().find("dualshock") >= 0))
            and controlProfile["Manipulator grip"]["Primary"]["Control"]
            and controlProfile["Manipulator grip"]["Secondary"]["Control"]):
            self.cManGrip = self.triggersControlToOneVal(self.primaryJoystick, "Manipulator grip")
        else:
            self.cManGrip = self.control3(self.primaryJoystick, self.secondaryJoystick,
                                            "Manipulator grip", "Manipulator grip close", "Manipulator grip open")
        # Lights toggle        
        if self.getControlValue(self.secondaryJoystick,controlProfile["Lights"]["Secondary"]["Control"]) or self.getControlValue(self.primaryJoystick,controlProfile["Lights"]["Primary"]["Control"]):
            if not self.lightsChangeFlag:
                self.cflagLights = not self.cflagLights
                self.lightsChangeFlag = True
        else:
            self.lightsChangeFlag = False
        # Reset positiom
        self.cflagResetStab = self.getControlValue(self.primaryJoystick, controlProfile["Reset position"]["Secondary"]["Control"]) or self.getControlValue(self.secondaryJoystick, controlProfile["Reset position"]["Primary"]["Control"])
        # Master        
        if self.getControlValue(self.secondaryJoystick, controlProfile["Master"]["Secondary"]["Control"]) or self.getControlValue(self.primaryJoystick, controlProfile["Master"]["Primary"]["Control"]):
            if not self.masterChangeFlag:
                self.cflagMaster = not self.cflagMaster
                self.masterChangeFlag = True
        else:
            self.masterChangeFlag = False

    def getControlValue(self, Joystick, Control, Inversion = False):        
        Value = 0
        if not Control:
            return 0
        ControlType, ControlIdx = Control.split(" ", 1)
        if not ControlType == "Dpad":
            ControlIdx = int(ControlIdx)
        #pygame.event.pump()
        if ControlType == "Axis":
            if ControlIdx < Joystick.get_numaxes():
                Value = Joystick.get_axis(ControlIdx)
        if ControlType == "Button":
            if ControlIdx < Joystick.get_numbuttons():
                Value = Joystick.get_button(ControlIdx)
        if ControlType == "Dpad":
            DpadValues = ControlIdx.split(";")
            DpadValues[0] = int(DpadValues[0])
            DpadValues[1] = int(DpadValues[1])
            hatValues = Joystick.get_hat(0)
            Value = 1 if (hatValues[0] == DpadValues[0]) and (hatValues[1] == DpadValues[1]) else 0
        if Inversion: 
            Value *= -1
        return Value                 

    def gatherControl(self):        
        self.getJoystickControl()        
        #print(self.secondTime-self.firstTime)
        self.updateMasterStatus()
        self.cflagResetIMU = self.settingsDialog.resetIMU
        self.cflagUpdatePID = self.settingsDialog.updatePID
        self.cRollPid = [self.settingsDialog.settings["PID"]["Roll"]["kP"],
                         self.settingsDialog.settings["PID"]["Roll"]["kI"],
                         self.settingsDialog.settings["PID"]["Roll"]["kD"]]
        self.cPitchPid = [self.settingsDialog.settings["PID"]["Pitch"]["kP"],
                          self.settingsDialog.settings["PID"]["Pitch"]["kI"],
                          self.settingsDialog.settings["PID"]["Pitch"]["kD"]]
        self.cYawPid = [self.settingsDialog.settings["PID"]["Yaw"]["kP"],
                        self.settingsDialog.settings["PID"]["Yaw"]["kI"],
                        self.settingsDialog.settings["PID"]["Yaw"]["kD"]]
        self.cDepthPid = [self.settingsDialog.settings["PID"]["Depth"]["kP"],
                          self.settingsDialog.settings["PID"]["Depth"]["kI"],
                          self.settingsDialog.settings["PID"]["Depth"]["kD"]]
        self.stabEnable = self.ui.stabOn.isChecked()
        if self.stabEnable:
            self.cflagRollStab  = self.ui.rollStabOn.isChecked()
            self.cflagPitchStab = self.ui.pitchStabOn.isChecked()
            self.cflagYawStab   = self.ui.yawStabOn.isChecked()
            self.cflagDepthStab = self.ui.depthStabOn.isChecked()
        else:
            self.cflagRollStab  = False
            self.cflagPitchStab = False
            self.cflagYawStab   = False
            self.cflagDepthStab = False
        self.cPowerTarget = self.ui.powerTargetVal.value()
        self.cManFlags = self.manipulatorControlWindow.manFlags
        self.cManAngles = self.manipulatorControlWindow.manAngles
        self.cGripState = self.manipulatorControlWindow.gripState
        self.manControl = self.manipulatorControlWindow.manControlEnabled

    def onMasterSwitchClick(self):
        self.cflagMaster = not self.cflagMaster
        self.updateMasterStatus()

    def updateMasterStatus(self):
        if self.cflagMaster:
            self.ui.masterStatus.setText("ARMED")
            self.ui.masterStatus.setStyleSheet("color:red;")
        else:
            self.ui.masterStatus.setText("SAFE")
            self.ui.masterStatus.setStyleSheet("color:green;")

    def sendControl(self):
        currentTime = time.time()
        if abs(currentTime - self.udp_thread.udpServer.lastTelemetryTime) > 2:
            self.connected = False
           # self.controlTimer.stop()
        else:
            self.connected = True
        self.updateOnlineStatus()
        if not self.connected:
            return
        # controlFlags, forward, strafe, vertical, rotation, rollInc, pitchInc, powerTarget, cameraRotate, manipulatorGrip, manipulatorRotate, rollKp, rollKi, rollKd, pitchKp, pitchKi, pitchKd, yawKp, yawKi, yawKd, depthKp, depthKi, depthKd
        # flags = MASTER, lightState, stabRoll, stabPitch, stabYaw, stabDepth, resetPosition, resetIMU, updatePID
        self.gatherControl()
        self.cControlFlags = self.cControlFlags | UDP_FLAGS_MASTERx         if self.cflagMaster     else self.cControlFlags & ~UDP_FLAGS_MASTERx
        self.cControlFlags = self.cControlFlags | UDP_FLAGS_LIGHT_STATEx    if self.cflagLights     else self.cControlFlags & ~UDP_FLAGS_LIGHT_STATEx 
        self.cControlFlags = self.cControlFlags | UDP_FLAGS_STAB_ROLLx      if self.cflagRollStab   else self.cControlFlags & ~UDP_FLAGS_STAB_ROLLx 
        self.cControlFlags = self.cControlFlags | UDP_FLAGS_STAB_PITCHx     if self.cflagPitchStab  else self.cControlFlags & ~UDP_FLAGS_STAB_PITCHx 
        self.cControlFlags = self.cControlFlags | UDP_FLAGS_STAB_YAWx       if self.cflagYawStab    else self.cControlFlags & ~UDP_FLAGS_STAB_YAWx 
        self.cControlFlags = self.cControlFlags | UDP_FLAGS_STAB_DEPTHx     if self.cflagDepthStab  else self.cControlFlags & ~UDP_FLAGS_STAB_DEPTHx 
        self.cControlFlags = self.cControlFlags | UDP_FLAGS_RESET_POSITIONx if self.cflagResetStab  else self.cControlFlags & ~UDP_FLAGS_RESET_POSITIONx 
        self.cControlFlags = self.cControlFlags | UDP_FLAGS_RESET_IMUx      if self.cflagResetIMU   else self.cControlFlags & ~UDP_FLAGS_RESET_IMUx           
        self.cControlFlags = self.cControlFlags | UDP_FLAGS_UPDATE_PIDx     if self.cflagUpdatePID  else self.cControlFlags & ~UDP_FLAGS_UPDATE_PIDx
        self.cControlFlags = self.cControlFlags | UDP_FLAGS_MANIPULATOR_ANGLE_1_UPDATE if self.cManFlags[0] else self.cControlFlags & ~UDP_FLAGS_MANIPULATOR_ANGLE_1_UPDATE
        self.cControlFlags = self.cControlFlags | UDP_FLAGS_MANIPULATOR_ANGLE_2_UPDATE if self.cManFlags[1] else self.cControlFlags & ~UDP_FLAGS_MANIPULATOR_ANGLE_2_UPDATE
        self.cControlFlags = self.cControlFlags | UDP_FLAGS_MANIPULATOR_ANGLE_3_UPDATE if self.cManFlags[2] else self.cControlFlags & ~UDP_FLAGS_MANIPULATOR_ANGLE_3_UPDATE
        self.cControlFlags = self.cControlFlags | UDP_FLAGS_MANIPULATOR_GRIP_UPDATE    if self.cManFlags[3] else self.cControlFlags & ~UDP_FLAGS_MANIPULATOR_GRIP_UPDATE   
        if not self.manControl:
            controlPacket = struct.pack("=Qffffffffffffffffffffff", 
                                        self.cControlFlags, self.cForwardThrust,
                                        self.cStrafeThrust, self.cVerticalThrust,
                                        self.cYawThrust, self.cRollInc,
                                        self.cPitchInc, self.cPowerTarget,
                                        self.cCamRotate, self.cManGrip,
                                        self.cManRotate,
                                        self.cRollPid[0], self.cRollPid[1], self.cRollPid[2],
                                        self.cPitchPid[0], self.cPitchPid[1], self.cPitchPid[2],
                                        self.cYawPid[0], self.cYawPid[1], self.cYawPid[2],
                                        self.cDepthPid[0], self.cDepthPid[1], self.cDepthPid[2],)
        else:
            # controlFlags, forward, strafe, vertical, rotation, rollInc, pitchInc, powerTarget, cameraRotate, manipulatorGrip, 
            # manipulatorRotate, rollKp, rollKi, rollKd, pitchKp, pitchKi, pitchKd, yawKp, yawKi, yawKd, depthKp, depthKi, depthKd,
            # Extended packet:
            # manipulatorAngle1, manipulatorAngle2, manipulatorAngle3, manipulatorGrip
            # flags = MASTER, lightState, stabRoll, stabPitch, stabYaw, stabDepth, resetPosition, resetIMU, updatePID, 
            # Extended packet:
            # manipulatorAngleUpdate1, manipulatorAngleUpdate2, manipulatorAngleUpdate3, manipulatorGripUpdate
            controlPacket = struct.pack("=QfffffffffffffffffffffffffB", 
                                        self.cControlFlags, self.cForwardThrust,
                                        self.cStrafeThrust, self.cVerticalThrust,
                                        self.cYawThrust, self.cRollInc,
                                        self.cPitchInc, self.cPowerTarget,
                                        self.cCamRotate, self.cManGrip,
                                        self.cManRotate,
                                        self.cRollPid[0], self.cRollPid[1], self.cRollPid[2],
                                        self.cPitchPid[0], self.cPitchPid[1], self.cPitchPid[2],
                                        self.cYawPid[0], self.cYawPid[1], self.cYawPid[2],
                                        self.cDepthPid[0], self.cDepthPid[1], self.cDepthPid[2],
                                        self.cManAngles[0], self.cManAngles[1], self.cManAngles[2], self.cGripState)
        #print(*["%.2f" % elem for elem in struct.unpack_from("=Qffffffffffffffffffffff",controlPacket)], sep ='; ')
        try:
            self.udp_thread.transport.sendto(controlPacket, (self.remoteIP, self.remotePort))
        except Exception as ex:
            print(ex)
        self.telemetryUpdate()

        for i in range(4):
            if self.cManFlags[i]:
                self.cManFlags[i] = False
                self.manipulatorControlWindow.manFlags[i] = False

        if self.cflagResetIMU:
            self.cflagResetIMU = False
            self.settingsDialog.resetIMU = False
            print("IMU values reseted at Roll: %5.1f, Pitch: %5.1f, Yaw: %5.1f" % (self.tRoll, self.tPitch, self.tYaw)) 

        if self.cflagUpdatePID:
            self.cflagUpdatePID = False
            self.settingsDialog.updatePID = False
            print("New PID constants has been sent") 
            print(self.settingsDialog.settings["PID"])

        if self.cflagResetStab:
            self.cflagResetStab = False
            #print("All stabibilizations and setpoints has been reset")
        
    def updateOnlineStatus(self):
        if self.connected:
            self.ui.onlineStatus.setText("ONLINE")
            self.ui.onlineStatus.setStyleSheet("color:green;")
        else:
            self.ui.onlineStatus.setText("OFFLINE")
            self.ui.onlineStatus.setStyleSheet("color:red;")
            self.manTelemetryObtained = False
            self.udp_thread.udpServer.manTelemetryObtained = False
            self.manipulatorControlWindow.manTelemetryObtained = False
            self.manipulatorControlWindow.window_Update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())