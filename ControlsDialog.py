from CustomLineEdit import CustomLineEdit
from UI.controls_window import Ui_controlsDialog
import json, os, pygame
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QDialog, QLineEdit, QComboBox, QFileDialog
from joystickInputDetector import JoystickInputDetector

defaultControls = {
    "Primary Device": "Keyboard", "Secondary Device": "Keyboard",
    "Forward":                   {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Strafe":                    {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Vertical":                  {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Yaw":                       {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Roll":                      {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Pitch":                     {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Camera angle":              {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Manipulator rotate":        {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Manipulator grip":          {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},        
    "Move forward":              {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Move backwards":            {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},        
    "Move left":                 {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Move right":                {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},        
    "Rotate left":               {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Rotate right":              {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},        
    "Move down":                 {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Move up":                   {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},        
    "Roll increment":            {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Roll decrement":            {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},        
    "Pitch increment":           {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Pitch decrement":           {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},        
    "Camera rotate up":          {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Camera rotate down":        {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},        
    "Manipulator rotate left":   {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Manipulator rotate right":  {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},        
    "Manipulator grip close":    {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Manipulator grip open":     {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},        
    "Lights":                    {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
    "Reset position":            {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},        
    "Master":                    {"Primary": {"Control": "", "Inverted": False},"Secondary": {"Control": "", "Inverted": False}},
}

class ControlsDialog(QDialog):
    def __init__(self, parentApp):
        self.parentApp = parentApp
        super(ControlsDialog, self).__init__()
        self.ui = Ui_controlsDialog()
        self.ui.setupUi(self)
        self.profileName = "default.json"
        self.controlsToInversionsMap = {
            "Forward":           {"Primary": self.ui.primaryForwardInv,   "Secondary": self.ui.secondaryForwardInv},   
            "Strafe":            {"Primary": self.ui.primaryStrafeInv,  "Secondary": self.ui.secondaryStrafeInv},
            "Vertical":          {"Primary": self.ui.primaryVerticalInv,  "Secondary": self.ui.secondaryVerticalInv},  
            "Yaw":               {"Primary": self.ui.primaryYawInv,     "Secondary": self.ui.secondaryYawInv},
            "Roll":              {"Primary": self.ui.primaryRollInv,      "Secondary": self.ui.secondaryRollInv},      
            "Pitch":             {"Primary": self.ui.primaryPitchInv,   "Secondary": self.ui.secondaryPitchInv},
            "Camera angle":      {"Primary": self.ui.primaryCamAngleInv,  "Secondary": self.ui.secondaryCamAngleInv},  
            "Manipulator rotate":{"Primary": self.ui.primaryManRotInv,  "Secondary": self.ui.secondaryManRotInv},
            "Manipulator grip":  {"Primary": self.ui.primaryManGripInv,   "Secondary": self.ui.secondaryManGripInv}
            }

        self.controlsToEditsMap = {
            "Forward":                   {"Primary": "primaryForward",       "Secondary": "secondaryForward"},
            "Strafe":                    {"Primary": "primaryStrafe",        "Secondary": "secondaryStrafe"},
            "Vertical":                  {"Primary": "primaryVertical",      "Secondary": "secondaryVertical"},
            "Yaw":                       {"Primary": "primaryYaw",           "Secondary": "secondaryYaw"},
            "Roll":                      {"Primary": "primaryRoll",          "Secondary": "secondaryRoll"},
            "Pitch":                     {"Primary": "primaryPitch",         "Secondary": "secondaryPitch"},
            "Camera angle":              {"Primary": "primaryCamAngle",      "Secondary": "secondaryCamAngle"},
            "Manipulator rotate":        {"Primary": "primaryManRot",        "Secondary": "secondaryManRot"},
            "Manipulator grip":          {"Primary": "primaryManGrip",       "Secondary": "secondaryManGrip"},
            "Move forward":              {"Primary": "primaryForwardBut",    "Secondary": "secondaryForwardBut"},
            "Move backwards":            {"Primary": "primaryBackwardsBut",  "Secondary": "secondaryBackwardsBut"},
            "Move left":                 {"Primary": "primaryLeftBut",       "Secondary": "secondaryLeftBut"},
            "Move right":                {"Primary": "primaryRightBut",      "Secondary": "secondaryRightBut"},
            "Rotate left":               {"Primary": "primaryRotLeftBut",    "Secondary": "secondaryRotLeftBut"},
            "Rotate right":              {"Primary": "primaryRotRightBut",   "Secondary": "secondaryRotRightBut"},
            "Move down":                 {"Primary": "primaryDownBut",       "Secondary": "secondaryDownBut"},
            "Move up":                   {"Primary": "primaryUpBut",         "Secondary": "secondaryUpBut"},
            "Roll increment":            {"Primary": "primaryRollInc",       "Secondary": "secondaryRollInc"},
            "Roll decrement":            {"Primary": "primaryRollDec",       "Secondary": "secondaryRollDec"},
            "Pitch increment":           {"Primary": "primaryPitchInc",      "Secondary": "secondaryPitchInc"},
            "Pitch decrement":           {"Primary": "primaryPitchDec",      "Secondary": "secondaryPitchDec"},
            "Camera rotate up":          {"Primary": "primaryCamUp",         "Secondary": "secondaryCamUp"},
            "Camera rotate down":        {"Primary": "primaryCamDown",       "Secondary": "secondaryCamDown"},
            "Manipulator rotate left":   {"Primary": "primaryManLeft",       "Secondary": "secondaryManLeft"},
            "Manipulator rotate right":  {"Primary": "primaryManRight",      "Secondary": "secondaryManRight"},
            "Manipulator grip close":    {"Primary": "primaryManClose",      "Secondary": "secondaryManClose"},
            "Manipulator grip open":     {"Primary": "primaryManOpen",       "Secondary": "secondaryManOpen"},
            "Lights":                    {"Primary": "primaryLightsOn",      "Secondary": "secondaryLightsOn"},
            "Reset position":            {"Primary": "primaryPosReset",      "Secondary": "secondaryPosReset"},
            "Master":                    {"Primary": "primaryMaster",        "Secondary": "secondaryMaster"}
            }

        pygame.init
        pygame.joystick.init
        self.ignoreChanges = False

        # If custom actions is needed
        action_map = {}
        # Action mapping examle
        # action_map = {
        #     "primaryForward": {
        #         "left":self.prim_forward_Lbutton_click,
        #         "right":self.prim_forward_Lbutton_click,
        #                         },
        #     "primaryMaster": {
        #         "left": self.prim_master_Lbutton_click,
        #         "right": self.prim_master_Lbutton_click,
        #                       }
        #     }
        self.custom_line_edits = []
        self.inputDevices = []
        self.replace_widgets(self,action_map)
        self.countdownTimer = QTimer()
        self.countdownTimer.timeout.connect(self.onCountdownTimer)
        self.progressValue = 0
        self.controlProfile = {}
        self.getInputDevices()     
        self.ui.primaryDeviceList.currentIndexChanged.connect(self.primaryDeviceSelected)
        self.ui.secondaryDeviceList.currentIndexChanged.connect(self.secondaryDeviceSelected)

        self.joystick_thread = None
        self.currentInput = ["",""]
        
        for control, value in self.controlsToInversionsMap.items():
            value["Primary"].stateChanged.connect(self.setinversionOnCheckBox)
            value["Secondary"].stateChanged.connect(self.setinversionOnCheckBox)
        
        self.ui.saveProfileBut.clicked.connect(self.onSaveButton)
        self.ui.loadProfileMan.clicked.connect(self.onLoadButton)

    def updateDevicesInParent(self):
        # self.parentApp.primaryJoystick = self.controlProfile["Primary Device"]
        # self.parentApp.secondaryJoystick = self.controlProfile["Secondary Device"]
        self.parentApp.primaryIdx = self.parentApp.getJoystickIndex(self.controlProfile["Primary Device"])
        self.parentApp.secondaryIdx = self.parentApp.getJoystickIndex(self.controlProfile["Secondary Device"])
    
    def primaryDeviceSelected(self, index):
        if self.ignoreChanges:
            return
        self.controlProfile["Primary Device"] = self.ui.primaryDeviceList.itemText(index)
        print("Primary device selected: " + self.controlProfile["Primary Device"])
        self.updateDevicesInParent()
        
    def setinversionOnCheckBox(self):
        if self.ignoreChanges:
            return
        for control, value in self.controlsToInversionsMap.items():
            self.controlProfile[control]["Primary"]["Inverted"] = value["Primary"].isChecked()
            self.controlProfile[control]["Secondary"]["Inverted"] = value["Secondary"].isChecked()
    
    def secondaryDeviceSelected(self, index):
        if self.ignoreChanges:
            return
        self.controlProfile["Secondary Device"] = self.ui.secondaryDeviceList.itemText(index)
        print("Secondary device selected: " + self.controlProfile["Secondary Device"])
        self.updateDevicesInParent()
    
    def getInputDevices(self):
        if not pygame.get_init():
            pygame.init()
            pygame.joystick.init()
        for i in range(pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            self.inputDevices.append(joystick.get_name())
            joystick.quit()
        self.inputDevices.append("Keyboard")

    def closeEvent(self, event):
        self.accept()
        self.setWindowTitle("Controls")
        pygame.quit()
        if self.joystick_thread:
            self.joystick_thread.stop()
        event.accept()
        self.updateDevicesInParent()
    
    def getQComboBoxItems(self, comboBox: QComboBox):
        items = [comboBox.itemText(i) for i in range(comboBox.count())]
        return items
    
    def safeDeviceListAdd(self):
        primItems = self.getQComboBoxItems(self.ui.primaryDeviceList)
        secItems = self.getQComboBoxItems(self.ui.secondaryDeviceList)
        for device in self.inputDevices:
            if not device in primItems:
                self.ui.primaryDeviceList.addItem(device)
        for device in self.inputDevices:
            if not device in secItems:
                self.ui.secondaryDeviceList.addItem(device)

    def updateChecks(self):
        for control, value in self.controlsToInversionsMap.items():
            value["Primary"].setChecked(self.controlProfile[control]["Primary"]["Inverted"])
            value["Secondary"].setChecked(self.controlProfile[control]["Secondary"]["Inverted"])

    def verifyChecks(self):
        for control, value in self.controlsToInversionsMap.items():
            if not value["Primary"].checkState() == self.controlProfile[control]["Primary"]["Inverted"]:
                value["Primary"].setChecked(self.controlProfile[control]["Primary"]["Inverted"])
            if not value["Secondary"].checkState() == self.controlProfile[control]["Secondary"]["Inverted"]:
                value["Secondary"].setChecked(self.controlProfile[control]["Secondary"]["Inverted"])

    def updateControlsMapWindow(self):
        self.ignoreChanges = True
        self.safeDeviceListAdd()
        for control, value in self.controlProfile.items():
            if control == "Primary Device":
                if not value in self.getQComboBoxItems(self.ui.primaryDeviceList):
                    self.ui.primaryDeviceList.addItem(value)
                self.ui.primaryDeviceList.setCurrentText(value)
                continue
            if control == "Secondary Device":
                if not value in self.getQComboBoxItems(self.ui.secondaryDeviceList):
                    self.ui.secondaryDeviceList.addItem(value)
                self.ui.secondaryDeviceList.setCurrentText(value)
                continue
            self.get_line_edit(self.controlsToEditsMap[control]["Primary"]).setText(value["Primary"]["Control"])
            self.get_line_edit(self.controlsToEditsMap[control]["Secondary"]).setText(value["Secondary"]["Control"])
            if control in self.controlsToInversionsMap:
                self.controlsToInversionsMap[control]["Primary"].setChecked(value["Primary"]["Inverted"])
                self.controlsToInversionsMap[control]["Secondary"].setChecked(value["Secondary"]["Inverted"])
        self.updateChecks()
        self.verifyChecks()
        self.ignoreChanges = False
        self.updateDevicesInParent()

    def startCoundown(self):
        self.progressValue = 5000
        self.ui.inputProgressBar.setValue(self.progressValue)
        self.countdownTimer.start(1)

    def load_control_profile(self, filename):    
        controlProfile = defaultControls
        if os.path.exists(filename):
            with open(filename, "r") as f:
                controlProfile = json.load(f)
            profileName = os.path.splitext(os.path.basename(filename))[0]
            self.ui.profileNameVal.setText(profileName)
            self.parentApp.settingsDialog.settings["Control Profile"] = profileName + ".json"
            self.parentApp.settingsDialog.save_settings()
            self.parentApp.update_settings()
        else:
            with open(filename, "w") as f:
                json.dump(controlProfile, f)
            self.ui.profileNameVal.setText("default")
        self.controlProfile = controlProfile
        self.updateControlsMapWindow()

    def onLoadButton(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "JSON файлы (*.json)")
        if file_path:
            self.load_control_profile(file_path)

    def onCountdownTimer(self):
        self.progressValue -= 1 if self.progressValue > 0 else 0
        self.ui.inputProgressBar.setValue(self.progressValue)
        if not self.progressValue:
            self.stopCountdown("Controls - No input detected")

    def replace_widgets(self, dialog, action_map):
        self.replace_widget_with_custom(dialog.layout(), QLineEdit, action_map)

    def findLinkedControl(self, name):
        ctrl = ""
        type = ""
        inv = False
        for control, value in self.controlsToEditsMap.items():
            if value["Primary"] == name:
                ctrl = control
                type = "Primary"
                break
            elif value["Secondary"] == name:
                ctrl = control
                type = "Secondary"
                break
        if ctrl in self.controlsToInversionsMap:
            inv = self.controlsToInversionsMap[ctrl][type].isChecked()
        return (ctrl, type, inv)

    def stopCountdown(self, msg):
        self.countdownTimer.stop()
        self.progressValue = 0        
        self.ui.inputProgressBar.setValue(self.progressValue)
        self.setWindowTitle(msg)

    def controlMapLC(self, name):
        if name == "profileNameVal":
            return
        if self.progressValue:
            return         
        control, type, inv = self.findLinkedControl(name)
        self.setWindowTitle("Controls - " + control + ": Waiting for input")
        self.startCoundown()
        device = ""
        if type == "Primary":
            device = self.controlProfile["Primary Device"]
        if type == "Secondary":
            device = self.controlProfile["Secondary Device"]

        self.currentInput = [control, type]
        if self.joystick_thread:
            if self.joystick_thread.isFinished():
                self.joystick_thread = JoystickInputDetector(device)
        else:
            self.joystick_thread = JoystickInputDetector(device)
        if control in self.controlsToInversionsMap:
            self.joystick_thread.axis_moved.connect(self.onGamepadAxesDetected)
        else:
            self.joystick_thread.button_pressed.connect(self.onGameadButtonDetected)
            self.joystick_thread.button_released.connect(self.onGameadButtonDetected)
            self.joystick_thread.dpad_moved.connect(self.onGamePadDpad)
            if device == "Keyboard":
                self.joystick_thread.keyboard_press.connect(self.onKeyboardKeyDetected)


        self.joystick_thread.start()
        #self.setCustomLineEditText(self.controlsToEditsMap[control][type],type + control)

    def onSaveButton(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", self.ui.profileNameVal.text() + ".json" , "JSON файлы (*.json)")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(self.controlProfile, file, ensure_ascii=False, indent=4)
            
    def onGamePadDpad(self, x, y):
        if not x and not y:
            return
        control = self.currentInput[0]
        type = self.currentInput[1]
        if not control or not type:
            return
        self.currentInput = ["",""]        
        self.joystick_thread.stop()
        self.controlProfile[control][type]["Control"] = "Dpad " + str(x)+";"+str(y)
        dpadName = ""
        if (x, y) == (0, 1):
            dpadName = ("D-Pad Up")
        elif (x, y) == (0, -1):
            dpadName = ("D-Pad Down")
        elif (x, y) == (-1, 0):
            dpadName = ("D-Pad Left")
        elif (x, y) == (1, 0):
            dpadName = ("D-Pad Right")
        self.stopCountdown("Control - Input " + dpadName + " is set for " + type + " " + control)
        self.setCustomLineEditText(self.controlsToEditsMap[control][type], dpadName)
        print(self.controlProfile[control][type])
        self.updateDevicesInParent()
        
    def onKeyboardKeyDetected(self, key):        
        control = self.currentInput[0]
        type = self.currentInput[1]
        if not control or not type:
            return
        self.currentInput = ["",""]
        self.controlProfile[control][type]["Control"] = key
        self.joystick_thread.stop()
        self.stopCountdown("Control - Input " + key + " is set for " + type + " " + control)
        self.setCustomLineEditText(self.controlsToEditsMap[control][type],"Key " + key)
        print(self.controlProfile[control][type])
        self.updateDevicesInParent()
    
    def onGameadButtonDetected(self, button):        
        control = self.currentInput[0]
        type = self.currentInput[1]
        if not control or not type:
            return
        self.currentInput = ["",""]
        self.controlProfile[control][type]["Control"] = "Button " + str(button)
        self.joystick_thread.stop()
        self.stopCountdown("Control - Input Button " + str(button) + " is set for " + type + " " + control)
        self.setCustomLineEditText(self.controlsToEditsMap[control][type],"Button " + str(button))
        print(self.controlProfile[control][type])
        self.updateDevicesInParent()

    def onGamepadAxesDetected(self, axis):
        control = self.currentInput[0]
        type = self.currentInput[1]
        if not control or not type:
            return
        self.currentInput = ["",""]
        self.joystick_thread.stop()
        self.controlProfile[control][type]["Control"] = "Axis " + str(axis)
        self.controlProfile[control][type]["Inverted"] = self.controlsToInversionsMap[control][type].isChecked()        
        self.stopCountdown("Control - Input Axis " + str(axis) + " is set for " + type + " " + control)
        self.setCustomLineEditText(self.controlsToEditsMap[control][type],"Axis " + str(axis))
        print(self.controlProfile[control][type])
        self.updateDevicesInParent()

    def controlMapRC(self, name):
        if name == "profileNameVal":
            return
        if self.progressValue:            
            self.stopCountdown("Controls - Input canceled")
            self.currentInput = ["",""]
            return
        control, type, inv = self.findLinkedControl(name)
        self.controlProfile[control][type]["Control"] = ""
        self.setWindowTitle("Controls - Input for " + control + " cleared")
        self.setCustomLineEditText(name, "")
        self.updateDevicesInParent()

    def get_line_edit(self, name):
        for line_edit in self.custom_line_edits:
            if line_edit.objectName() == name:
                return line_edit
        return None

    def setCustomLineEditText(self, name, text):
        line_edit = self.get_line_edit(name)
        if line_edit:
            line_edit.setText(text)

    def getLineEditText(self, name):
        line_edit = self.get_line_edit(name)
        if line_edit:
            return line_edit.text()
        
    def showEvent(self, event):                        
        self.updateControlsMapWindow()
        super().showEvent(event)

    def replace_widget_with_custom(self, layout, base_class, action_map):
        """Рекурсивно заменяет виджеты типа `base_class` на `CustomLineEdit` в заданном `layout`."""
        if layout is None:
            return

        for i in range(layout.count()):
            item = layout.itemAt(i)

            # Если элемент - виджет, проверяем его тип
            widget = item.widget()
            if widget and isinstance(widget, base_class) and not widget.objectName() == "profileNameVal":
                # Создаем кастомный виджет, сохраняя все свойства
                custom_widget = CustomLineEdit(self)
                custom_widget.setGeometry(widget.geometry())
                custom_widget.setStyleSheet(widget.styleSheet())
                custom_widget.setReadOnly(widget.isReadOnly())  # Сохраняем состояние readOnly

                # Копируем специфические свойства
                custom_widget.setText(widget.text())
                custom_widget.setPlaceholderText(widget.placeholderText())
                custom_widget.setObjectName(widget.objectName())  # Сохраняем objectName
                custom_widget.setMinimumSize(widget.minimumSizeHint())  # Сохраняем размеры

                # Подключаем сигналы для обработки кликов в зависимости от objectName
                custom_widget.leftClicked.connect(lambda name=custom_widget.objectName(): action_map.get(name, {}).get('left', lambda: self.controlMapLC(name))())
                custom_widget.rightClicked.connect(lambda name=custom_widget.objectName(): action_map.get(name, {}).get('right', lambda: self.controlMapRC(name))())

                # Заменяем виджет в layout
                layout.removeWidget(widget)
                widget.deleteLater()
                layout.insertWidget(i, custom_widget)

                self.custom_line_edits.append(custom_widget)

            # Если элемент - это вложенный layout, проверяем его рекурсивно
            elif item.layout():
                self.replace_widget_with_custom(item.layout(), base_class, action_map)