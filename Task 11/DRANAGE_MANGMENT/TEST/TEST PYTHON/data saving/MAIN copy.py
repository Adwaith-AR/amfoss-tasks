from typing import Self
import paho.mqtt.client as mqttclient
from openpyxl import Workbook
import time
import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors
import os
from datetime import datetime, timedelta



b1d=0
b2d=0
b3d=0

b1wl=0
b1ol=0
b1gl=0
b2wl=0
b2ol=0
b2gl=0
b3wl=0
b3ol=0
b3gl=0




# Get information about all monitors
for monitor in get_monitors():
    print("Width:", monitor.width)
    print("Height:", monitor.height)



def color_of_Progress_Bar(a):
    colour=""
    if a>30:
        colour="Green"
    elif a>70:
        colour="Yellow"
    elif a>100:
        colour="Red"
    return colour






class MQTTApp:
    def __init__(self, root):
        # Tkinter setup
        self.root = root
        self.root.title("MQTT Data Progression")
        self.root.geometry(str(monitor.width) + "x" + str(monitor.height-30))  # Set a fixed window size to remove excess space
        self.root.resizable(True, True)  # Make the window non-resizable
        
        self.water_level_max_read_value = 280
        self.obstacles_level_max_read_value = 280
        self.gas_level_max_read_value = 280
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
        self.water_level_label = tk.Label(self.bard2_frame, text="Water Level ")
        self.water_level_label.pack()
        self.water_level_bar = ttk.Progressbar(self.bard2_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.water_level_bar.pack()

        # Obstacles Progress Bar for bard2
        self.obstacles_label = tk.Label(self.bard2_frame, text="Obstacles ")
        self.obstacles_label.pack()
        self.obstacles_bar = ttk.Progressbar(self.bard2_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.obstacles_bar.pack()

        self.gas_label = tk.Label(self.bard2_frame, text="gas ")
        self.gas_label.pack()
        self.gas_bar = ttk.Progressbar(self.bard2_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.gas_bar.pack()


        # Frame for bard1 data (right side)
        self.bard1_frame = tk.Frame(self.root)
        self.bard1_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Add bard1 label
        self.bard1_label = tk.Label(self.bard1_frame, text="Node 1  Data", font=("Helvetica", int(monitor.width*(2/100)), "bold"))
        self.bard1_label.pack(pady=5)

        # Water Level Progress Bar for bard1
        self.water_level_label_bard1 = tk.Label(self.bard1_frame, text="Water Level ")
        self.water_level_label_bard1.pack()
        self.water_level_bar_bard1 = ttk.Progressbar(self.bard1_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.water_level_bar_bard1.pack()

        # Obstacles Progress Bar for bard1
        self.obstacles_label_bard1 = tk.Label(self.bard1_frame, text="Obstacles ")
        self.obstacles_label_bard1.pack()
        self.obstacles_bar_bard1 = ttk.Progressbar(self.bard1_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.obstacles_bar_bard1.pack()

        self.gas_label_bard1 = tk.Label(self.bard1_frame, text="gas ")
        self.gas_label_bard1.pack()
        self.gas_bar_bard1 = ttk.Progressbar(self.bard1_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.gas_bar_bard1.pack()

        # Set up custom style for green progress bars
        

        # Frame for bard3 data (third section - center aligned)
        self.bard3_frame = tk.Frame(self.root)
        self.bard3_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")  # Put bard3 on a new row and span both columns

        # Title for bard3 section
        self.bard3_title = tk.Label(self.bard3_frame, text="Node3 Data", font=("Helvetica", int(monitor.width*(2/100)), "bold"))
        self.bard3_title.pack(pady=5)

        # Water Level Progress Bar for bard3
        self.water_level_label_bard3 = tk.Label(self.bard3_frame, text="Water Level ",)
        self.water_level_label_bard3.pack()
        self.water_level_bar_bard3 = ttk.Progressbar(self.bard3_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.water_level_bar_bard3.pack()
        

        # Obstacles Progress Bar for bard3
        self.obstacles_label_bard3 = tk.Label(self.bard3_frame, text="Obstacles ")
        self.obstacles_label_bard3.pack()
        self.obstacles_bar_bard3 = ttk.Progressbar(self.bard3_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.obstacles_bar_bard3.pack()

        self.gas_label_bard3 = tk.Label(self.bard3_frame, text="gas ")
        self.gas_label_bard3.pack()
        self.gas_bar_bard3 = ttk.Progressbar(self.bard3_frame, orient="horizontal", length=int(monitor.width*(33.33/100)), mode="determinate")
        self.gas_bar_bard3.pack()


        self.style = ttk.Style()
        self.style.configure("Green.Horizontal.TProgressbar",
                             thickness=30,  # Set the thickness of the progress bar
                             troughcolor="lightgray",  # Background of the progress bar
                             background="green",  # Color of the filled part
                             )
       
        self.style.configure("Red.Horizontal.TProgressbar",
                thickness=30,  # Set the thickness of the progress bar
                troughcolor="lightgray",  # Background color of the progress bar
                background="red",  # Color of the filled part
                )
        self.style.configure("Yellow.Horizontal.TProgressbar",
                             thickness=30,  # Set the thickness of the progress bar
                             troughcolor="lightgray",  # Background of the progress bar
                             background="yellow",  # Color of the filled part
                             )

        

# Apply the style to the progress bars
        self.water_level_bar.configure(style="Green.Horizontal.TProgressbar")
        self.obstacles_bar.configure(style="Green.Horizontal.TProgressbar")
        self.gas_bar.configure(style="Green.Horizontal.TProgressbar")
        self.water_level_bar_bard1.configure(style="Green.Horizontal.TProgressbar")
        self.obstacles_bar_bard1.configure(style="Green.Horizontal.TProgressbar")
        self.gas_bar_bard1.configure(style="Green.Horizontal.TProgressbar")
        self.water_level_bar_bard3.configure(style="Green.Horizontal.TProgressbar")
        self.obstacles_bar_bard3.configure(style="Green.Horizontal.TProgressbar")
        self.gas_bar_bard3.configure(style="Green.Horizontal.TProgressbar")
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
       
        global b1wl
        global b1ol
        global b1gl
        global b2wl
        global b2ol
        global b2gl
        global b3wl
        global b3ol
        global b3gl
        global b1d
        global b2d
        global b3d
        
        # Handle bard2 messages
        if "bard2" in msg:
            b2d=b2d+1
            msg = msg.replace('bard2', '')  # Remove 'bard2' from the message
            
            if "water level: " in msg:
                msg = msg.replace(' water level: ', '')
                print(msg)
                try:
                    self.cm_water = int(int(msg) / 10)
                    b2wl=int(int(msg) / 10)
                    water_level = (int(msg) / self.water_level_max_read_value) * 100
                    self.update_progress_bar(water_level, "Water Level", self.cm_water)
                except ValueError:
                    print("Invalid water level value")
                    
            elif "obstacles: " in msg:
                msg = msg.replace(' obstacles: ', '')
                print(msg)

                try:
                    b2ol=int(int(msg) / 10)
                    self.cm_obstacles = int(int(msg) / 10)
                    obstacles = (int(msg) / self.obstacles_level_max_read_value) * 100
                    self.update_progress_bar(obstacles, "Obstacles", self.cm_obstacles)
                except ValueError:
                    print("Invalid obstacles value")
            elif "gas: " in msg:
                msg = msg.replace(' gas: ', '')
                print(msg)


                try:
                    b2gl= int(int(msg) / 10)
                    self.cm_gas = int(int(msg) / 10)
                    gas = (int(msg) / self.gas_level_max_read_value) * 100
                    self.update_progress_bar(gas, "Gas Level", self.cm_gas)
                except ValueError:
                    print("Invalid gas value")

           
        
        # Handle bard1 messages (fix: replace 'bard1' instead of 'bard2')
        if "bard1" in msg:
            b1d=b1d+1
            msg = msg.replace('bard1', '')  # Correctly remove 'bard1' from the message
            
            if "water level: " in msg:
                msg = msg.replace(' water level: ', '')
                
                print(msg)


                try:
                    b1wl=int(int(msg) / 10)
                    self.cm_water_bard1 = int(int(msg) / 10)
                    water_level = (int(msg) / self.water_level_max_read_value) * 100
                    self.update_progress_bar_bard1(water_level, "Water Level", self.cm_water_bard1)
                except ValueError:
                    print("Invalid water level value")
                    
            elif "obstacles: " in msg:
                msg = msg.replace(' obstacles: ', '')
                print(msg)


                try:
                    b1ol=int(int(msg) / 10)
                    self.cm_obstacles_bard1 = int(int(msg) / 10)
                    obstacles = (int(msg) / self.obstacles_level_max_read_value) * 100
                    self.update_progress_bar_bard1(obstacles, "Obstacles", self.cm_obstacles_bard1)
                except ValueError:
                    print("Invalid obstacles value")
            elif "gas: " in msg:
                msg = msg.replace(' gas: ', '')
                msg=int(msg)
                print(msg)


                try:
                    b1gl=int(int(msg) / 10)
                    self.cm_gas_bard1 = int(int(msg) / 10)
                    gas = (int(msg) / self.gas_level_max_read_value) * 100
                    self.update_progress_bar_bard1(gas, "Gas Level", self.cm_gas_bard1)
                except ValueError:
                    print("Invalid gas value")
            

        if "bard3" in msg:
            b1d=b1d+1
            msg = msg.replace('bard3', '')  # Correctly remove 'bard3' from the message
            if "water level: " in msg:
                msg = msg.replace(' water level: ', '')
                print(msg)
                try:
                    b3wl=int(int(msg) / 10)
                    self.cm_water_bard3 = int(int(msg) / 10)
                    water_level = (int(msg) / self.water_level_max_read_value) * 100
                    self.update_progress_bar_bard3(water_level, "Water Level", self.cm_water_bard3)
                except ValueError:
                    print("Invalid water level value")
                
            elif "obstacles: " in msg:
                msg = msg.replace(' obstacles: ', '')
                print(msg)

                try:
                    b3ol=int(int(msg) / 10)
                    self.cm_obstacles_bard3 = int(int(msg) / 10)
                    obstacles = (int(msg) / self.obstacles_level_max_read_value) * 100
                    self.update_progress_bar_bard3(obstacles, "Obstacles", self.cm_obstacles_bard3)
                except ValueError:
                    print("Invalid obstacles value")
            elif "gas: " in msg:
                msg = msg.replace(' gas: ', '')
                print(msg)

                

                try:
                    b3gl=int(int(msg) / 10)
                    self.cm_gas_bard3 = int(int(msg) / 10)
                    gas = (int(msg) / self.gas_level_max_read_value) * 100
                    self.update_progress_bar_bard3(gas, "Gas Level",self.cm_gas_bard3)
                except ValueError:
                    print("Invalid gas value")
            
    
    # Tkinter progress bar update function for bard2 (Reversed)
    def update_progress_bar(self, value, label, cm):
        # Reverse the value by subtracting from 100
        reversed_value = 100 - value
        
        
        if label == "Water Level":
            if reversed_value < 30:
                self.water_level_bar.configure(style="Green.Horizontal.TProgressbar")
            elif reversed_value < 70:
                self.water_level_bar.configure(style="Yellow.Horizontal.TProgressbar")
            else:
                self.water_level_bar.configure(style="Red.Horizontal.TProgressbar")
            
            self.water_level_bar["value"] = reversed_value
            self.water_level_label["text"] = f"Water Level : {cm}%"
        elif label == "Obstacles":
            if reversed_value < 30:
                self.obstacles_bar.configure(style="Green.Horizontal.TProgressbar")
            elif reversed_value < 70:
                self.obstacles_bar.configure(style="Yellow.Horizontal.TProgressbar")
            else:
                self.obstacles_bar.configure(style="Red.Horizontal.TProgressbar")
            
            self.obstacles_bar["value"] = reversed_value
            self.obstacles_label["text"] = f"Obstacles : {cm}%"
        elif label == "Gas Level":
            if reversed_value < 30:
                self.gas_bar.configure(style="Green.Horizontal.TProgressbar")
            elif reversed_value < 70:
                self.gas_bar.configure(style="Yellow.Horizontal.TProgressbar")
            else:
                self.gas_bar.configure(style="Red.Horizontal.TProgressbar")
            
            self.gas_bar["value"] = reversed_value
            self.gas_label["text"] = f"Water Level : {reversed_value}%"
    
    # Tkinter progress bar update function for bard1 (Reversed)
    def update_progress_bar_bard1(self, value, label, cm):
        # Reverse the value by subtracting from 100
        reversed_value = 100 - value
        
        if label == "Water Level":
            if reversed_value < 30:
                self.water_level_bar_bard1.configure(style="Green.Horizontal.TProgressbar")
            elif reversed_value < 70:
                self.water_level_bar_bard1.configure(style="Yellow.Horizontal.TProgressbar")
            else:
                self.water_level_bar_bard1.configure(style="Red.Horizontal.TProgressbar")
            
            self.water_level_bar_bard1["value"] = reversed_value
            self.water_level_label_bard1["text"] = f"Water Level : {cm}%"
        elif label == "Obstacles":
            if reversed_value < 30:
                self.obstacles_bar_bard1.configure(style="Green.Horizontal.TProgressbar")
            elif reversed_value < 70:
                self.obstacles_bar_bard1.configure(style="Yellow.Horizontal.TProgressbar")
            else:
                self.obstacles_bar_bard1.configure(style="Red.Horizontal.TProgressbar")
            
            self.obstacles_bar_bard1["value"] = reversed_value
            self.obstacles_label_bard1["text"] = f"Obstacles : {cm}%"
        elif label == "Gas Level":
            if reversed_value < 30:
                self.gas_bar_bard1.configure(style="Green.Horizontal.TProgressbar")
            elif reversed_value < 70:
                self.gas_bar_bard1.configure(style="Yellow.Horizontal.TProgressbar")
            else:
                self.gas_bar_bard1.configure(style="Red.Horizontal.TProgressbar")
            
            self.gas_bar_bard1["value"] = reversed_value
            self.gas_label_bard1["text"] = f"Water Level : {reversed_value}%"
    def update_progress_bar_bard3(self, value, label, cm):
        # Reverse the value by subtracting from 100
        reversed_value = 100 - value
        
        if label == "Water Level":
            if reversed_value < 30:
                self.water_level_bar_bard3.configure(style="Green.Horizontal.TProgressbar")
            elif reversed_value < 70:
                self.water_level_bar_bard3.configure(style="Yellow.Horizontal.TProgressbar")
            else:
                self.water_level_bar_bard3.configure(style="Red.Horizontal.TProgressbar")
            
            self.water_level_bar_bard3["value"] = reversed_value
            self.water_level_label_bard3["text"] = f"Water Level : {cm}%"
        elif label == "Obstacles":
            if reversed_value < 30:
                self.obstacles_bar_bard3.configure(style="Green.Horizontal.TProgressbar")
            elif reversed_value < 70:
                self.obstacles_bar_bard3.configure(style="Yellow.Horizontal.TProgressbar")
            else:
                self.obstacles_bar_bard3.configure(style="Red.Horizontal.TProgressbar")
            
            self.obstacles_bar_bard3["value"] = reversed_value
            self.obstacles_label_bard3["text"] = f"Obstacles : {cm}%"
        elif label == "Gas Level":
            if reversed_value < 30:
                self.gas_bar_bard3.configure(style="Green.Horizontal.TProgressbar")
            elif reversed_value < 70:
                self.gas_bar_bard3.configure(style="Yellow.Horizontal.TProgressbar")
            else:
                self.gas_bar_bard3.configure(style="Red.Horizontal.TProgressbar")
            
            self.gas_bar_bard3["value"] = reversed_value
            self.gas_label_bard3["text"] = f"Water Level : {reversed_value}%"

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
