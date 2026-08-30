#include <Wire.h>
#include <VL53L0X.h>
#include <ESP32Servo.h> // Make sure to include this library
#include <WiFi.h>
#include <PubSubClient.h>

// Declare the servo objects
Servo servo1;
Servo servo2;

int BoardNumber = 1;

int servo_timer = 0;

const int analogPin = 4;   // GPIO 4 for A0 (Analog Output)
const int digitalPin = 33; // GPIO 33 for D0 (Digital Output)

// Create two instances of the VL53L0X sensor
VL53L0X sensor1, sensor2;

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
WiFiClient espClient;
PubSubClient client(espClient); // Initialize MQTT client

// Function to activate a channel on the TCA9548A I2C multiplexer
void activateTCA9548A(uint8_t channel)
{
          Wire.beginTransmission(0x70); // TCA9548A I2C address
          Wire.write(1 << channel);     // Activate specified channel (0-7)
          Wire.endTransmission();
}

void SentData(int bord_num, String SensorType, float value)
{
          String msg = "bard" + String(bord_num) + " " + String(SensorType) + ": " + String(value); // Corrected variable name
          client.publish(topic, msg.c_str(), true);
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

// Function to scan I2C bus for devices
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

void setup()
{
          WiFi.begin(ssid, password);
          while (WiFi.status() != WL_CONNECTED)
          {
                    delay(100);
                    Serial.print(".");
          }
          Serial.println("\nConnected to WiFi");

          // Setup MQTT
          client.setServer(mqtt_broker, mqtt_port);
          connectToMQTT();

          // Attach servos to pins
          servo1.attach(14); // GPIO14
          servo2.attach(15); // GPIO15

          // Set initial positions
          servo1.write(90); // Neutral position
          servo2.write(90); // Neutral position

          // Print initial positions to the Serial Monitor
          Serial.println("Servos are at initial positions: 90 degrees");

          // Declaring gas sensor
          pinMode(digitalPin, INPUT);

          Serial.begin(115200); // Use a higher baud rate for faster serial communication

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
          Serial.println("VL53L0X 2 initialized successfully.");

          Serial.println("VL53L0X sensors initialized and measuring...");
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
                    Serial.print("Sensor 1 Distance: ");
                    Serial.print(distance1);
                    Serial.println(" mm");
                    SentData(BoardNumber, "water level", distance1);
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
                    SentData(BoardNumber, "water level", distance2);
          }

          delay(50);                                  // Delay between readings
          int analogValue = analogRead(analogPin);    // Read the analog value from A0
          int digitalValue = digitalRead(digitalPin); // Read the digital value from D0

          Serial.print("Analog Value: ");
          Serial.println(analogValue);
          SentData(BoardNumber, "analog_methane_level", analogValue);

          Serial.print("Digital Value: ");
          Serial.println(digitalValue);
          SentData(BoardNumber, "digital_methane_level", digitalValue);

          delay(1000); // Wait for 1 second before repeating

          
} // End of loop function
void RotateMoter(){
          servo_timer = servo_timer + 1;
          if (servo_timer == 10)
          {
                    // Sweep both servos together from 0 to 180 degrees

                    // Sweep both servos together from 0 to 180 degrees

                    // Sweep both servos together from 0 to 180 degrees
                    for (int pos = 0; pos <= 180; pos++)
                    {
                              servo1.write(pos);
                              servo2.write(pos); // Move both servos simultaneously
                              delay(15);         // Allow the servos to move
                              Serial.print("Servo 1 Position: ");
                              Serial.print(pos);
                              Serial.print("  |  Servo 2 Position: ");
                              Serial.println(pos);
                    }

                    // Sweep both servos together from 180 to 0 degrees
                    for (int pos = 180; pos >= 0; pos--)
                    {
                              servo1.write(pos);
                              servo2.write(pos); // Move both servos simultaneously
                              delay(15);         // Allow the servos to move
                              Serial.print("Servo 1 Position: ");
                              Serial.print(pos);
                              Serial.print("  |  Servo 2 Position: ");
                              Serial.println(pos);
                    }

                    // Reset the servo_timer
                    servo_timer = 0;
          }
}