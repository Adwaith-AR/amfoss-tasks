const int analogPin = 0;   // GPIO 4 for A0 (Analog Output)
const int digitalPin = 33; // GPIO 33 for D0 (Digital Output)

void setup()
{
  Serial.begin(115200);
  pinMode(digitalPin, INPUT);
}

void loop()
{
  int analogValue = analogRead(analogPin);    // Read the analog value from A0
  int digitalValue = digitalRead(digitalPin); // Read the digital value from D0

  Serial.print("Analog Value: ");
  Serial.println(analogValue);

  Serial.print("Digital Value: ");
  Serial.println(digitalValue);

  delay(1000); // Wait for 1 second before repeating
}