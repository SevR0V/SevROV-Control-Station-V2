import pygame
from PySide6.QtCore import QThread, Signal

class JoystickInputDetecto(QThread):
    button_pressed = Signal(int)
    button_released = Signal(int)
    axis_moved = Signal(int, float)    
    dpad_moved = Signal(int, int)
    keyboard_press = Signal(str)

    def __init__(self, pyg: pygame, joystick: pygame.joystick, joystickName):
        super().__init__()
        self.pyg = pyg
        self.joystick = joystick
        self.joystickName = joystickName
        self.joystick_index = -1
        self.findIndex()
        self.running = True
        
    def findIndex(self):
        for i in range(self.joystick.get_count()):
            joystick = self.joystick.Joystick(i)
            joystick.init()
            if self.joystickName == joystick.get_name():
                self.joystick_index = i
                break
            elif i == self.joystick.get_count()-1:
                self.joystick_index = -1
                self.stop()

    def run(self):
        if (self.joystick_index == -1) and not (self.joystickName == "Keyboard"):
            return
        joystick= None
        if not (self.joystickName == "Keyboard"):
            joystick = self.joystick.Joystick(self.joystick_index)
            joystick.init()
        while self.running:
            for event in self.pyg.event.get():
                if event.type == self.pyg.JOYBUTTONDOWN:
                    self.button_pressed.emit(event.button)
                elif event.type == self.pyg.JOYBUTTONUP:
                    self.button_released.emit(event.button)
                elif event.type == self.pyg.JOYAXISMOTION:
                    if joystick:
                        axis_value = joystick.get_axis(event.axis)
                        if abs(axis_value) >= 0.5:
                            self.axis_moved.emit(event.axis, axis_value)
                elif event.type == self.pyg.JOYHATMOTION:
                    x, y = event.value
                    self.dpad_moved.emit(x, y)
                elif self.joystickName == "Keyboard":
                    if event.type == self.pyg.KEYDOWN:
                        key = event.key
                        self.keyboard_press.emit(key)
                        



    def stop(self):
        self.running = False
        self.wait()