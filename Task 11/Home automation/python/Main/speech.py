import speech_recognition as sr
import paho.mqtt.client as mqttclient
import time
import cv2
import face_recognition
def send_message(message):

    try:
        client.publish("89biln7212/", message)
        print(f"Message sent to topic : {message}")
    except Exception as e:
        print(f"Failed to send message: {e}")


def on_connect(client, userdata, flags, rc):
    global connected
    if rc == 0:
        print("Connected")
        connected = True
        client.subscribe("89biln7212/")  # Subscribe after connection
    else:
        print("Not connected")

def on_message(client, userdata, message):
    msg=str(message.payload.decode('utf-8'))
   
   

connected = False

broker_address = "b37.mqtt.one"
port = 1883
user = "89biln7212"
password = "5678deghlz"

client = mqttclient.Client(client_id="89biln7212", protocol=mqttclient.MQTTv311)  # Specify the protocol version
client.username_pw_set(user, password=password)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port=port)

client.loop_start()

# Replace '0' with the correct index if necessary
recognizer = sr.Recognizer()
mic_index = 2
while True:
    with sr.Microphone(mic_index) as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Please say something...")
        audio = recognizer.listen(source)

        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        command=command.lower()
        print("You said: " + command)
        if "door" in command:
            send_message('maindoor')
        elif "gate" in command:
            send_message('gate')
        elif 'ac' in command:
            send_message("livingroom_fan")
        



