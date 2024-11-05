import pygame
from PySide6.QtCore import QThread, Signal

class JoystickInputDetector(QThread):
    button_pressed = Signal(int)
    button_released = Signal(int)
    axis_moved = Signal(int, float)    
    dpad_moved = Signal(int, int)
    keyboard_press = Signal(str)

    def __init__(self, joystickName):
        super().__init__()

        self.joystickName = joystickName
        self.joystick_index = -1
        pygame.init()
        pygame.joystick.init
        self.findIndex()
        self.running = True        
        
    def findIndex(self):
        for i in range(pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            if self.joystickName == joystick.get_name():
                self.joystick_index = i
                break
            # elif i == self.joystick.get_count()-1:
            #     self.joystick_index = -1
            #     self.stop()

    def run(self):
        if (self.joystick_index == -1) and not (self.joystickName == "Keyboard"):
            return
        joystick= None
        if not pygame.get_init():
            pygame.init()
        if not (self.joystickName == "Keyboard"):
            joystick = pygame.joystick.Joystick(self.joystick_index)
            joystick.init()
        while self.running:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.JOYBUTTONDOWN:
                        self.button_pressed.emit(event.button)
                    elif event.type == pygame.JOYBUTTONUP:
                        self.button_released.emit(event.button)
                    elif event.type == pygame.JOYAXISMOTION:
                        if joystick:
                            axis_value = joystick.get_axis(event.axis)
                            if abs(axis_value) >= 0.5:
                                self.axis_moved.emit(event.axis, axis_value)
                    elif event.type == pygame.JOYHATMOTION:
                        x, y = event.value
                        self.dpad_moved.emit(x, y)
                    elif self.joystickName == "Keyboard":
                        if event.type == pygame.KEYDOWN:
                            key = event.key
                            self.keyboard_press.emit(key)
            except:
                continue
                        
    def stop(self):
        pygame.quit()
        self.running = False
        self.wait()