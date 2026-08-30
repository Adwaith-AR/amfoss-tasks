#include <Wire.h>
#include <VL53L0X.h>

// Create two instances of the VL53L0X sensor
VL53L0X sensor1, sensor2;

// Function to activate a channel on the TCA9548A I2C multiplexer
void activateTCA9548A(uint8_t channel)
{
          Wire.beginTransmission(0x70); // TCA9548A I2C address
          Wire.write(1 << channel);     // Activate specified channel (0-7)
          Wire.endTransmission();
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
}

void loop()
{
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