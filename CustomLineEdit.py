from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLineEdit


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