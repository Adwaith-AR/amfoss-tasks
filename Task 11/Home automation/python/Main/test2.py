import cv2
import numpy as np
import time
import threading
import mediapipe as mp
import paho.mqtt.client as mqttclient
from collections import deque

# ---------- MQTT CONFIG ----------
temp = 0
sleep=0
broker_address = "b37.mqtt.one"
port = 1883
user = "89biln7212"
password = "5678deghlz"
topic = "89biln7212/"
connected = False
running = True

# ---------- MQTT FUNCTIONS ----------
def send_message(message):
    try:
        if connected:
            client.publish(topic, message)
            print(f"📤 Sent: {message}")
    except Exception as e:
        print(f"❌ MQTT send failed: {e}")

def receive_msg(msg):
    global temp
    msg = msg.strip()
    if "true" in msg:
        msg = msg.replace(" true", "")
        temp = float(msg)
        print(f"Received temperature: {temp}")
    elif "false" in msg:
        msg = msg.replace(" false", "")
        temp = float(msg)
        print(f"Received temperature: {temp}")

def on_connect(client, userdata, flags, rc):
    global connected
    if rc == 0:
        connected = True
        print("🔗 Connected to MQTT broker")
        client.subscribe(topic)
    else:
        print(f"❌ MQTT connection failed (code {rc})")

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    receive_msg(msg)

def on_disconnect(client, userdata, rc):
    global connected
    connected = False
    print("🔌 Disconnected from MQTT broker.")

# ---------- MQTT CLIENT SETUP ----------
client = mqttclient.Client(client_id="89biln7212", protocol=mqttclient.MQTTv311)
client.username_pw_set(user, password=password)
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect(broker_address, port)
client.loop_start()

while not connected:
    time.sleep(0.1)

print("✅ MQTT Connected & Listening...\n")

# ---------- CAMERA THREAD ----------
class VideoStream:
    def __init__(self, src=0):
        self.cap = cv2.VideoCapture(src)
        if not self.cap.isOpened():
            raise IOError(f"❌ Cannot open camera at index {src}")

        # Optimize for speed
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        self.frame = None
        self.running = True
        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

    def update(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                self.frame = frame

    def read(self):
        return self.frame

    def stop(self):
        self.running = False
        self.thread.join()
        self.cap.release()

# ---------- CAMERA AUTO-DETECTION ----------
camera_index = None
for i in range(3):
    test_cap = cv2.VideoCapture(2)
    if test_cap.isOpened():
        camera_index = 2
        test_cap.release()
        print(f"📷 Using camera index: {i}")
        break
    test_cap.release()

if camera_index is None:
    print("❌ No working camera found.")
    client.loop_stop()
    client.disconnect()
    exit()

stream = VideoStream(camera_index)

# ---------- MEDIAPIPE FACE TRACKER ----------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

prev_center = None
last_time = time.time()
smoothed_rate = 0.0

SMOOTH_FACTOR = 0.3
MIN_MOVE_THRESHOLD = 3
MAX_VALID_RATE = 300.0

print("🎥 Stable MediaPipe Face Movement Tracker Running... Press 'q' to exit.\n")

try:
    while running:
        frame = stream.read()
        if frame is None:
            continue

        h, w = frame.shape[:2]
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:
            # Use nose tip (landmark 1) as stable face reference point
            face_landmarks = results.multi_face_landmarks[0].landmark
            nose = face_landmarks[1]
            cx, cy = int(nose.x * w), int(nose.y * h)

            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

            if prev_center is not None:
                dx = cx - prev_center[0]
                dy = cy - prev_center[1]
                dist = np.sqrt(dx ** 2 + dy ** 2)

                if dist < MIN_MOVE_THRESHOLD:
                    continue

                dt = time.time() - last_time
                if dt > 0:
                    raw_rate = dist / dt
                    if raw_rate < MAX_VALID_RATE:
                        smoothed_rate = (SMOOTH_FACTOR * raw_rate) + ((1 - SMOOTH_FACTOR) * smoothed_rate)
                        # Color control logic
                        if smoothed_rate > 120 or int(temp) >= 34:
                            sleep=sleep+1
                            if sleep>50:
                                
                              send_message("rgb255,0,0")
                              if sleep>100:
                                sleep=0
                        else:
                            send_message("rgb0,0,255")

            prev_center = (cx, cy)
            last_time = time.time()

        cv2.putText(frame, f"Rate: {smoothed_rate:.2f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        cv2.imshow("MediaPipe Face Tracker", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            running = False
            break

except KeyboardInterrupt:
    running = False
    print("\n🧹 Interrupted by user.")

finally:
    stream.stop()
    face_mesh.close()
    cv2.destroyAllWindows()
    if connected:
        client.loop_stop()
        client.disconnect()
    print("🔌 Disconnected cleanly.")
