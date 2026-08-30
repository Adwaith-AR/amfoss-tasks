#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include <VL53L0X.h>

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
          Serial.print("Received message: ");
          Serial.println(msg);
}

// Function to connect to the MQTT broker
void connectToMQTT()
{
          while (!client.connected())
          {
                    String client_id = "esp32-client-" + String(WiFi.macAddress());
                    Serial.print("Attempting MQTT connection...");
                    if (client.connect(client_id.c_str(), mqtt_username, mqtt_password))
                    {
                              Serial.println("Connected to MQTT broker");
                              client.subscribe(topic); // Subscribe to the topic
                    }
                    else
                    {
                              Serial.print("Failed to connect, state: ");
                              Serial.println(client.state());
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

void setup()
{
          Serial.begin(115200);       // Start Serial communication
          pinMode(digitalPin, INPUT); // Setup digital pin

          // Connect to WiFi
          WiFi.begin(ssid, password);
          while (WiFi.status() != WL_CONNECTED)
          {
                    delay(100);
                    Serial.print(".");
          }
          Serial.println("\nConnected to WiFi");

          // Setup MQTT
          client.setServer(mqtt_broker, mqtt_port);
          client.setCallback(callback);
          connectToMQTT(); // Connect to MQTT broker

          // Initialize I2C
          Wire.begin(8, 9); // Custom SDA and SCL (GPIO 8, 9)

          // Initialize sensor 1 (Channel 0)
          activateTCA9548A(0); // Activate channel 0 for sensor 1
          Serial.println("Initializing VL53L0X 1...");
          if (!sensor1.init())
          {
                    Serial.println("Failed to initialize VL53L0X 1!");
                    while (1)
                              ; // Halt if sensor 1 fails
          }
          sensor1.startContinuous(); // Start continuous measurement for sensor 1

          // Initialize sensor 2 (Channel 1)
          activateTCA9548A(1); // Activate channel 1 for sensor 2
          Serial.println("Initializing VL53L0X 2...");
          if (!sensor2.init())
          {
                    Serial.println("Failed to initialize VL53L0X 2!");
                    while (1)
                              ; // Halt if sensor 2 fails
          }
          sensor2.startContinuous(); // Start continuous measurement for sensor 2

          Serial.println("VL53L0X sensors initialized and measuring...");
}

void loop()
{
          // Ensure the MQTT client stays connected
          if (!client.connected())
          {
                    connectToMQTT(); // Reconnect if connection lost
          }

          client.loop(); // Process incoming messages

          // Read distance from sensor 1
          activateTCA9548A(0); // Activate channel 0 for sensor 1
          uint16_t distance1 = sensor1.readRangeContinuousMillimeters();
          if (sensor1.timeoutOccurred())
          {
                    Serial.println("Sensor 1 timeout!");
          }
          else
          {
                    Serial.print("Sensor 1 Distance: ");
                    Serial.print(distance1);
                    Serial.println(" mm");
                    SentData(1, "water level", distance1); // Send distance to MQTT
          }

          // Read distance from sensor 2
          activateTCA9548A(1); // Activate channel 1 for sensor 2
          uint16_t distance2 = sensor2.readRangeContinuousMillimeters();
          if (sensor2.timeoutOccurred())
          {
                    Serial.println("Sensor 2 timeout!");
          }
          else
          {
                    Serial.print("Sensor 2 Distance: ");
                    Serial.print(distance2);
                    Serial.println(" mm");
                    SentData(1, "water level", distance2); // Send distance to MQTT
          }

          // Read analog and digital values
          int analogValue = analogRead(analogPin);    // Read analog value
          int digitalValue = digitalRead(digitalPin); // Read digital value

          // Send analog value to MQTT
          Serial.print("Analog Value: ");
          Serial.println(analogValue);
          SentData(1, "analog_methane_level", analogValue);

          // Send digital value to MQTT
          Serial.print("Digital Value: ");
          Serial.println(digitalValue);
          SentData(1, "digital_methane_level", digitalValue);

          delay(1000); // Delay for 1 second before repeating
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

          Serial.println("Scanning I2C bus...");
          nDevices = 0;

          for (address = 1; address < 127; address++)
          {
                    Wire.beginTransmission(address);
                    error = Wire.endTransmission();

                    if (error == 0)
                    {
                              Serial.print("I2C device found at address 0x");
                              if (address < 16)
                              {
                                        Serial.print("0");
                              }
                              Serial.println(address, HEX);
                              nDevices++;
                    }
          }

          if (nDevices == 0)
          {
                    Serial.println("No I2C devices found!");
          }
          else
          {
                    Serial.println("Scan completed!");
          }
}
