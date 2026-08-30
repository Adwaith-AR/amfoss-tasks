#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include <VL53L0X.h>

// WiFi credentials
const char *ssid = "mi";
const char *password = "N@123456";

// MQTT Broker settings
const char *mqtt_broker = "broker.hivemq.com";//b37.mqtt.one
    const char *topic = "89biln7212/";
const char *mqtt_username = "89biln7212";
const char *mqtt_password = "5678deghlz";
const int mqtt_port = 1883;

// Variables for storing incoming message
String msg;

VL53L0X sensor1, sensor2; // Removed sensor3
#define TCA9548A_ADDRESS 0x70

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
                    if (client.connect(client_id.c_str(), mqtt_username, mqtt_password))
                    {
                              Serial.println("Connected to MQTT broker");
                              client.subscribe(topic);
                    }
                    else
                    {
                              Serial.print("Failed to connect, state: ");
                              Serial.println(client.state());
                              delay(500); // Short delay before retrying
                    }
          }
}

void setup()
{
          Serial.begin(115200); // Use a higher baud rate for faster serial communication

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
          connectToMQTT();

          Wire.begin(8, 9); // Use custom SDA and SCL (GPIO 8, 9)

          // Scan I2C bus for devices
          scanI2C();

          // Initialize sensor 1 on channel 0
          activateTCA9548A(0); // Activate channel 0 for sensor 1
          Serial.println("Initializing VL53L0X 1...");
          if (!sensor1.init())
          {
                    Serial.println("Failed to initialize VL53L0X 1!");
                    while (1)
                              ; // Halt the program if sensor 1 fails to initialize
          }
          sensor1.startContinuous(); // Start continuous measurement for sensor 1
          Serial.println("VL53L0X 1 initialized successfully.");

          // Initialize sensor 2 on channel 1
          activateTCA9548A(1); // Activate channel 1 for sensor 2
          Serial.println("Initializing VL53L0X 2...");
          if (!sensor2.init())
          {
                    Serial.println("Failed to initialize VL53L0X 2!");
                    while (1)
                              ; // Halt the program if sensor 2 fails to initialize
          }
          sensor2.startContinuous(); // Start continuous measurement for sensor 2
}

void loop()
{
          // Ensure the MQTT client stays connected
          if (!client.connected())
          {
                    connectToMQTT();
          }

          // Process any incoming MQTT messages
          client.loop();

          // Read distance from sensor 1
          activateTCA9548A(0); // Activate channel 0 for sensor 1
          uint16_t distance1 = sensor1.readRangeContinuousMillimeters();
          if (sensor1.timeoutOccurred())
          {
                    Serial.println("Sensor 1 timeout!");
          }
          else
          {
                    String distanceStr1 = "bard1 water level: " + String(distance1); // Corrected variable name
                    client.publish(topic, distanceStr1.c_str(), true);               // Publish distance as a const char*
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
                    String distanceStr2 = "bard1 obstacles: " + String(distance2); // Corrected variable name
                    client.publish(topic, distanceStr2.c_str(), true);
          }

          delay(50); // Delay between readings
}

// Function to activate a channel on the TCA9548A I2C multiplexer
void activateTCA9548A(uint8_t channel)
{
          Wire.beginTransmission(TCA9548A_ADDRESS);
          Wire.write(1 << channel); // Activate specified channel (0-7)
          Wire.endTransmission();
}

// Function to scan I2C bus for connected devices
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