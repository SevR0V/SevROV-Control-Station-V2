import sys, pygame
import struct
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from AsyncioThread import AsyncioThread
from SettingsDialog import SettingsDialog
from ControlsDialog import ControlsDialog
from UI.main_window import Ui_MainWindow
import numpy as np
# controlFlags, forward, strafe, vertical, rotation, rollInc, pitchInc, powerTarget, cameraRotate, manipulatorGrip, manipulatorRotate, rollKp, rollKi, rollKd, pitchKp, pitchKi, pitchKd, yawKp, yawKi, yawKd, depthKp, depthKi, depthKd
# flags = MASTER, lightState, stabRoll, stabPitch, stabYaw, stabDepth, resetPosition, resetIMU, updatePID

#ERRORFLAGS, roll, pitch, yaw, depth, batVoltage, batCharge, batCurrent, rollSP, pitchSP

UDP_FLAGS_MASTERx = np.uint64(1 << 0)
UDP_FLAGS_LIGHT_STATEx = np.uint64(1 << 1)
UDP_FLAGS_STAB_ROLLx = np.uint64(1 << 2)
UDP_FLAGS_STAB_PITCHx = np.uint64(1 << 3)
UDP_FLAGS_STAB_YAWx = np.uint64(1 << 4)
UDP_FLAGS_STAB_DEPTHx = np.uint64(1 << 5)
UDP_FLAGS_RESET_POSITIONx = np.uint64(1 << 6)
UDP_FLAGS_RESET_IMUx = np.uint64(1 << 7)
UDP_FLAGS_UPDATE_PIDx = np.uint64(1 << 8)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.pyg = pygame
        self.joystick = self.pyg.joystick
        self.pyg.init()
        self.joystick.init()

        self.controlsDialog = ControlsDialog(self.pyg, self.joystick)
        self.settingsDialog = SettingsDialog() 

        self.stabEnable = False
        self.remoteIP = ""
        self.remotePort = 0
        self.connected = False

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
        
        self.udp_thread = AsyncioThread(self.remoteIP, self.remotePort)
        self.udp_thread.start()
        
        self.setup_connections() 
        self.settingsDialog.load_settings()
        self.updateSettings()

        self.controlTimer = QTimer()
        self.controlTimer.timeout.connect(self.sendControl)   
        self.controlTimer.start(2000)

    def onSettingsClose(self):
        print('set cls')
        self.updateSettings()
        
    def updateSettings(self):        
        self.remoteIP = self.settingsDialog.settings["IP address"]
        self.remotePort = self.settingsDialog.settings["Port"]
    
    def telemetryUpdate(self):
        self.ui.rollVal.setText(str(self.udp_thread.udpServer.tRoll))
        self.ui.pitchVal.setText(str(self.udp_thread.udpServer.tPitch))
        self.ui.yawVal.setText(str(self.udp_thread.udpServer.tYaw))
        self.ui.depthVal.setText(str(self.udp_thread.udpServer.tDepth))
        self.ui.voltageVal.setText(str(self.udp_thread.udpServer.tVolts))
        self.ui.chargeVal.setText(str(self.udp_thread.udpServer.tCharge))
        self.ui.currentVal.setText(str(self.udp_thread.udpServer.tAmps))
        self.ui.rollSPVal.setText(str(self.udp_thread.udpServer.tRollSP))
        self.ui.pitchSPVal.setText(str(self.udp_thread.udpServer.tPitchSP))

    def setup_connections(self):
        self.ui.settingsBut.clicked.connect(self.settings_button_click)
        self.ui.controlsBut.clicked.connect(self.controlsButtonClick)
        self.ui.connectButton.clicked.connect(self.connectionButtonClick)
        self.settingsDialog.finished.connect(self.onSettingsClose)

    def settings_button_click(self):
        self.settingsDialog.exec()
        
    def resetPositionButtonClick(self):
        self.cflagResetStab = True

    def connectionButtonClick(self):
        print('Connection attempt to: ' + self.remoteIP + ':' + str(self.remotePort)) 
        self.connectToRemote()
        self.connected = True

    def controlsButtonClick(self):        
        self.controlsDialog.updateControlsMapWindow()
        self.controlsDialog.exec()
        
    def connectToRemote(self):
        startPacket = struct.pack("=BB", 0xAA, 0xFF)
        self.udp_thread.transport.sendto(startPacket, (self.remoteIP, self.remotePort))

    def gatherControl(self):
        self.cflagResetIMU = self.settingsDialog.resetIMU
        self.cflagUpdatePID = self.settingsDialog.updatePID
        self.cRollPid = [self.settings["PID"]["Roll"]["kP"],
                         self.settings["PID"]["Roll"]["kI"],
                         self.settings["PID"]["Roll"]["kD"]]
        self.cPitchPid = [self.settings["PID"]["Pitch"]["kP"],
                          self.settings["PID"]["Pitch"]["kI"],
                          self.settings["PID"]["Pitch"]["kD"]]
        self.cYawPid = [self.settings["PID"]["Yaw"]["kP"],
                        self.settings["PID"]["Yaw"]["kI"],
                        self.settings["PID"]["Yaw"]["kD"]]
        self.cDepthPid = [self.settings["PID"]["Depth"]["kP"],
                          self.settings["PID"]["Depth"]["kI"],
                          self.settings["PID"]["Depth"]["kD"]]
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

    def sendControl(self):
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
             
        controlPacket = struct.pack("=Qffffffffffffffffffffff", 
                                    self.cControlFlags,
                                    self.cForwardThrust,
                                    self.cStrafeThrust,
                                    self.cVerticalThrust,
                                    self.cYawThrust,
                                    self.cRollInc,
                                    self.cPitchInc,
                                    self.cPowerTarget,
                                    self.cCamRotate,
                                    self.cManGrip,
                                    self.cManRotate,
                                    self.cRollPid[0],
                                    self.cRollPid[1],
                                    self.cRollPid[2],
                                    self.cPitchPid[0],
                                    self.cPitchPid[1],
                                    self.cPitchPid[2],
                                    self.cYawPid[0],
                                    self.cYawPid[1],
                                    self.cYawPid[2],
                                    self.cDepthPid[0],
                                    self.cDepthPid[1],
                                    self.cDepthPid[2],)

        self.udp_thread.transport.sendto(controlPacket, (self.remoteIP, self.remotePort))
        self.telemetryUpdate()

        if self.cflagResetIMU:
            self.cflagResetIMU = False
            self.settingsDialog.resetIMU = False
            print("IMU values reseted at Roll: %5.1f, Pitch: %5.1f, Yaw: %5.1f" % (self.tRoll, self.tPitch, self.tYaw)) 

        if self.cflagUpdatePID:
            self.cflagUpdatePID = False
            self.settingsDialog.updatePID = False
            print("New PID constants has been sent") 
            print(self.settings["PID"])

        if self.cflagResetStab:
            self.cflagResetStab = False
            print("All stabibilizations and setpoints has been reset") 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())