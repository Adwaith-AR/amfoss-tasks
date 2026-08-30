#include <WiFi.h>
#include <PubSubClient.h>
#include <ESP32Servo.h>




Servo main_door;
Servo gate;



const int switch_door = 13;
const int kitchen_fan = 27;
const int ac_light = 26;
const int led_red = 18;
const int led_blue = 4;
const int led_green = 5;
const int main_doorPin = 12;
const int gatePin = 14;
const int alaram = 23;

bool kitchen_fan_status = false;
bool ac_status = false;
bool main_door_status = false;
bool gate_status = false;
bool light_status = false;

// WiFi setup
const char *ssid = "KOCH";
const char *password = "1234556789";

// MQTT setup
const char *mqtt_server = "b37.mqtt.one";
const char *mqtt_user = "89biln7212";
const char *mqtt_password = "5678deghlz";

WiFiClient espClient;
PubSubClient client(espClient);



// Function to send a message to the server
void sent_msg(const String &msg_to_send)
{
          client.publish("89biln7212/", msg_to_send.c_str());
}

// Function to handle received messages
void received_msg(const String &msg)
{
          if (msg == "Kitchen_fan")
          {
                    kitchen_fan_status = !kitchen_fan_status;
                    digitalWrite(kitchen_fan, kitchen_fan_status ? HIGH : LOW);
          }
          else if (msg == "livingroom_fan")
          {
                    ac_status = !ac_status;
                    digitalWrite(ac_light, ac_status ? HIGH : LOW);
          }
         
          else if (msg == "bedroomlight")
          {
             light_status = !light_status;
             digitalWrite(led_red, light_status ? HIGH : LOW);
             digitalWrite(led_green, light_status ? HIGH : LOW);
             digitalWrite(led_blue, light_status ? HIGH : LOW);
                    }
          else if (msg.indexOf("gate") != -1)
          { // Use indexOf() instead of find()
                    gate_status = !gate_status;
                    gate.write(gate_status ? 0 : 90);
          }
          else if (msg.indexOf("true") != -1)
          { // Use indexOf() instead of find()
             digitalWrite(alaram, LOW);
             delay(1000);
             digitalWrite(alaram, HIGH);
             delay(1000);
          }

          else if (msg.indexOf("maindoor") != -1)
             {
                if (msg.indexOf("durga") != -1)
                {

                   main_door.write(0);
                   delay(2000);
                   main_door.write(90);
                }
                else if (msg.indexOf("adwaith") != -1)
                {

                   main_door.write(0);
                   delay(2000);
                   main_door.write(90);
                }
                else
                {
                   main_door.write(0);
                   delay(2000);
                   main_door.write(90);
                }
             }
          else if (msg.indexOf("rgb") != -1)
          { // Use indexOf() instead of find()
                    String rgb_value = msg;
                    rgb_value.replace("rgb", "");
                    int commaIndex1 = rgb_value.indexOf(',');
                    int commaIndex2 = rgb_value.indexOf(',', commaIndex1 + 1);

                    String rStr = rgb_value.substring(0, commaIndex1);
                    String gStr = rgb_value.substring(commaIndex1 + 1, commaIndex2);
                    String bStr = rgb_value.substring(commaIndex2 + 1);

                    // Convert the color components from String to integers
                    int r = rStr.toInt();
                    int g = gStr.toInt();
                    int b = bStr.toInt();
                    analogWrite(led_red, r);
                    analogWrite(led_green, g);
                    analogWrite(led_blue, b);
          }
}

void setup_wifi()
{
          delay(10);
          Serial.println("Connecting to WiFi...");
          WiFi.begin(ssid, password);

          while (WiFi.status() != WL_CONNECTED)
          {
                    delay(500);
                    Serial.print(".");
          }
          Serial.println("\nWiFi connected");
}

void callback(char *topic, byte *payload, unsigned int length)
{
          String message;
          for (int i = 0; i < length; i++)
          {
                    message += (char)payload[i];
          }
          Serial.print("Message received: ");
          Serial.println(message);
          received_msg(message); // Pass the message to the handler
}

void reconnect()
{
          while (!client.connected())
          {
                    Serial.print("Attempting MQTT connection...");
                    if (client.connect("ESP32Client", mqtt_user, mqtt_password))
                    {
                              Serial.println("connected");
                              sent_msg("ESP32 connected");
                              client.subscribe("89biln7212/");
                    }
                    else
                    {
                              Serial.print("failed, rc=");
                              Serial.print(client.state());
                              Serial.println(" try again in 5 seconds");
                              delay(5000);
                    }
          }
}

void setup()
{
          Serial.begin(115200);
          pinMode(switch_door, INPUT);
          pinMode(kitchen_fan, OUTPUT);
          pinMode(ac_light, OUTPUT);
          pinMode(led_blue, OUTPUT);
          pinMode(led_green, OUTPUT);
          pinMode(led_red, OUTPUT);
          pinMode(alaram, OUTPUT);
          main_door.attach(main_doorPin);
          gate.attach(gatePin);

          digitalWrite(alaram, HIGH);
          setup_wifi();
          client.setServer(mqtt_server, 1883);
          client.setCallback(callback);
}

void loop()
{
          if (!client.connected())
          {
                    reconnect();
          }
          client.loop();

          if (digitalRead(switch_door) == HIGH)
          {
                    
                    delay(3000);
                    sent_msg("door unlocked");
          }
}
