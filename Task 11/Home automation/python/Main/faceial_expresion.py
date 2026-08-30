import cv2
from deepface import DeepFace
import time
import pyfirmata 
import paho.mqtt.client as mqttclient
import time
import cv2
import face_recognition
import os
import numpy as np




def send_message(message):
    try:
        client.publish("89biln7212/", message)
        print(f"📤 Message sent: {message}")
    except Exception as e:
        print(f"❌ Failed to send message: {e}")
def receive_msg(msg):
    print(f"📩 Received message: {msg}")
    
        

def on_connect(client, userdata, flags, rc):
    global connected
    if rc == 0:
        print("🔗 Connected to MQTT Broker")
        connected = True
        client.subscribe("89biln7212/")
    else:
        print(f"❌ Failed to connect, return code: {rc}")

def on_message(client, userdata, message):
    msg = str(message.payload.decode('utf-8'))
    receive_msg(msg)

def light(mood):
    if mood == 'happy':
       send_message("rgb,255,100,139")
    elif  mood == 'angry':
        send_message("rgb 220,20,60")
    elif mood =='sad':
        send_message("rgb 54,100,139")

    else:
        send_message("rgb 255,255,255")
connected = False
broker_address = "b37.mqtt.one"
port = 1883
user = "89biln7212"
password = "5678deghlz"

client = mqttclient.Client(client_id="89biln7212", protocol=mqttclient.MQTTv311)
client.username_pw_set(user, password=password)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port=port)

client.loop_start()


# Load the Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start capturing video from the default webcam
cap = cv2.VideoCapture(2)

# Set the desired frame rate (e.g., 10 FPS)
desired_fps = 60
frame_time = 1 / desired_fps


while True:
    start_time = time.time()  # Start time for frame processing

    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame for faster processing
    frame = cv2.resize(frame, (640, 480))  # Adjust size as needed

    frame = cv2.flip(frame, 1)

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Process every second frame to reduce load
    if len(faces) > 0:
        # Analyze only the first detected face for speed
        (x, y, w, h) = faces[0]
        face_roi = frame[y:y + h, x:x + w]

        # Predict emotions using the pre-trained model
        preds = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

        # Get the dominant emotion
        emotion = preds[0]['dominant_emotion']
        print(emotion)
        light(emotion)
        

        # Draw a rectangle around the face and label it with the predicted emotion
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Real-time Emotion Detection', frame)

    # Calculate processing time and adjust for frame rate
    elapsed_time = time.time() - start_time
    if elapsed_time < frame_time:
        time.sleep(frame_time - elapsed_time)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# ---------- MAIN SETUP ----------

while not connected:
    time.sleep(0.2)

print("✅ System ready — waiting for MQTT trigger ('door unlocked')...\n")

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("🧹 Interrupted by user — disconnecting...")

client.loop_stop()
client.disconnect()
print("🔌 Disconnected cleanly.")

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()


