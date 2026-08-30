#include <Arduino.h>

// Define the pins connected to the ultrasonic sensor and other components
const int lightSensorPin = 2;
const int light = 3;
const int Alarm = 5;
const int Alarm2 = 6;
const int IR = 7;
const int Flame = 9;
const int stare_light = 10;
const int gas_sensor = A0;

void setup()
{

  pinMode(lightSensorPin, INPUT);
  pinMode(IR, INPUT);
  pinMode(gas_sensor,INPUT);
  pinMode(Flame, INPUT);
  pinMode(Alarm, OUTPUT);
  pinMode(light, OUTPUT);
  pinMode(stare_light, OUTPUT);
}

void loop()
{

  if(digitalRead(lightSensorPin)==HIGH){
    digitalWrite(light,HIGH);
  }
  else{
    digitalWrite(light,LOW);
   }

  // Flame sensor and alarm control logic
  if (digitalRead(Flame) == LOW)
  {
    for (int i = 0; i <= 255; i++)
    {
      analogWrite(Alarm, i);
      analogWrite(Alarm2, i);
      delay(5);
    }
    for (int i = 255; i >= 0; i--)
    {
      analogWrite(Alarm, i);
      analogWrite(Alarm2, i);
      delay(5);
    }
  }
  else
  {
    digitalWrite(Alarm, LOW);
    digitalWrite(Alarm2, LOW);
  }

  // IR sensors and person count logic
  if (digitalRead(IR) == LOW)
  {

    // Stair light control based on person count
    digitalWrite(stare_light, HIGH);
    delay(5000);
    digitalWrite(stare_light, LOW);


  }
  if (analogRead(gas_sensor)>340){
    for (int i = 0; i <= 255; i++)
    {
      analogWrite(Alarm, i);
      analogWrite(Alarm2, i);
      delay(5);
    }
    for (int i = 255; i >= 0; i--)
    {
      analogWrite(Alarm, i);
      analogWrite(Alarm2, i);
      delay(5);
    }
  }
  else
  {
    digitalWrite(Alarm, LOW);
    digitalWrite(Alarm2, LOW);
  }

    delay(200);
}