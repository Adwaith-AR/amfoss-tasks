#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include <VL53L0X.h>
#include <ESP32Servo.h>

int servotimer = 1;
// Create Servo objects
Servo servo1;
Servo servo2;

// Pin Definitions
const int analogPin = 4;   // GPIO 4 for A0 (Analog Output)
const int digitalPin = 33; // GPIO 33 for D0 (Digital Output)

// WiFi setup
const char *ssid = "KOCHUPARAMBIL";
const char *password = "rakhy1363";

// MQTT setup
const char *mqtt_server = "b37.mqtt.one";
const char *mqtt_user = "89biln7212";
const char *mqtt_password = "5678deghlz";

// Variables for storing incoming message
String msg;

// Create two instances of the VL53L0X sensor
VL53L0X sensor1, sensor2;

WiFiClient espClient;
PubSubClient client(espClient);



// Function to send a message to the server
void sent_msg(const String &msg_to_send) void SentData(int bord_num, String SensorType, float value)
{
          String msg = "bard" + String(bord_num) + " " + String(SensorType) + ": " + String(value);
          client.publish(topic, msg.c_str(), true); // Send data to MQTT broker
}

// Function to handle received messages
void received_msg(const String &msg)
{
          if (msg == "clean")
          {
                    moveservo();
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

void moveservo()
{
          // Sweep both servos together from 0 to 180 degrees
          for (int pos = 0; pos <= 180; pos++)
          {
                    servo1.write(pos);
                    servo2.write(pos); // Move both servos simultaneously
                    delay(15);         // Allow the servos to move
          }

          // Sweep both servos together from 180 to 0 degrees
          for (int pos = 180; pos >= 0; pos--)
          {
                    servo1.write(pos);
                    servo2.write(pos); // Move both servos simultaneously
                    delay(15);         // Allow the servos to move
          }
}

void setup()
{

          servo1.attach(14); // GPIO14
          servo2.attach(15); // GPIO15

          // Set initial positions
          servo1.write(90); // Neutral position
          servo2.write(90); // Neutral position

          // Print initial positions to the Serial Monitor

          pinMode(digitalPin, INPUT); // Setup digital pin

          setup_wifi();
          client.setServer(mqtt_server, 1883);
          client.setCallback(callback);

          Wire.begin(8, 9); // Custom SDA and SCL (GPIO 8, 9)

          // Initialize sensor 1 (Channel 0)
          activateTCA9548A(0); // Activate channel 0 for sensor 1

          if (!sensor1.init())
          {

                    while (1)
                              ; // Halt if sensor 1 fails
          }
          sensor1.startContinuous(); // Start continuous measurement for sensor 1

          // Initialize sensor 2 (Channel 1)
          activateTCA9548A(1); // Activate channel 1 for sensor 2

          if (!sensor2.init())
          {

                    while (1)
                              ; // Halt if sensor 2 fails
          }
          sensor2.startContinuous(); // Start continuous measurement for sensor 2
}

void loop()
{
          if (!client.connected())
          {
                    reconnect();
          }
          client.loop();

          // Read distance from sensor 1
          activateTCA9548A(0); // Activate channel 0 for sensor 1
          uint16_t distance1 = sensor1.readRangeContinuousMillimeters();
          if (sensor1.timeoutOccurred())
          {
          }
          else
          {

                    SentData(1, "water level", distance1); // Send distance to MQTT
          }

          // Read distance from sensor 2
          activateTCA9548A(1); // Activate channel 1 for sensor 2
          uint16_t distance2 = sensor2.readRangeContinuousMillimeters();
          if (sensor2.timeoutOccurred())
          {
          }
          else
          {

                    SentData(1, "water level", distance2); // Send distance to MQTT
          }

          // Read analog and digital values
          int analogValue = analogRead(analogPin);    // Read analog value
          int digitalValue = digitalRead(digitalPin); // Read digital value

          // Send analog value to MQTT

          SentData(1, "analog_methane_level", analogValue);

          // Send digital value to MQTT

          SentData(1, "digital_methane_level", digitalValue);

          delay(1000); // Delay for 1 second before repeating
          servotimer = servotimer + 1;
          if (servotimer == 3)
          {

                    delay(500);
          }
}

// Function to activate a channel on the TCA9548A I2C multiplexer
void activateTCA9548A(uint8_t channel)
{
          Wire.beginTransmission(0x70); // TCA9548A I2C address
          Wire.write(1 << channel);     // Activate the specified channel
          Wire.endTransmission();
}

// Function to scan I2C bus for devices (optional)
void scanI2C()
{
          byte error, address;
          int nDevices;

          nDevices = 0;

          for (address = 1; address < 127; address++)
          {
                    Wire.beginTransmission(address);
                    error = Wire.endTransmission();

                    if (error == 0)
                    {

                              if (address < 16)
                              {
                                        Serial.print("0");
                              }

                              nDevices++;
                    }
          }
}
