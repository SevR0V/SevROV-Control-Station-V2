import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
import threading
import pygame
import time

class SevROVControlV2App:
    def __init__(self, master):
        self.master = master
        master.title("SevROV Control V2")

        # Initialize variables

        # Variables for ROV Connection
        self.connection_status = tk.BooleanVar()
        self.master_switch = tk.BooleanVar()

        # Telemetry data variables
        self.telemetry_data = {
            "Roll": tk.DoubleVar(),
            "Pitch": tk.DoubleVar(),
            "Heading": tk.DoubleVar(),
            "Depth": tk.DoubleVar(),
            "Voltage": tk.DoubleVar(),
            "Battery charge": tk.DoubleVar(),
            "Current": tk.DoubleVar(),
            "Roll Setpoint": tk.DoubleVar(),
            "Pitch Setpoint": tk.DoubleVar()
        }

        # Stabilization variables
        self.stabilization_enabled = tk.BooleanVar()
        self.stabilization = {
            "Roll": tk.BooleanVar(),
            "Pitch": tk.BooleanVar(),
            "Yaw": tk.BooleanVar(),
            "Depth": tk.BooleanVar()
        }

        # Power target variable
        self.power_target = tk.DoubleVar()

        # Initialize pygame for joystick and keyboard handling
        pygame.init()
        pygame.joystick.init()

        # Keep track of opened windows
        self.settings_window = None
        self.controls_window = None

        # Setup the main window
        self.create_main_window()

        # Initialize settings
        self.settings = {}

        # Load settings from file
        self.load_settings()

        # Load default control profile
        self.control_profile = {}
        self.load_control_profile("default.json")

        # Handle window close event
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_main_window(self):
        # Configure grid weights for resizing
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)

        # Create the ROV group
        rov_frame = ttk.LabelFrame(self.master, text="ROV")
        rov_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Connect button
        self.connect_button = ttk.Button(rov_frame, text="Connect", command=self.connect)
        self.connect_button.grid(row=0, column=0, padx=5, pady=5)

        # Connection status
        self.status_label = ttk.Label(rov_frame, text="Status:")
        self.status_label.grid(row=1, column=0, sticky="e")
        self.status_indicator = ttk.Label(rov_frame, text="●", foreground="red")
        self.status_indicator.grid(row=1, column=1, sticky="w")

        # MASTER switch group
        master_frame = ttk.LabelFrame(self.master, text="MASTER switch")
        master_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.master_switch_button = ttk.Checkbutton(master_frame, text="MASTER switch", variable=self.master_switch, command=self.update_master_status)
        self.master_switch_button.grid(row=0, column=0, padx=5, pady=5)

        self.master_status_label = ttk.Label(master_frame, text="SAFE", foreground="green")
        self.master_status_label.grid(row=0, column=1, padx=5, pady=5)

        # Telemetry data group
        telemetry_frame = ttk.LabelFrame(self.master, text="Telemetry data")
        telemetry_frame.grid(row=0, column=1, rowspan=2, padx=5, pady=5, sticky="nsew")
        # Telemetry labels and entries
        row = 0
        for key in ["Roll", "Pitch", "Heading", "Depth", "Voltage", "Battery charge", "Current"]:
            label = ttk.Label(telemetry_frame, text=key + ":")
            label.grid(row=row, column=0, sticky="e")
            entry = ttk.Entry(telemetry_frame, textvariable=self.telemetry_data[key], width=10)
            entry.grid(row=row, column=1)
            if key in ["Roll", "Pitch"]:
                # Also add setpoints
                setpoint_label = ttk.Label(telemetry_frame, text=key + " Setpoint:")
                setpoint_label.grid(row=row, column=2, sticky="e")
                setpoint_entry = ttk.Entry(telemetry_frame, textvariable=self.telemetry_data[key + " Setpoint"], width=10)
                setpoint_entry.grid(row=row, column=3)
            row += 1

        # Stabilization group
        stab_frame = ttk.LabelFrame(self.master, text="Stabilization")
        stab_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Enable stabilization checkbutton
        self.enable_stab_check = ttk.Checkbutton(stab_frame, text="Enable stabilization", variable=self.stabilization_enabled)
        self.enable_stab_check.grid(row=0, column=0, padx=5, pady=5)
        # Individual stabilization switches
        col = 1
        for key in ["Roll", "Pitch", "Yaw", "Depth"]:
            check = ttk.Checkbutton(stab_frame, text=key, variable=self.stabilization[key])
            check.grid(row=0, column=col, padx=5, pady=5)
            col +=1

        # Reset setpoints button
        self.reset_setpoints_button = ttk.Button(self.master, text="Reset setpoints", command=self.reset_setpoints)
        self.reset_setpoints_button.grid(row=3, column=0, padx=5, pady=5)

        # Power target field
        power_target_label = ttk.Label(self.master, text="Power target:")
        power_target_label.grid(row=3, column=1, sticky="e")
        self.power_target_entry = ttk.Entry(self.master, textvariable=self.power_target, width=10)
        self.power_target_entry.grid(row=3, column=2, sticky="w")

        # Settings and Controls buttons
        self.settings_button = ttk.Button(self.master, text="Settings", command=self.open_settings_window)
        self.settings_button.grid(row=4, column=0, padx=5, pady=5)
        self.controls_button = ttk.Button(self.master, text="Controls", command=self.open_controls_window)
        self.controls_button.grid(row=4, column=1, padx=5, pady=5)

    def connect(self):
        # Dummy connect function
        self.connection_status.set(not self.connection_status.get())
        self.update_connection_status()

    def update_connection_status(self):
        status = self.connection_status.get()
        color = "green" if status else "red"
        self.status_indicator.config(foreground=color)

    def update_master_status(self):
        status = self.master_switch.get()
        if status:
            self.master_status_label.config(text="ARMED", foreground="red")
        else:
            self.master_status_label.config(text="SAFE", foreground="green")

    def reset_setpoints(self):
        self.telemetry_data["Roll Setpoint"].set(0)
        self.telemetry_data["Pitch Setpoint"].set(0)
    def load_settings(self):
        if os.path.exists("Settings.txt"):
            with open("Settings.txt", "r") as f:
                self.settings = json.load(f)
            # Update settings fields if needed
        else:
            # Default settings
            self.settings = {
                "IP address": "192.168.0.1",
                "Port": 8888,
                "PID": {
                    "Roll": {"kP": 0.0, "kI": 0.0, "kD": 0.0},
                    "Pitch": {"kP": 0.0, "kI": 0.0, "kD": 0.0},
                    "Yaw": {"kP": 0.0, "kI": 0.0, "kD": 0.0},
                    "Depth": {"kP": 0.0, "kI": 0.0, "kD": 0.0}
                }
            }

    def save_settings(self):
        with open("Settings.txt", "w") as f:
            json.dump(self.settings, f)

    def load_control_profile(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                self.control_profile = json.load(f)
        else:
            # Create default control profile
            self.control_profile = {}
            # Save default profile
            with open(filename, "w") as f:
                json.dump(self.control_profile, f)

    def open_settings_window(self):
        if self.settings_window is None or not self.settings_window.winfo_exists():
            self.settings_window = SettingsWindow(self)
        else:
            self.settings_window.lift()

    def open_controls_window(self):
        if self.controls_window is None or not self.controls_window.winfo_exists():
            self.controls_window = ControlsWindow(self)
        else:
            self.controls_window.lift()

    def on_close(self):
        # Perform any cleanup
        # Close any open windows
        if self.controls_window and self.controls_window.winfo_exists():
            self.controls_window.on_close()
        if self.settings_window and self.settings_window.winfo_exists():
            self.settings_window.on_close()
        # Quit pygame if necessary
        pygame.quit()
        # Destroy the main window
        self.master.destroy()

    # Setters and Getters
    def get_connection_status(self):
        return self.connection_status.get()

    def set_connection_status(self, value):
        self.connection_status.set(value)
        self.update_connection_status()

    def get_master_switch(self):
        return self.master_switch.get()

    def set_master_switch(self, value):
        self.master_switch.set(value)
        self.update_master_status()

    def get_telemetry_data(self, key):
        return self.telemetry_data[key].get()

    def set_telemetry_data(self, key, value):
        self.telemetry_data[key].set(value)

    def get_stabilization_enabled(self):
        return self.stabilization_enabled.get()

    def set_stabilization_enabled(self, value):
        self.stabilization_enabled.set(value)

    def get_stabilization(self, key):
        return self.stabilization[key].get()

    def set_stabilization(self, key, value):
        self.stabilization[key].set(value)

    def get_power_target(self):
        return self.power_target.get()

    def set_power_target(self, value):
        self.power_target.set(value)

class SettingsWindow:
    def __init__(self, parent_app):
        self.parent_app = parent_app
        self.window = tk.Toplevel()
        self.window.title("Settings")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        # Configure grid weights for resizing
        self.window.columnconfigure(0, weight=1)

        # Connection group
        conn_frame = ttk.LabelFrame(self.window, text="Connection")
        conn_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.ip_address = tk.StringVar()
        self.port = tk.IntVar()

        ttk.Label(conn_frame, text="IP address:").grid(row=0, column=0, sticky="e")
        self.ip_entry = ttk.Entry(conn_frame, textvariable=self.ip_address)
        self.ip_entry.grid(row=0, column=1)

        ttk.Label(conn_frame, text="Port:").grid(row=1, column=0, sticky="e")
        self.port_entry = ttk.Entry(conn_frame, textvariable=self.port)
        self.port_entry.grid(row=1, column=1)

        # PID group
        pid_frame = ttk.LabelFrame(self.window, text="PID")
        pid_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.pid_values = {}
        row = 0
        for param in ["Roll", "Pitch", "Yaw", "Depth"]:
            ttk.Label(pid_frame, text=param + ":").grid(row=row, column=0, sticky="e")
            kp_var = tk.DoubleVar()
            ki_var = tk.DoubleVar()
            kd_var = tk.DoubleVar()
            self.pid_values[param] = {"kP": kp_var, "kI": ki_var, "kD": kd_var}
            ttk.Entry(pid_frame, textvariable=kp_var, width=5).grid(row=row, column=1)
            ttk.Entry(pid_frame, textvariable=ki_var, width=5).grid(row=row, column=2)
            ttk.Entry(pid_frame, textvariable=kd_var, width=5).grid(row=row, column=3)
            row +=1

        self.update_pid_button = ttk.Button(pid_frame, text="Update PID", command=self.update_pid)
        self.update_pid_button.grid(row=row, column=0, columnspan=4, pady=5)

        # Reset angles button
        self.reset_angles_button = ttk.Button(self.window, text="Reset angles", command=self.reset_angles)
        self.reset_angles_button.grid(row=2, column=0, padx=5, pady=5)

        # Load settings into fields
        self.load_settings_into_fields()

    def update_pid(self):
        # Update PID settings
        # For now, just print to console
        print("Updating PID settings:")
        for param, values in self.pid_values.items():
            print(f"{param}: kP={values['kP'].get()}, kI={values['kI'].get()}, kD={values['kD'].get()}")

    def reset_angles(self):
        # Reset angles
        print("Resetting angles")

    def load_settings_into_fields(self):
        settings = self.parent_app.settings
        # Load IP and port
        self.ip_address.set(settings.get("IP address", "192.168.0.1"))
        self.port.set(settings.get("Port", 8888))
        # Load PID settings
        pid_settings = settings.get("PID", {})
        for param, values in self.pid_values.items():
            param_settings = pid_settings.get(param, {})
            values["kP"].set(param_settings.get("kP", 0))
            values["kI"].set(param_settings.get("kI", 0))
            values["kD"].set(param_settings.get("kD", 0))

    def save_settings_from_fields(self):
        settings = self.parent_app.settings
        settings["IP address"] = self.ip_address.get()
        settings["Port"] = self.port.get()
        # PID settings
        pid_settings = {}
        for param, values in self.pid_values.items():
            pid_settings[param] = {
                "kP": values["kP"].get(),
                "kI": values["kI"].get(),
                "kD": values["kD"].get()
            }
        settings["PID"] = pid_settings

    def on_close(self):
        # Save settings
        self.save_settings_from_fields()
        self.parent_app.save_settings()
        self.parent_app.settings_window = None
        self.window.destroy()

class ControlsWindow:
    def __init__(self, parent_app):
        self.parent_app = parent_app
        self.window = tk.Toplevel()
        self.window.title("Controls")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        # Flag to signal threads to stop
        self.running = True

        # Get list of input devices
        self.input_devices = []
        for i in range(pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            self.input_devices.append(joystick.get_name())

        # Add Keyboard as an input device
        self.input_devices.append("Keyboard")

        # Configure grid weights for resizing
        self.window.columnconfigure(0, weight=1)

        # Device selection
        device_frame = ttk.Frame(self.window)
        device_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        ttk.Label(device_frame, text="Input Device:").grid(row=0, column=0, sticky="e")
        self.input_device_primary = tk.StringVar()
        self.input_device_secondary = tk.StringVar()
        self.primary_device_combobox = ttk.Combobox(device_frame, textvariable=self.input_device_primary, width=25, values=self.input_devices)
        self.primary_device_combobox.grid(row=0, column=1)
        self.secondary_device_combobox = ttk.Combobox(device_frame, textvariable=self.input_device_secondary, width=25, values=self.input_devices)
        self.secondary_device_combobox.grid(row=0, column=2)

        # Load devices from profile if available
        self.input_device_primary.set(self.parent_app.control_profile.get("Primary Device", ""))
        self.input_device_secondary.set(self.parent_app.control_profile.get("Secondary Device", ""))

        # Fields for controls
        self.controls = {}
        values_frame = ttk.Frame(self.window)
        values_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        row =0

        control_values = [
            ("Forward", "Axis"),
            ("Strafe", "Axis"),
            ("Vertical", "Axis"),
            ("Yaw", "Axis"),
            ("Roll", "Axis"),
            ("Pitch", "Axis"),
            ("Roll increment up", "Button"),
            ("Roll increment down", "Button"),
            ("Camera rotate up", "Button"),
            ("Camera rotate down", "Button"),
            ("Manipulator rotate", "Axis"),
            ("Manipulator rotate left", "Button"),
            ("Manipulator rotate right", "Button"),
            ("Manipulator grip", "Axis"),
            ("Manipulator grip left", "Button"),
            ("Manipulator grip right", "Button"),
            ("Lights on/off", "Button"),
            ("Reset position", "Button"),
            ("MASTER switch", "Button"),
            ("MASTER ARM", "Button"),
            ("MASTER SAFE", "Button")
        ]

        ttk.Label(values_frame, text="Control").grid(row=0, column=0)
        ttk.Label(values_frame, text="Primary Input").grid(row=0, column=1)
        ttk.Label(values_frame, text="Inv").grid(row=0, column=2)
        ttk.Label(values_frame, text="Secondary Input").grid(row=0, column=3)
        ttk.Label(values_frame, text="Inv").grid(row=0, column=4)

        row =1
        for control, input_type in control_values:
            self.controls[control] = {
                "Primary": tk.StringVar(),
                "Secondary": tk.StringVar(),
                "Primary Inverted": tk.BooleanVar(),
                "Secondary Inverted": tk.BooleanVar(),
                "Type": input_type
            }
            ttk.Label(values_frame, text=control).grid(row=row, column=0, sticky="e")
            # Entries for inputs
            primary_entry = ttk.Entry(values_frame, textvariable=self.controls[control]["Primary"], width=15, state="readonly")
            primary_entry.grid(row=row, column=1)
            primary_entry.bind("<Button-1>", lambda e, c=control: self.wait_for_input("Primary", c))
            primary_entry.bind("<Button-3>", lambda e, c=control: self.clear_input("Primary", c))

            ttk.Checkbutton(values_frame, variable=self.controls[control]["Primary Inverted"]).grid(row=row, column=2)

            secondary_entry = ttk.Entry(values_frame, textvariable=self.controls[control]["Secondary"], width=15, state="readonly")
            secondary_entry.grid(row=row, column=3)
            secondary_entry.bind("<Button-1>", lambda e, c=control: self.wait_for_input("Secondary", c))
            secondary_entry.bind("<Button-3>", lambda e, c=control: self.clear_input("Secondary", c))

            ttk.Checkbutton(values_frame, variable=self.controls[control]["Secondary Inverted"]).grid(row=row, column=4)
            row+=1

        # Load controls from profile if available
        self.load_controls_from_profile()

        # Profile field and save/load buttons
        profile_frame = ttk.Frame(self.window)
        profile_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        ttk.Label(profile_frame, text="Profile name:").grid(row=0, column=0, sticky="e")
        self.profile_name = tk.StringVar()
        self.profile_name.set("default")
        ttk.Entry(profile_frame, textvariable=self.profile_name).grid(row=0, column=1)
        self.save_profile_button = ttk.Button(profile_frame, text="Save Profile", command=self.save_profile)
        self.save_profile_button.grid(row=0, column=2, padx=5)
        self.load_profile_button = ttk.Button(profile_frame, text="Load Profile", command=self.load_profile)
        self.load_profile_button.grid(row=0, column=3, padx=5)

        # Flag to stop input waiting thread
        self.waiting_for_input = False

    def wait_for_input(self, device_type, control_name):
        # Start a thread to wait for input
        if self.waiting_for_input:
            return  # Already waiting
        self.waiting_for_input = True

        def input_thread():
            start_time = time.time()
            detected_input = None
            messagebox.showinfo("Input Capture", f"Waiting for {self.controls[control_name]['Type']} input...")

            # Record initial state of axes
            initial_axis_values = {}
            initial_hat_values = {}
            while time.time() - start_time < 5:
                if not self.running:
                    break  # Stop if window is closed
                pygame.event.pump()
                # Handle keyboard input
                if (device_type == "Primary" and self.input_device_primary.get() == "Keyboard") or (device_type == "Secondary" and self.input_device_secondary.get() == "Keyboard"):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            detected_input = f"Key {pygame.key.name(event.key)}"
                            break
                    if detected_input:
                        break
                else:
                    # Handle joystick input
                    if self.controls[control_name]["Type"] == "Button":
                        for i in range(pygame.joystick.get_count()):
                            joystick = pygame.joystick.Joystick(i)
                            joystick.init()
                            if device_type == "Primary" and joystick.get_name() != self.input_device_primary.get():
                                continue
                            if device_type == "Secondary" and joystick.get_name() != self.input_device_secondary.get():
                                continue
                            for event in pygame.event.get():
                                if event.type == pygame.JOYBUTTONDOWN and event.joy == joystick.get_id():
                                    detected_input = f"Button {event.button}"
                                    break
                            if detected_input:
                                break
                    elif self.controls[control_name]["Type"] == "Axis":
                        for i in range(pygame.joystick.get_count()):
                            joystick = pygame.joystick.Joystick(i)
                            joystick.init()
                            if device_type == "Primary" and joystick.get_name() != self.input_device_primary.get():
                                continue
                            if device_type == "Secondary" and joystick.get_name() != self.input_device_secondary.get():
                                continue
                            joystick_id = joystick.get_id()
                            num_axes = joystick.get_numaxes()
                            if joystick_id not in initial_axis_values:
                                initial_axis_values[joystick_id] = [joystick.get_axis(a) for a in range(num_axes)]
                            for axis in range(num_axes):
                                initial_value = initial_axis_values[joystick_id][axis]
                                current_value = joystick.get_axis(axis)
                                if abs(current_value - initial_value) > 0.1:
                                    detected_input = f"Axis {axis}"
                                    break
                            if detected_input:
                                break
                    elif self.controls[control_name]["Type"] == "Hat":
                        for i in range(pygame.joystick.get_count()):
                            joystick = pygame.joystick.Joystick(i)
                            joystick.init()
                            if device_type == "Primary" and joystick.get_name() != self.input_device_primary.get():
                                continue
                            if device_type == "Secondary" and joystick.get_name() != self.input_device_secondary.get():
                                continue
                            joystick_id = joystick.get_id()
                            num_hats = joystick.get_numhats()
                            if joystick_id not in initial_hat_values:
                                initial_hat_values[joystick_id] = [joystick.get_hat(h) for h in range(num_hats)]
                            for hat in range(num_hats):
                                initial_value = initial_hat_values[joystick_id][hat]
                                current_value = joystick.get_hat(hat)
                                if current_value != initial_value:
                                    detected_input = f"Hat {hat} Value {current_value}"
                                    break
                            if detected_input:
                                break
                if detected_input:
                    break
                time.sleep(0.01)
            if detected_input:
                self.controls[control_name][device_type].set(detected_input)
            else:
                if self.running:  # Avoid showing message if window was closed
                    messagebox.showinfo("Input Capture", "No input detected.")
            self.waiting_for_input = False

        thread = threading.Thread(target=input_thread)
        thread.daemon = True  # Allow thread to exit when main program exits
        thread.start()

    def clear_input(self, device_type, control_name):
        # Clear the input field
        self.controls[control_name][device_type].set("")

    def save_profile(self):
        # Save profile to file
        profile_data = {}
        profile_data["Primary Device"] = self.input_device_primary.get()
        profile_data["Secondary Device"] = self.input_device_secondary.get()
        for control, values in self.controls.items():
            profile_data[control] = {
                "Primary": values["Primary"].get(),
                "Secondary": values["Secondary"].get(),
                "Primary Inverted": values["Primary Inverted"].get(),
                "Secondary Inverted": values["Secondary Inverted"].get(),
                "Type": values["Type"]
            }
        profile_name = self.profile_name.get()
        filename = profile_name + ".json"
        with open(filename, "w") as f:
            json.dump(profile_data, f)
        messagebox.showinfo("Save Profile", f"Profile saved to {filename}")

    def load_profile(self):
        # Load profile from file
        profile_name = self.profile_name.get()
        filename = profile_name + ".json"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                profile_data = json.load(f)
            self.input_device_primary.set(profile_data.get("Primary Device", ""))
            self.input_device_secondary.set(profile_data.get("Secondary Device", ""))
            for control, values in profile_data.items():
                if control in self.controls:
                    self.controls[control]["Primary"].set(values["Primary"])
                    self.controls[control]["Secondary"].set(values["Secondary"])
                    self.controls[control]["Primary Inverted"].set(values["Primary Inverted"])
                    self.controls[control]["Secondary Inverted"].set(values["Secondary Inverted"])
            messagebox.showinfo("Load Profile", f"Profile loaded from {filename}")
        else:
            messagebox.showerror("Load Profile", f"Profile {filename} does not exist.")

    def load_controls_from_profile(self):
        # Load controls from parent_app's control profile
        profile_data = self.parent_app.control_profile
        self.input_device_primary.set(profile_data.get("Primary Device", ""))
        self.input_device_secondary.set(profile_data.get("Secondary Device", ""))
        for control, values in profile_data.items():
            if control in self.controls:
                self.controls[control]["Primary"].set(values["Primary"])
                self.controls[control]["Secondary"].set(values["Secondary"])
                self.controls[control]["Primary Inverted"].set(values["Primary Inverted"])
                self.controls[control]["Secondary Inverted"].set(values["Secondary Inverted"])

    def save_controls_to_profile(self):
        profile_data = {}
        profile_data["Primary Device"] = self.input_device_primary.get()
        profile_data["Secondary Device"] = self.input_device_secondary.get()
        for control, values in self.controls.items():
            profile_data[control] = {
                "Primary": values["Primary"].get(),
                "Secondary": values["Secondary"].get(),
                "Primary Inverted": values["Primary Inverted"].get(),
                "Secondary Inverted": values["Secondary Inverted"].get(),
                "Type": values["Type"]
            }
        self.parent_app.control_profile = profile_data
        # Save to default.json
        with open("default.json", "w") as f:
            json.dump(profile_data, f)

    def on_close(self):
        # Save control profile to parent app
        self.running = False  # Signal any threads to stop
        self.save_controls_to_profile()
        self.parent_app.controls_window = None
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SevROVControlV2App(root)
    root.mainloop()
