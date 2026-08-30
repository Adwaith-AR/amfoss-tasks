#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include <VL53L0X.h>
#include <ESP32Servo.h>

int servotimer=1;
// Create Servo objects
Servo servo1;
Servo servo2;

// Pin Definitions
const int analogPin = 4;   // GPIO 4 for A0 (Analog Output)
const int digitalPin = 33; // GPIO 33 for D0 (Digital Output)

// WiFi Credentials
const char *ssid = "KOCHUPARAMBIL";
const char *password = "rakhy1363";

// MQTT Broker settings
const char *mqtt_broker = "b37.mqtt.one";
const char *topic = "89biln7212/";
const char *mqtt_username = "89biln7212";
const char *mqtt_password = "5678deghlz";
const int mqtt_port = 1883;

// Variables for storing incoming message
String msg;

// Create two instances of the VL53L0X sensor
VL53L0X sensor1, sensor2;

WiFiClient espClient;
PubSubClient client(espClient);

// MQTT callback function for receiving messages
void callback(char *topic, byte *payload, unsigned int length)
{
          msg = "";
          for (int i = 0; i < length; i++)
          {
                    msg += (char)payload[i];
          }
          
}

// Function to connect to the MQTT broker
void connectToMQTT()
{
          while (!client.connected())
          {
                    String client_id = "esp32-client-" + String(WiFi.macAddress());
                    
                    if (client.connect(client_id.c_str(), mqtt_username, mqtt_password))
                    {
                              
                              client.subscribe(topic); // Subscribe to the topic
                    }
                    else
                    {
                              
                              delay(5000); // Retry after 5 seconds
                    }
          }
}

// Function to send data to MQTT broker
void SentData(int bord_num, String SensorType, float value)
{
          String msg = "bard" + String(bord_num) + " " + String(SensorType) + ": " + String(value);
          client.publish(topic, msg.c_str(), true); // Send data to MQTT broker
}
void moveservo(){
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

          
          servo1.attach(14);          // GPIO14
          servo2.attach(15);          // GPIO15

          // Set initial positions
          servo1.write(90); // Neutral position
          servo2.write(90); // Neutral position

          // Print initial positions to the Serial Monitor
          

          pinMode(digitalPin, INPUT); // Setup digital pin

          // Connect to WiFi
          WiFi.begin(ssid, password);
          while (WiFi.status() != WL_CONNECTED)
          {
                    delay(100);
                    
          }
          

          // Setup MQTT
          client.setServer(mqtt_broker, mqtt_port);
          client.setCallback(callback);
          connectToMQTT(); // Connect to MQTT broker

          // Initialize I2C
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
          // Ensure the MQTT client stays connected
          if (!client.connected())
          {
                    pinMode(digitalPin, INPUT); // Setup digital pin      connectToMQTT(); // Reconnect if connection lost
          }

          client.loop(); // Process incoming messages

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
          servotimer=servotimer+1;
          if  (servotimer==3){
                   
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
