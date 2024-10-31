import tkinter as tk
from tkinter import ttk, messagebox
import socket
import threading
import struct
import time
import pygame

class ROVControlApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ROV Control Panel")
        self.geometry("400x600")

        # Инициализация переменных для настроек сети
        self.server_ip = "192.168.1.10"  # Начальное значение IP-адреса сервера
        self.control_port = 8000         # Начальный порт для отправки управляющих пакетов
        self.telemetry_port = 8001       # Начальный порт для приема телеметрии

        # Флаги состояния соединения
        self.connected = False
        self.running = False
        self.last_telemetry_time = 0

        # Создание элементов интерфейса
        self.create_widgets()

        # Инициализация джойстика
        self.init_joystick()

        # Обновление статуса подключения
        self.after(500, self.update_connection_status)

    def create_widgets(self):
        # Рамка для настроек подключения
        settings_frame = tk.LabelFrame(self, text="Настройки подключения")
        settings_frame.pack(pady=10, padx=10, fill="x")

        tk.Label(settings_frame, text="IP-адрес сервера:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.ip_entry = tk.Entry(settings_frame)
        self.ip_entry.insert(0, self.server_ip)
        self.ip_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(settings_frame, text="Порт управления:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.control_port_entry = tk.Entry(settings_frame)
        self.control_port_entry.insert(0, str(self.control_port))
        self.control_port_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(settings_frame, text="Порт телеметрии:").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.telemetry_port_entry = tk.Entry(settings_frame)
        self.telemetry_port_entry.insert(0, str(self.telemetry_port))
        self.telemetry_port_entry.grid(row=2, column=1, padx=5, pady=5)

        # Кнопка подключения
        self.connect_button = tk.Button(settings_frame, text="Подключиться", command=self.connect)
        self.connect_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Индикатор статуса подключения
        status_frame = tk.Frame(self)
        status_frame.pack(pady=10)

        self.connection_status_label = tk.Label(status_frame, text="Статус подключения:")
        self.connection_status_label.pack(side=tk.LEFT)

        self.connection_status_canvas = tk.Canvas(status_frame, width=20, height=20)
        self.status_circle = self.connection_status_canvas.create_oval(2, 2, 18, 18, fill='red')
        self.connection_status_canvas.pack(side=tk.LEFT, padx=5)

        # Метки для телеметрии
        self.telemetry_label = tk.Label(self, text="Данные телеметрии:")
        self.telemetry_label.pack()

        self.telemetry_text = tk.Text(self, height=15, width=50)
        self.telemetry_text.pack(pady=5)

    def init_joystick(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print(f"Джойстик подключен: {self.joystick.get_name()}")
        else:
            print("Джойстик не найден.")

    def connect(self):
        if not self.connected:
            # Получаем IP-адрес и порты из полей ввода
            self.server_ip = self.ip_entry.get()
            try:
                self.control_port = int(self.control_port_entry.get())
                self.telemetry_port = int(self.telemetry_port_entry.get())
            except ValueError:
                messagebox.showerror("Ошибка", "Пожалуйста, введите корректные номера портов.")
                return
            # Проверка корректности введенных данных
            if not self.server_ip:
                messagebox.showerror("Ошибка", "Пожалуйста, введите корректный IP-адрес.")
                return

            # Инициализация сокетов
            self.control_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.telemetry_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            # Привязываем сокет телеметрии
            try:
                self.telemetry_socket.bind(('', self.telemetry_port))
                # Устанавливаем тайм-аут для сокета телеметрии
                self.telemetry_socket.settimeout(1.0)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось привязать сокет телеметрии: {e}")
                return

            # Устанавливаем флаги соединения
            self.connected = True
            self.running = True

            # Запуск потоков
            self.telemetry_thread = threading.Thread(target=self.receive_telemetry)
            self.telemetry_thread.daemon = True
            self.telemetry_thread.start()

            self.control_thread = threading.Thread(target=self.send_control_packets)
            self.control_thread.daemon = True
            self.control_thread.start()

            # Отправка стартового пакета
            start_packet = bytes([0xAA, 0xFF])
            try:
                self.control_socket.sendto(start_packet, (self.server_ip, self.control_port))
                print("Стартовый пакет отправлен.")
            except Exception as e:
                print(f"Ошибка при отправке стартового пакета: {e}")

            self.connect_button.config(text="Отключиться")
        else:
            # Отключение
            self.connected = False
            self.running = False
            self.connect_button.config(text="Подключиться")

            # Закрываем сокеты
            try:
                self.control_socket.close()
                self.telemetry_socket.close()
            except Exception as e:
                print(f"Ошибка при закрытии сокетов: {e}")

            print("Отключено от сервера.")

    def send_control_packets(self):
        while self.connected and self.running:
            if self.connected:
                # Чтение данных с джойстика
                pygame.event.pump()
                if self.joystick:
                    # Пример осей джойстика (замените на соответствующие вашей модели)
                    forward = -self.joystick.get_axis(1)  # Вперед/назад
                    strafe = self.joystick.get_axis(0)    # Влево/вправо
                    vertical = -self.joystick.get_axis(2)  # Вверх/вниз
                    rotation = self.joystick.get_axis(3)  # Поворот

                    # Чтение кнопок для флагов
                    buttons = self.joystick.get_numbuttons()
                    MASTER = self.joystick.get_button(0)
                    lightState = self.joystick.get_button(1)
                    stabRoll = self.joystick.get_button(2)
                    stabPitch = self.joystick.get_button(3)
                    stabYaw = self.joystick.get_button(4)
                    stabDepth = self.joystick.get_button(5)
                    resetPosition = self.joystick.get_button(6)
                    resetIMU = self.joystick.get_button(7)
                    updatePID = self.joystick.get_button(8)
                else:
                    # Если джойстик не подключен, используем значения по умолчанию
                    forward = 0.0
                    strafe = 0.0
                    vertical = 0.0
                    rotation = 0.0
                    MASTER = 0
                    lightState = 0
                    stabRoll = 0
                    stabPitch = 0
                    stabYaw = 0
                    stabDepth = 0
                    resetPosition = 0
                    resetIMU = 0
                    updatePID = 0

                # Другие управляющие параметры (можно получить из интерфейса)
                rollInc = 0.0
                pitchInc = 0.0
                powerTarget = 0.0
                cameraRotate = 0.0
                manipulatorGrip = 0.0
                manipulatorRotate = 0.0
                # Параметры ПИД-регуляторов
                rollKp = 0.0
                rollKi = 0.0
                rollKd = 0.0
                pitchKp = 0.0
                pitchKi = 0.0
                pitchKd = 0.0
                yawKp = 0.0
                yawKi = 0.0
                yawKd = 0.0
                depthKp = 0.0
                depthKi = 0.0
                depthKd = 0.0

                # Формирование флагов управления
                controlFlags = (
                    (MASTER << 0) |
                    (lightState << 1) |
                    (stabRoll << 2) |
                    (stabPitch << 3) |
                    (stabYaw << 4) |
                    (stabDepth << 5) |
                    (resetPosition << 6) |
                    (resetIMU << 7) |
                    (updatePID << 8)
                )

                # Упаковка данных с использованием struct
                packet_data = struct.pack(
                    "=Qfffffffffffffffffff",
                    controlFlags,
                    forward,
                    strafe,
                    vertical,
                    rotation,
                    rollInc,
                    pitchInc,
                    powerTarget,
                    cameraRotate,
                    manipulatorGrip,
                    manipulatorRotate,
                    rollKp,
                    rollKi,
                    rollKd,
                    pitchKp,
                    pitchKi,
                    pitchKd,
                    yawKp,
                    yawKi,
                    yawKd,
                    depthKp,
                    depthKi,
                    depthKd
                )

                # Отправка пакета по UDP
                try:
                    self.control_socket.sendto(packet_data, (self.server_ip, self.control_port))
                except Exception as e:
                    print(f"Ошибка при отправке управляющего пакета: {e}")
            time.sleep(0.05)  # Отправляем пакеты приблизительно 20 раз в секунду
        print("Поток отправки управляющих пакетов остановлен.")

    def receive_telemetry(self):
        while self.connected and self.running:
            try:
                data, addr = self.telemetry_socket.recvfrom(1024)
                if data:
                    self.last_telemetry_time = time.time()
                    # Распаковка данных телеметрии
                    telemetry = struct.unpack('=Qfffffffff', data)
                    errorFlags = telemetry[0]
                    roll = telemetry[1]
                    pitch = telemetry[2]
                    yaw = telemetry[3]
                    depth = telemetry[4]
                    batVoltage = telemetry[5]
                    batCharge = telemetry[6]
                    batCurrent = telemetry[7]
                    rollSP = telemetry[8]
                    pitchSP = telemetry[9]

                    # Обновление данных в интерфейсе
                    telemetry_text = (
                        f"Флаги ошибок: {errorFlags}n"
                        f"Крен: {roll}n"
                        f"Тангаж: {pitch}n"
                        f"Рыскание: {yaw}n"
                        f"Глубина: {depth}n"
                        f"Напряжение батареи: {batVoltage}n"
                        f"Заряд батареи: {batCharge}n"
                        f"Ток батареи: {batCurrent}n"
                        f"Заданный крен: {rollSP}n"
                        f"Заданный тангаж: {pitchSP}n"
                    )
                    # Безопасное обновление интерфейса
                    self.telemetry_text.delete(1.0, tk.END)
                    self.telemetry_text.insert(tk.END, telemetry_text)
            except socket.timeout:
                # Тайм-аут срабатывает, чтобы можно было проверить флаг self.running
                continue
            except Exception as e:
                print(f"Ошибка при приеме телеметрии: {e}")
        print("Поток приема телеметрии остановлен.")

    def update_connection_status(self):
        # Проверяем, было ли получено телеметрическое сообщение в последнюю секунду
        current_time = time.time()
        if current_time - self.last_telemetry_time < 1.0:
            # Обновляем индикатор на зеленый
            self.connection_status_canvas.itemconfig(self.status_circle, fill='green')
        else:
            # Обновляем индикатор на красный
            self.connection_status_canvas.itemconfig(self.status_circle, fill='red')
        # Планируем следующую проверку
        self.after(500, self.update_connection_status)

if __name__ == '__main__':
    app = ROVControlApp()
    app.mainloop()
