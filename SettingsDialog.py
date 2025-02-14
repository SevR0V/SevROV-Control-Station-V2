from UI.settings_window import Ui_settingsDialog
import json, os
from PySide6.QtWidgets import QDialog

defaultSettings = {
                "IP address": "192.168.0.1",
                "Port": 1337,
                "PID": {
                    "Roll": {"kP": 0.0, "kI": 0.0, "kD": 0.0},
                    "Pitch": {"kP": 0.0, "kI": 0.0, "kD": 0.0},
                    "Yaw": {"kP": 0.0, "kI": 0.0, "kD": 0.0},
                    "Depth": {"kP": 0.0, "kI": 0.0, "kD": 0.0}
                },
                "Control Profile": "default.json"
            }

class SettingsDialog(QDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.ui = Ui_settingsDialog()
        self.ui.setupUi(self)
        self.setup_connections()
        self.settings = defaultSettings
        self.resetIMU = False
        self.updatePID = False        

    def onOpen(self, event):
        self.setSettingsWindowValues()
        event.accept()

    def setup_connections(self):
        self.ui.resetIMUBut.clicked.connect(self.resetIMU_button_click)
        self.ui.updatePIDBut.clicked.connect(self.updatePID_button_click)
        self.ui.ipVal.mousePressEvent

    def resetIMU_button_click(self):
        self.resetIMU = True

    def updatePID_button_click(self):
        self.setSettings()
        self.updatePID = True

    def save_settings(self):
        with open("Settings.json", "w") as f:
            json.dump(self.settings, f)

    def load_settings(self):
        if os.path.exists("Settings.json"):
            with open("Settings.json", "r") as f:
                self.settings = json.load(f)
        else:
            self.settings = defaultSettings   
        self.setSettingsWindowValues()

    def setSettingsWindowValues(self):
        self.ui.ipVal.setText(self.settings["IP address"])
        self.ui.portVal.setText(str(self.settings["Port"]))
        self.ui.rollKPval.setValue(self.settings["PID"]["Roll"]["kP"])
        self.ui.rollKIval.setValue(self.settings["PID"]["Roll"]["kI"])
        self.ui.rollKDval.setValue(self.settings["PID"]["Roll"]["kD"])
        self.ui.pitchKIval.setValue(self.settings["PID"]["Pitch"]["kI"])
        self.ui.pitchKDval.setValue(self.settings["PID"]["Pitch"]["kD"])
        self.ui.pitchKPval.setValue(self.settings["PID"]["Pitch"]["kP"])
        self.ui.yawKPval.setValue(self.settings["PID"]["Yaw"]["kP"])
        self.ui.yawKIval.setValue(self.settings["PID"]["Yaw"]["kI"])
        self.ui.yawKDval.setValue(self.settings["PID"]["Yaw"]["kD"])
        self.ui.depthKPval.setValue(self.settings["PID"]["Depth"]["kP"])
        self.ui.depthKIval.setValue(self.settings["PID"]["Depth"]["kI"])
        self.ui.depthKDval.setValue(self.settings["PID"]["Depth"]["kD"])

    def closeEvent(self, event):
        self.setSettings()
        self.save_settings()
        self.accept()
        event.accept()

    def setSettings(self):
        self.settings = {
            "IP address": self.ui.ipVal.text(),
            "Port": int(self.ui.portVal.text()),
            "PID": {
                "Roll": {
                    "kP": self.ui.rollKPval.value(),
                    "kI": self.ui.rollKIval.value(),
                    "kD": self.ui.rollKDval.value()},
                "Pitch": {
                    "kP": self.ui.pitchKPval.value(),
                    "kI": self.ui.pitchKIval.value(),
                    "kD": self.ui.pitchKDval.value()},
                "Yaw": {
                    "kP": self.ui.yawKPval.value(),
                    "kI": self.ui.yawKIval.value(),
                    "kD": self.ui.yawKDval.value()},
                "Depth": {
                    "kP": self.ui.depthKPval.value(),
                    "kI": self.ui.depthKIval.value(),
                    "kD": self.ui.depthKDval.value()}
                },
                "Control Profile": self.settings["Control Profile"]
            }