import sys
import pygame as pg
import time
import struct
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from AsyncioThread import AsyncioThread  # возможно, лучше как AsyncThread
from SettingsDialog import SettingsDialog  # возможно, лучше как SettingsDlg
from ControlsDialog import ControlsDialog  # возможно, ControlsDlg
from UI.main_window import Ui_MainWindow
from ManipulatorControlWindow import ManipulatorControlWindow  # возможно, ManipulatorCtrl

# Константы
JOYSTICK_DEADZONE = 0.03
TIMER_PERIOD_MS = 50

# Флаги для управления
UDP_FLAGS = {
    'MASTER': np.uint64(1 << 0),
    'LIGHT_STATE': np.uint64(1 << 1),
    'STAB_ROLL': np.uint64(1 << 2),
    'STAB_PITCH': np.uint64(1 << 3),
    'STAB_YAW': np.uint64(1 << 4),
    'STAB_DEPTH': np.uint64(1 << 5),
    'RESET_POSITION': np.uint64(1 << 6),
    'RESET_IMU': np.uint64(1 << 7),
    'UPDATE_PID': np.uint64(1 << 8)
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Настройка интерфейса и статусов
        self.ui.masterStatus.setStyleSheet("color:green;")
        self.ui.onlineStatus.setStyleSheet("color:red;")
        self.primaryIdx = self.secondaryIdx = -1
        
        # Инициализация модулей
        pg.init()
        pg.joystick.init()
        self.primaryJoystick = self.secondaryJoystick = None
        
        # Инициализация диалогов и окон
        self.settingsDialog = SettingsDialog()
        self.settingsDialog.load_settings()
        self.remoteIP, self.remotePort = "", 0
        self.controlsDialog = ControlsDialog(self)
        self.controlsDialog.profileName = self.settingsDialog.settings["Control Profile"]
        self.controlsDialog.load_control_profile(self.controlsDialog.profileName)
        self.manipulatorControlWindow = ManipulatorControlWindow()
        
        # Таймеры и флаги
        self.controlTimer = QTimer()
        self.controlTimer.timeout.connect(self.sendControl)
        self.controlTimer.start(TIMER_PERIOD_MS)
        self.masterChangeFlag = self.lightsChangeFlag = False
        
        # Настройка UDP
        self.udp_thread = AsyncioThread(self.remoteIP, self.remotePort)
        self.udp_thread.start()
        
        # Установка соединений
        self.setup_connections()
        self.reset_flags()
        self.init_control_values()

    def setup_connections(self):
        self.ui.settingsBut.clicked.connect(self.show_settings_dialog)
        self.ui.controlsBut.clicked.connect(self.show_controls_dialog)
        self.ui.connectButton.clicked.connect(self.connect_to_remote)
        self.settingsDialog.finished.connect(self.update_settings)
        #self.controlsDialog.finished.connect(self.apply_control_settings)
        self.ui.masterButton.clicked.connect(self.toggle_master_status)
        #self.ui.positionResetBut.clicked.connect(self.reset_position)
        self.ui.manipulatorButton.clicked.connect(self.show_manipulator_control)

    def show_settings_dialog(self):
        self.settingsDialog.exec()
    
    def show_controls_dialog(self):
        self.controlsDialog.exec()

    def show_manipulator_control(self):
        self.manipulatorControlWindow.show()

    def connect_to_remote(self):
        print(f'Connecting to: {self.remoteIP}:{self.remotePort}')
        if self.udp_thread.isFinished:
            self.udp_thread.start()
        self.controlTimer.start(TIMER_PERIOD_MS)
    
    def reset_flags(self):
        """ Сброс флагов стабилизации """
        self.cflagMaster = self.cflagResetIMU = False
        self.cflagLights = self.cflagRollStab = False
        self.cflagPitchStab = self.cflagYawStab = False
        self.cflagDepthStab = self.cflagUpdatePID = False
    
    def init_control_values(self):
        """ Инициализация начальных значений управления """
        self.cControlFlags = np.uint64(0)
        self.cForwardThrust = self.cStrafeThrust = self.cVerticalThrust = 0.0
        self.cYawThrust = self.cRollInc = self.cPitchInc = 0.0
        self.cPowerTarget = self.cCamRotate = 0.0
        self.cManGrip = self.cManRotate = 0.0
        self.cRollPid = [0.0, 0.0, 0.0]
        self.cPitchPid = [0.0, 0.0, 0.0]
        self.cYawPid = [0.0, 0.0, 0.0]
        self.cDepthPid = [0.0, 0.0, 0.0]
        
    def update_settings(self):
        self.remoteIP = self.settingsDialog.settings["IP address"]
        self.remotePort = self.settingsDialog.settings["Port"]

    def sendControl(self):
        """Отправка пакета управления на удалённое устройство"""
        self.gather_control_data()
        self.update_flags()
        controlPacket = struct.pack(
            "=Qffffffffffffffffffffff",
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
            *self.cRollPid, *self.cPitchPid,
            *self.cYawPid, *self.cDepthPid
        )
        try:
            self.udp_thread.transport.sendto(controlPacket, (self.remoteIP, self.remotePort))
        except Exception as ex:
            print(f"Error sending control packet: {ex}")
        self.update_ui_status()

    def gather_control_data(self):
        """Сбор данных управления"""
        self.getJoystickControl()
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
        self.cflagRollStab = self.ui.rollStabOn.isChecked() if self.stabEnable else False
        self.cflagPitchStab = self.ui.pitchStabOn.isChecked() if self.stabEnable else False
        self.cflagYawStab = self.ui.yawStabOn.isChecked() if self.stabEnable else False
        self.cflagDepthStab = self.ui.depthStabOn.isChecked() if self.stabEnable else False
        self.cPowerTarget = self.ui.powerTargetVal.value()

    def update_flags(self):
        """Обновление флагов управления"""
        self.cControlFlags = 0
        self.cControlFlags |= UDP_FLAGS['MASTER'] if self.cflagMaster else 0
        self.cControlFlags |= UDP_FLAGS['LIGHT_STATE'] if self.cflagLights else 0
        self.cControlFlags |= UDP_FLAGS['STAB_ROLL'] if self.cflagRollStab else 0
        self.cControlFlags |= UDP_FLAGS['STAB_PITCH'] if self.cflagPitchStab else 0
        self.cControlFlags |= UDP_FLAGS['STAB_YAW'] if self.cflagYawStab else 0
        self.cControlFlags |= UDP_FLAGS['STAB_DEPTH'] if self.cflagDepthStab else 0
        self.cControlFlags |= UDP_FLAGS['RESET_POSITION'] if self.cflagResetIMU else 0
        self.cControlFlags |= UDP_FLAGS['UPDATE_PID'] if self.cflagUpdatePID else 0

    def update_ui_status(self):
        """Обновление статуса подключения на интерфейсе"""
        is_connected = time.time() - self.udp_thread.udpServer.lastTelemetryTime < 2
        self.ui.onlineStatus.setText("ONLINE" if is_connected else "OFFLINE")
        self.ui.onlineStatus.setStyleSheet("color:green;" if is_connected else "color:red;")

    def getJoystickControl(self): 
        """ Получение значений с контроллера """
        if not pg.get_init():
            pg.init()
            pg.joystick.init()
        
        pg.event.pump()
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
        
        if self.primaryIdx == -1:
            print("Primary joystick not found")
            return
        if not pg.joystick.get_init():
            return
        else:
            if self.primaryJoystick:
                if not (self.primaryJoystick.get_name == primaryJoystickName):
                    self.primaryJoystick = pg.joystick.Joystick(self.primaryIdx)
            else:
                self.primaryJoystick = pg.joystick.Joystick(self.primaryIdx)
        if self.secondaryIdx == -1:
            print("Secondary joystick not found")
        else:
            if self.secondaryJoystick:
                if not (self.secondaryJoystick.get_name == secondaryJoystickName):
                    self.secondaryJoystick = pg.joystick.Joystick(self.secondaryIdx)
            else: 
                self.secondaryJoystick = pg.joystick.Joystick(self.secondaryIdx)

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
                                            "Roll", "Roll increment", "Roll decrement")
        # Pitch thrust (increment)
        self.cPitchInc = self.control3(self.primaryJoystick, self.secondaryJoystick,
                                            "Pitch", "Pitch increment", "Pitch decrement")
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
        if self.getControlValue(self.secondaryJoystick, controlProfile["Lights"]["Secondary"]["Control"]) or self.getControlValue(self.primaryJoystick, controlProfile["Lights"]["Primary"]["Control"]):
            if not self.lightsChangeFlag:
                self.cflagLights = not self.cflagLights
                self.lightsChangeFlag = True
        else:
            self.lightsChangeFlag = False

        # Reset position
        self.cflagResetIMU = self.getControlValue(self.primaryJoystick, controlProfile["Reset position"]["Secondary"]["Control"]) or self.getControlValue(self.secondaryJoystick, controlProfile["Reset position"]["Primary"]["Control"])

        # Master
        if self.getControlValue(self.secondaryJoystick, controlProfile["Master"]["Secondary"]["Control"]) or self.getControlValue(self.primaryJoystick, controlProfile["Master"]["Primary"]["Control"]):
            if not self.masterChangeFlag:
                self.cflagMaster = not self.cflagMaster
                self.masterChangeFlag = True
        else:
            self.masterChangeFlag = False

    def getJoystickIndex(self, joystickName):
        joystickIndex = -1
        if not pg.get_init():
            pg.init()
        for i in range(pg.joystick.get_count()):
            joystick = pg.joystick.Joystick(i)
            joystick.init()
            if joystickName == joystick.get_name():
                joystickIndex = i
                break
            joystick.quit()
        return joystickIndex

    def control3(self, primaryJoystick, secondaryJoystick, control, altControl1, altControl2):
        """ Логика управления с учетом альтернативных элементов управления """
        primaryValue = 0
        secondaryValue = 0        
        altVal1 = 0
        altVal2 = 0
        altSecondaryValue = 0
        altPrimaryValue = 0
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

    def joystickDeadzone(self, val, deadzone):
        if abs(val) <= deadzone:
            return 0
        if val > 0:
            dzval = (val - deadzone) * (1 / (1 - deadzone))
        else:
            dzval = (val + deadzone) * (1 / (1 - deadzone))
        return dzval

    def getControlValue(self, Joystick, Control, Inversion=False):        
        Value = 0
        if not Control:
            return 0
        ControlType, ControlIdx = Control.split(" ", 1)
        if ControlType != "Dpad":
            ControlIdx = int(ControlIdx)
        if ControlType == "Axis":
            if ControlIdx < Joystick.get_numaxes():
                Value = Joystick.get_axis(ControlIdx)
        if ControlType == "Button":
            if ControlIdx < Joystick.get_numbuttons():
                Value = Joystick.get_button(ControlIdx)
        if ControlType == "Dpad":
            DpadValues = list(map(int, ControlIdx.split(";")))
            hatValues = Joystick.get_hat(0)
            Value = 1 if (hatValues[0] == DpadValues[0]) and (hatValues[1] == DpadValues[1]) else 0
        return -Value if Inversion else Value

    def triggersControlToOneVal(self, joystick, control):
        """ Логика объединения триггеров в одно значение """
        mapping = self.controlsDialog.controlProfile[control]
        PrimaryControl = mapping["Primary"]["Control"]
        SecondaryControl = mapping["Secondary"]["Control"]
        primaryInversion = mapping["Primary"]["Inverted"]
        secondaryInversion = mapping["Secondary"]["Inverted"]
        primaryValue = self.getControlValue(joystick, PrimaryControl, primaryInversion) if PrimaryControl else 0
        secondaryValue = self.getControlValue(joystick, SecondaryControl, secondaryInversion) if SecondaryControl else 0
        return primaryValue - secondaryValue

    def toggle_master_status(self):
        self.cflagMaster = not self.cflagMaster
        self.update_master_status()

    def update_master_status(self):
        if self.cflagMaster:
            self.ui.masterStatus.setText("ARMED")
            self.ui.masterStatus.setStyleSheet("color:red;")
        else:
            self.ui.masterStatus.setText("SAFE")
            self.ui.masterStatus.setStyleSheet("color:green;")

# Главный запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
