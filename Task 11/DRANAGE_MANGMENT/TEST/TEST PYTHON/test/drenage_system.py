import paho.mqtt.client as mqttclient
import time
import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors

# Get information about all monitors
for monitor in get_monitors():
    print("Width:", monitor.width)
    print("Height:", monitor.height)



class MQTTApp:
    def __init__(self, root):
        # Tkinter setup
        self.root = root
        self.root.title("MQTT Data Progression")
        self.root.geometry(str(monitor.width)+"x"+str(monitor.height))  # Set a fixed window size to remove excess space
        self.root.resizable(False, False)  # Make the window non-resizable
        
        self.water_level_max_read_value = 280
        self.obstacles_level_max_read_value = 280
        self.cm_water = 0
        self.cm_obstacles = 0
        self.cm_water_bard1 = 0
        self.cm_obstacles_bard1 = 0
        self.cm_water_bard3 = 0
        self.cm_obstacles_bard3 = 0
        self.connected = False

        # Grid configuration to make layout more compact
        self.root.grid_rowconfigure(0, weight=1, minsize=150)  # Allow row 0 to expand but with a minimum height
        self.root.grid_columnconfigure(0, weight=1, minsize=250)  # Allow column 0 to expand with a minimum width
        self.root.grid_columnconfigure(1, weight=1, minsize=250)  # Allow column 1 to expand with a minimum width
        
        # Frame for bard2 data (left side)
        self.bard2_frame = tk.Frame(self.root)
        self.bard2_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Title for bard2 section
        self.bard2_title = tk.Label(self.bard2_frame, text="Node2 Data", font=("Helvetica", int(monitor.width*(2/100)), "bold"))
        self.bard2_title.pack(pady=5)

        # Water Level Progress Bar for bard2
        self.water_level_label = tk.Label(self.bard2_frame, text="Water Level : 0%")
        self.water_level_label.pack()
        self.water_level_bar = ttk.Progressbar(self.bard2_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.water_level_bar.pack()

        # Obstacles Progress Bar for bard2
        self.obstacles_label = tk.Label(self.bard2_frame, text="Obstacles : 0%")
        self.obstacles_label.pack()
        self.obstacles_bar = ttk.Progressbar(self.bard2_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.obstacles_bar.pack()

        # Frame for bard1 data (right side)
        self.bard1_frame = tk.Frame(self.root)
        self.bard1_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Add bard1 label
        self.bard1_label = tk.Label(self.bard1_frame, text="Node 1  Data", font=("Helvetica", int(monitor.width*(2/100)), "bold"))
        self.bard1_label.pack(pady=5)

        # Water Level Progress Bar for bard1
        self.water_level_label_bard1 = tk.Label(self.bard1_frame, text="Water Level (bard1): 0%")
        self.water_level_label_bard1.pack()
        self.water_level_bar_bard1 = ttk.Progressbar(self.bard1_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.water_level_bar_bard1.pack()

        # Obstacles Progress Bar for bard1
        self.obstacles_label_bard1 = tk.Label(self.bard1_frame, text="Obstacles (bard1): 0%")
        self.obstacles_label_bard1.pack()
        self.obstacles_bar_bard1 = ttk.Progressbar(self.bard1_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.obstacles_bar_bard1.pack()

        # Set up custom style for green progress bars
        self.style = ttk.Style()
        self.style.configure("TProgressbar",
                             thickness=20,  # Set the thickness of the progress bar
                             troughcolor="lightgray",  # Background of the progress bar
                             background="green",  # Color of the filled part
                             )

        # Apply the style to the progress bars
        self.water_level_bar.configure(style="TProgressbar")
        self.obstacles_bar.configure(style="TProgressbar")
        self.water_level_bar_bard1.configure(style="TProgressbar")
        self.obstacles_bar_bard1.configure(style="TProgressbar")

        # Frame for bard3 data (third section - center aligned)
        self.bard3_frame = tk.Frame(self.root)
        self.bard3_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")  # Put bard3 on a new row and span both columns

        # Title for bard3 section
        self.bard3_title = tk.Label(self.bard3_frame, text="Node3 Data", font=("Helvetica", int(monitor.width*(2/100)), "bold"))
        self.bard3_title.pack(pady=5)

        # Water Level Progress Bar for bard3
        self.water_level_label_bard3 = tk.Label(self.bard3_frame, text="Water Level (bard3): 0%")
        self.water_level_label_bard3.pack()
        self.water_level_bar_bard3 = ttk.Progressbar(self.bard3_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.water_level_bar_bard3.pack()

        # Obstacles Progress Bar for bard3
        self.obstacles_label_bard3 = tk.Label(self.bard3_frame, text="Obstacles (bard3): 0%")
        self.obstacles_label_bard3.pack()
        self.obstacles_bar_bard3 = ttk.Progressbar(self.bard3_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.obstacles_bar_bard3.pack()

        # MQTT client setup
        self.client = mqttclient.Client(client_id="89biln7212", protocol=mqttclient.MQTTv311)
        self.client.username_pw_set("89biln7212", password="5678deghlz")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect("b37.mqtt.one", port=1883)

        # Start MQTT client loop
        self.client.loop_start()

        # Wait for connection
        self.wait_for_connection()


    # MQTT connection callback
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected")
            self.connected = True
            client.subscribe("89biln7212/")  # Subscribe after connection
        else:
            print("Not connected")

    # MQTT message callback
    def on_message(self, client, userdata, message):
        msg = str(message.payload.decode('utf-8'))
        self.msg_to_work(msg)

    # MQTT message handler function
    def msg_to_work(self, msg):
        # Handle bard2 messages
        if "bard2" in msg:
            msg = msg.replace('bard2', '')  # Remove 'bard2' from the message
            
            if "water level: " in msg:
                msg = msg.replace(' water level: ', '')
                try:
                    self.cm_water = int(int(msg) / 10)
                    water_level = (int(msg) / self.water_level_max_read_value) * 100
                    self.update_progress_bar(water_level, "Water Level", self.cm_water)
                except ValueError:
                    print("Invalid water level value")
                    
            elif "obstacles: " in msg:
                msg = msg.replace(' obstacles: ', '')
                try:
                    self.cm_obstacles = int(int(msg) / 10)
                    obstacles = (int(msg) / self.obstacles_level_max_read_value) * 100
                    self.update_progress_bar(obstacles, "Obstacles", self.cm_obstacles)
                except ValueError:
                    print("Invalid obstacles value")
        
        # Handle bard1 messages (fix: replace 'bard1' instead of 'bard2')
        if "bard1" in msg:
            msg = msg.replace('bard1', '')  # Correctly remove 'bard1' from the message
            
            if "water level: " in msg:
                msg = msg.replace(' water level: ', '')
                try:
                    self.cm_water_bard1 = int(int(msg) / 10)
                    water_level = (int(msg) / self.water_level_max_read_value) * 100
                    self.update_progress_bar_bard1(water_level, "Water Level (bard1)", self.cm_water_bard1)
                except ValueError:
                    print("Invalid water level value")
                    
            elif "obstacles: " in msg:
                msg = msg.replace(' obstacles: ', '')
                try:
                    self.cm_obstacles_bard1 = int(int(msg) / 10)
                    obstacles = (int(msg) / self.obstacles_level_max_read_value) * 100
                    self.update_progress_bar_bard1(obstacles, "Obstacles (bard1)", self.cm_obstacles_bard1)
                except ValueError:
                    print("Invalid obstacles value")


        if "bard3" in msg:
            msg = msg.replace('bard3', '')  # Correctly remove 'bard3' from the message
            if "water level: " in msg:
                msg = msg.replace(' water level: ', '')
                try:
                    self.cm_water_bard3 = int(int(msg) / 10)
                    water_level = (int(msg) / self.water_level_max_read_value) * 100
                    self.update_progress_bar_bard3(water_level, "Water Level (bard3)", self.cm_water_bard3)
                except ValueError:
                    print("Invalid water level value")
                
            elif "obstacles: " in msg:
                msg = msg.replace(' obstacles: ', '')
                try:
                    self.cm_obstacles_bard3 = int(int(msg) / 10)
                    obstacles = (int(msg) / self.obstacles_level_max_read_value) * 100
                    self.update_progress_bar_bard3(obstacles, "Obstacles (bard3)", self.cm_obstacles_bard3)
                except ValueError:
                    print("Invalid obstacles value")

    # Tkinter progress bar update function for bard2 (Reversed)
    def update_progress_bar(self, value, label, cm):
        # Reverse the value by subtracting from 100
        reversed_value = 100 - value
        
        if label == "Water Level":
            self.water_level_bar["value"] = reversed_value
            self.water_level_label["text"] = f"Water Level (bard2): {cm}%"
        elif label == "Obstacles":
            self.obstacles_bar["value"] = reversed_value
            self.obstacles_label["text"] = f"Obstacles (bard2): {cm}%"
    
    # Tkinter progress bar update function for bard1 (Reversed)
    def update_progress_bar_bard1(self, value, label, cm):
        # Reverse the value by subtracting from 100
        reversed_value = 100 - value
        
        if label == "Water Level (bard1)":
            self.water_level_bar_bard1["value"] = reversed_value
            self.water_level_label_bard1["text"] = f"Water Level (bard1): {cm}%"
        elif label == "Obstacles (bard1)":
            self.obstacles_bar_bard1["value"] = reversed_value
            self.obstacles_label_bard1["text"] = f"Obstacles (bard1): {cm}%"

    # Wait for MQTT connection to be established
    def wait_for_connection(self):
        while not self.connected:
            time.sleep(0.2)

    # Main loop (Tkinter)
    def run(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("Interrupted by user")
        finally:
            self.client.loop_stop()
            self.client.disconnect()  # Clean disconnection


# Create Tkinter root window and start the MQTTApp
root = tk.Tk()
app = MQTTApp(root)
app.run()
