import paho.mqtt.client as mqttclient
import time
import cv2
import face_recognition
import os
import numpy as np

# ---------- LOAD MULTIPLE REFERENCE IMAGES ----------
reference_dir = "Current Work/HOME AUTOMATION/python/Test/references/"
known_face_encodings = []
known_face_names = []

print("📁 Loading reference images...")

for filename in os.listdir(reference_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        path = os.path.join(reference_dir, filename)
        try:
            image = face_recognition.load_image_file(path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                encoding = encodings[0]
                name = os.path.splitext(filename)[0]
                known_face_encodings.append(encoding)
                known_face_names.append(name)
                print(f"✅ Loaded: {name}")
            else:
                print(f"⚠️ No face found in {filename}")
        except Exception as e:
            print(f"❌ Error loading {filename}: {e}")

print(f"Total references loaded: {len(known_face_names)}\n")

# ---------- MQTT SETUP ----------
def send_message(message):
    try:
        client.publish("89biln7212/", message)
        print(f"📤 Message sent: {message}")
    except Exception as e:
        print(f"❌ Failed to send message: {e}")

# ---------- FACE RECOGNITION FUNCTION ----------
def initiate_face_recognition():
    print("🧠 Starting optimized face recognition...")
    cap = cv2.VideoCapture(2)

    if not cap.isOpened():
        print("❌ Error: Could not access webcam.")
        return

    face_detected = False
    frame_count = 0

    try:
        while not face_detected:
            ret, frame = cap.read()
            if not ret:
                print("❌ Error reading frame.")
                break

            frame_count += 1
            # Skip some frames to maintain speed
            if frame_count % 3 != 0:
                cv2.imshow("Smart Face Recognition", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                continue

            # --- LIGHT ENHANCEMENT (FAST VERSION) ---
            yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
            yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
            enhanced_frame = cv2.cvtColor(yuv, cv2.COLOR_YUV2RGB)

            # --- DOWNSCALE FOR SPEED ---
            small_frame = cv2.resize(enhanced_frame, (0, 0), fx=0.5, fy=0.5)

            # --- FACE DETECTION (FAST HOG MODEL) ---
            face_locations = face_recognition.face_locations(small_frame, model="hog")
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)

            for face_encoding, face_location in zip(face_encodings, face_locations):
                # --- HIGH ACCURACY MATCH ---
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.45)
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

                if len(face_distances) > 0:
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                        print(f"✅ Match found: {name}")
                        send_message(f"maindoor,{name}")
                        face_detected = True
                        break

            # --- DISPLAY ---
            cv2.imshow("Smart Face Recognition", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("🛑 Exiting manually.")
                break

        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"⚠️ Error during recognition: {e}")

# ---------- MQTT CALLBACKS ----------
def receive_msg(msg):
    print(f"📩 Received message: {msg}")
    if msg.lower() == "door unlocked":
        initiate_face_recognition()
    if "true" in msg:
        send_message("alarm")



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

# ---------- MAIN SETUP ----------
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



