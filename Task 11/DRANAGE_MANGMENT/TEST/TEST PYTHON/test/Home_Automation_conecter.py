import paho.mqtt.client as mqttclient
import time

def send_message(message):

    try:
        client.publish("89biln7212/", message)
        print(f"Message sent to topic : {message}")
    except Exception as e:
        print(f"Failed to send message: {e}")


    
   

def reseve_msg(msg):
    
    print (msg)




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
   
    reseve_msg(msg)

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

# Wait for connection
while not connected:
    time.sleep(0.2)

# Keep the script running to receive messages indefinitely
try:
    while True:
        time.sleep(0.1)  # Keep the main thread alive
except KeyboardInterrupt:
    print("Interrupted by user")

client.loop_stop()
client.disconnect()  # Clean disconnection
