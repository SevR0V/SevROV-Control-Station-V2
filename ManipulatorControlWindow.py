from PySide6.QtWidgets import QWidget
from UI.manipulatorControlWindow import Ui_Form

class ManipulatorControlWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()       # Создаем экземпляр интерфейса
        self.ui.setupUi(self)     # Настраиваем интерфейс на данном виджете (self)