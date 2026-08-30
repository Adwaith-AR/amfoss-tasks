#include <ESP32Servo.h>

// Create Servo objects
Servo servo1;
Servo servo2;

void setup()
{
          // Start serial communication
          Serial.begin(115200); // Set baud rate for serial communication

          // Attach servos to pins
          servo1.attach(14); // GPIO14
          servo2.attach(15); // GPIO15

          // Set initial positions
          servo1.write(90); // Neutral position
          servo2.write(90); // Neutral position

          // Print initial positions to the Serial Monitor
          Serial.println("Servos are at initial positions: 90 degrees");
}

void loop()
{
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

          // Wait for 10 seconds after one full cycle
          delay(10000); // 10000 milliseconds = 10 seconds
          Serial.println("Cycle complete, waiting for 10 seconds...");
}