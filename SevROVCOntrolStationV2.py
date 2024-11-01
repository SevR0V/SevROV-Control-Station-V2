import sys
import asyncio
import struct
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLineEdit
from PySide6.QtCore import Qt, Signal, QTimer, Slot, QThread
from main_window import Ui_MainWindow
from controls_window import Ui_controlsDialog
from settings_window import Ui_settingsDialog
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

class CustomLineEdit(QLineEdit):
    leftClicked = Signal()
    rightClicked = Signal()

    def __init__(self, *args, **kwargs):
        super(CustomLineEdit, self).__init__(*args, **kwargs)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.leftClicked.emit()
        elif event.button() == Qt.RightButton:
            self.rightClicked.emit()
        super(CustomLineEdit, self).mousePressEvent(event)

    def contextMenuEvent(self, event):
        # Отключаем контекстное меню
        event.ignore()
    def mouseDoubleClickEvent(self, event):
        event.ignore()

class AsyncioThread(QThread):
    def __init__(self, IP, port):
        super().__init__()
        self.loop = asyncio.new_event_loop()
        self.IP = IP
        self.port = port
        self.protocol = None
        self.transport = None
        self.udpServer = UDPServer()

    async def start_udp_server(self):
        self.transport, self.protocol = await self.loop.create_datagram_endpoint(
            lambda: self.udpServer, local_addr=('0.0.0.0', 8888)
        )
    
    def run(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.start_udp_server())
        self.loop.run_forever()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()       # создаём экземпляр интерфейса
        self.ui.setupUi(self) 
        self.num = 0
        self.settingsDialogUi = Ui_settingsDialog()
        self.controlsDialogUi = Ui_controlsDialog()
        self.controlsDialog = ControlsDialog(self.num)
        
        
        self.stabEnable = False
        self.remoteIP = '192.169.0.12'
        self.remotePort = 1337
        self.connected = False
        #данные для аппарата
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
        self.cRollPid = [0.0, 0.0, 0.0] #kP,kI,kD
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
        #данные телеметрии
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
        
        # Запускаем асинхронный UDP сервер в отдельном потоке
        self.udp_thread = AsyncioThread(self.remoteIP, self.remotePort)
        self.udp_thread.start()
        
        #self.replace_widget_with_custom(self.ui.centralwidget.layout(), QLineEdit, CustomLineEdit)
                # инициализируем интерфейс в главном окне
        self.setup_connections()        # создаём обработчики событий

                # Таймер для отправки данных
        self.controlTimer = QTimer()
        self.controlTimer.timeout.connect(self.sendControl)   
        self.controlTimer.start(2000)
        
        
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
        # Пример подключения событий к интерфейсу
        self.ui.settingsBut.clicked.connect(self.settings_button_click)  # подключаем кнопку
        self.ui.controlsBut.clicked.connect(self.controls_button_click)
        self.ui.connectButton.clicked.connect(self.connectionButtonClick)

    def settings_button_click(self):
        # Пример реакции на нажатие кнопки
        #self.ui.label.setText("Кнопка нажата!")
        settingsDialog = SettingsDialog()
        settingsDialog.exec()
        print(self.controlsDialog.num)
        
    def connectionButtonClick(self):
        print('Connection attempt to:' + self.remoteIP + ':' + str(self.remotePort)) 
        self.connectToRemote()
        self.connected = True


    def controls_button_click(self):
        # Пример реакции на нажатие кнопки
        #self.ui.label.setText("Кнопка нажата!")
        
        self.controlsDialog.exec()
        #print(self.controlsDialogUi.profileNameVal.text())
    
    def on_left_click(self):
        print("Левая кнопка мыши нажата на кнопке")

    def on_right_click(self):
        print("Правая кнопка мыши нажата на кнопке")
        
    def connectToRemote(self):
        startPacket = struct.pack("=BB", 0xAA, 0xFF)
        self.udp_thread.transport.sendto(startPacket, (self.remoteIP, self.remotePort))

    def sendControl(self):
        if not self.connected:
            return
        # Отправляем данные из lineEdit1 на сервер
        # controlFlags, forward, strafe, vertical, rotation, rollInc, pitchInc, powerTarget, cameraRotate, manipulatorGrip, manipulatorRotate, rollKp, rollKi, rollKd, pitchKp, pitchKi, pitchKd, yawKp, yawKi, yawKd, depthKp, depthKi, depthKd
        # flags = MASTER, lightState, stabRoll, stabPitch, stabYaw, stabDepth, resetPosition, resetIMU, updatePID
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

class SettingsDialog(QDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.settingsUI = Ui_settingsDialog()
        self.settingsUI.setupUi(self)
        self.setup_connections()
    
    def setup_connections(self):
        self.settingsUI.resetIMUBut.clicked.connect(self.resetIMU_button_click)
        self.settingsUI.ipVal.mousePressEvent
    
    def resetIMU_button_click(self):
        print(self.settingsUI.ipVal.text())

class ControlsDialog(QDialog):
    def __init__(self, num):
        self.num = num
        super(ControlsDialog, self).__init__()
        self.ui = Ui_controlsDialog()
        self.ui.setupUi(self)

        # self.replace_widgets(self, { 
        #     "primaryForward": self.prim_forward_Lbutton_click
        # })
        
        action_map = {
            "primaryForward": {
                "left":self.prim_forward_Lbutton_click,
                "right":self.prim_forward_Lbutton_click,
                                },   # Вызывается, когда нажимается "Кнопка 1"
            "primaryMaster": {
                "left": self.prim_master_Lbutton_click,
                "right": self.prim_master_Lbutton_click,
                              }
            }
        action_map = {}
        #self.replace_widget_with_custom(self.ui.layout, QLineEdit, CustomLineEdit, action_map)

        self.custom_line_edits = []

        self.replace_widgets(self,action_map)
        # self.setup_connections()
    
    # def setup_connections(self):
    #     self.ui.primaryForward.leftClicked.connect(self.prim_forward_Lbutton_click)
    
    def prim_forward_Lbutton_click(self):
        print(self)
        print('йооооо')
        self.setCustomLineEditText("primaryForward", 'ёшки матрёшки')

    def prim_master_Lbutton_click(self):
        print('йооооо')

    def replace_widgets(self, dialog, action_map):
        """Заменяет виджеты QLineEdit на CustomLineEdit в диалоге."""
        self.replace_widget_with_custom(dialog.layout(), QLineEdit, action_map)

    def controlMapLC(self, name):
        if name == "profileNameVal":
            return
        print('LC')
        
        print(name)
        self.num +=1
        print(self.num)

    def controlMapRC(self, name):
        if name == "profileNameVal":
            return
        print('RC')
        print(name)
        self.num -=1
        print(self.num)

    def get_line_edit(self, name):
        # Ищем кастомное поле ввода по objectName
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

class UDPServer(asyncio.DatagramProtocol):
    def __init__(self):
        print("sercer init")
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

    def connection_made(self, transport):
        self.transport = transport
        print("UDP Server started")

    def datagram_received(self, data, addr):
        #ERRORFLAGS, roll, pitch, yaw, depth, batVoltage, batCharge, batCurrent, rollSP, pitchSP
        received = struct.unpack_from("=Qfffffffff", data)
        self.tErrorsFlags = np.uint64(received[0])
        self.tRoll = received[1]
        self.tPitch = received[2]
        self.tYaw = received[3]
        self.tDepth = received[4]
        self.tVolts = received[5]
        self.tCharge = received[6]
        self.tAmps = received[7]
        self.tRollSP = received[8]
        self.tPitchSP = received[9]
        

    def error_received(self, exc):
        print(f"Error received: {exc}")

    def connection_lost(self, exc):
        print("UDP Server stopped")
        self.transport.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())