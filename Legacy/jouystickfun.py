import sys
import pygame
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox

class JoystickHandler(QThread):
    button_pressed = Signal(int)
    button_released = Signal(int)
    axis_moved = Signal(int, float)

    def __init__(self, joystick_index):
        super().__init__()
        self.joystick_index = joystick_index
        self.running = True

    def run(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(self.joystick_index)
        self.joystick.init()
        print(f"Используется джойстик: {self.joystick.get_name()}")
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    self.button_pressed.emit(event.button)
                elif event.type == pygame.JOYBUTTONUP:
                    self.button_released.emit(event.button)
                elif event.type == pygame.JOYAXISMOTION:
                    axis_value = self.joystick.get_axis(event.axis)
                    if abs(axis_value) > 0.6:
                        self.axis_moved.emit(event.axis, axis_value)

    def stop(self):
        self.running = False
        self.wait()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Device Selection Example")

        # Метка и кнопка остановки
        self.label = QLabel("Выберите устройство для обработки событий.")
        self.stop_button = QPushButton("Остановить устройство")
        self.stop_button.clicked.connect(self.stop_device)
        
        # ComboBox для выбора устройства (джойстик или клавиатура)
        self.device_select = QComboBox()
        self.device_select.addItems(["Клавиатура"] + self.get_joysticks())
        self.device_select.currentIndexChanged.connect(self.change_device)

        # Настройка интерфейса
        layout = QVBoxLayout()
        layout.addWidget(self.device_select)
        layout.addWidget(self.label)
        layout.addWidget(self.stop_button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Начинаем с выбранного устройства
        self.current_device_type = "Клавиатура"
        self.joystick_thread = None

    def get_joysticks(self):
        """Получение списка имен доступных джойстиков."""
        pygame.init()
        pygame.joystick.init()
        joystick_names = [pygame.joystick.Joystick(i).get_name() for i in range(pygame.joystick.get_count())]
        return joystick_names if joystick_names else ["Нет доступных джойстиков"]

    def start_joystick(self, joystick_index):
        """Запуск потока для выбранного джойстика."""
        self.joystick_thread = JoystickHandler(joystick_index)
        self.joystick_thread.button_pressed.connect(self.on_button_pressed)
        self.joystick_thread.button_released.connect(self.on_button_released)
        self.joystick_thread.axis_moved.connect(self.on_axis_moved)
        self.joystick_thread.start()
        self.label.setText(f"Запущен джойстик: {self.device_select.currentText()}")

    def stop_device(self):
        """Остановка текущего устройства."""
        if self.current_device_type == "Джойстик" and self.joystick_thread and self.joystick_thread.isRunning():
            self.joystick_thread.stop()
            self.label.setText("Джойстик остановлен")

    def change_device(self):
        """Переключение между устройствами в зависимости от выбора в ComboBox."""
        self.stop_device()  # Остановка текущего устройства

        # Определяем тип выбранного устройства
        selected_device = self.device_select.currentText()
        if selected_device == "Клавиатура":
            self.current_device_type = "Клавиатура"
            self.label.setText("Клавиатура активирована. Нажимайте клавиши для обработки событий.")
        elif selected_device != "Нет доступных джойстиков":
            self.current_device_type = "Джойстик"
            self.start_joystick(self.device_select.currentIndex() - 1)  # -1, так как клавиатура — первый элемент

    def on_button_pressed(self, button):
        self.label.setText(f"Нажата кнопка {button} на джойстике")

    def on_button_released(self, button):
        self.label.setText(f"Отжата кнопка {button} на джойстике")

    def on_axis_moved(self, axis, value):
        self.label.setText(f"Ось {axis} изменилась: {value:.2f}")

    def closeEvent(self, event):
        """Безопасная остановка потока при закрытии окна."""
        self.stop_device()
        event.accept()

    # Обработка событий клавиатуры, если выбрана клавиатура
    def keyPressEvent(self, event):
        if self.current_device_type == "Клавиатура":
            key = event.key()
            self.label.setText(f"Клавиша нажата: {Qt.Key(key).name}")

    def keyReleaseEvent(self, event):
        if self.current_device_type == "Клавиатура":
            key = event.key()
            self.label.setText(f"Клавиша отпущена: {Qt.Key(key).name}")

# Запуск приложения
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
