import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLineEdit
from PySide6.QtCore import Qt, Signal
from main_window import Ui_MainWindow
from controls_window import Ui_controlsDialog
from settings_window import Ui_settingsDialog

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

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()       # создаём экземпляр интерфейса
        self.ui.setupUi(self) 
        self.num = 0
        self.settingsDialogUi = Ui_settingsDialog()
        self.controlsDialogUi = Ui_controlsDialog()
        self.controlsDialog = ControlsDialog(self.num)

        #self.replace_widget_with_custom(self.ui.centralwidget.layout(), QLineEdit, CustomLineEdit)
                # инициализируем интерфейс в главном окне
        self.setup_connections()        # создаём обработчики событий

    def setup_connections(self):
        # Пример подключения событий к интерфейсу
        self.ui.settingsBut.clicked.connect(self.settings_button_click)  # подключаем кнопку
        self.ui.controlsBut.clicked.connect(self.controls_button_click)

    def settings_button_click(self):
        # Пример реакции на нажатие кнопки
        #self.ui.label.setText("Кнопка нажата!")
        settingsDialog = SettingsDialog()
        settingsDialog.exec()
        print(self.controlsDialog.num)
        

    def controls_button_click(self):
        # Пример реакции на нажатие кнопки
        #self.ui.label.setText("Кнопка нажата!")
        
        self.controlsDialog.exec()
        #print(self.controlsDialogUi.profileNameVal.text())
    
    def on_left_click(self):
        print("Левая кнопка мыши нажата на кнопке")

    def on_right_click(self):
        print("Правая кнопка мыши нажата на кнопке")

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

    def print_specific_line_edit_text(self, name):
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())