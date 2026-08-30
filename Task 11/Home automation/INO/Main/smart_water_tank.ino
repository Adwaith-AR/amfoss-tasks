#include <Arduino.h>

// Define the pins connected to the ultrasonic sensor and other components

const int pump = 4;

const int trigPin = 7;
const int echoPin = 8;




void setup()
{
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(pump, OUTPUT);
  
}

void loop()
{
  // Ultrasonic sensor logic
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  double duration = pulseIn(echoPin, HIGH);
  double distance = duration * 0.034 / 2;

  // Pump control logic
  if (distance < 3)
  {
    digitalWrite(pump, LOW);
  }
  else if (distance >= 8)
  {
    digitalWrite(pump, HIGH);
  }

  

  delay(200);
}