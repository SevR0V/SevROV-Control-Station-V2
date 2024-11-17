from PySide6.QtWidgets import QWidget
from UI.manipulatorControlWindow import Ui_Form

class ManipulatorControlWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)