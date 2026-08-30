#include <WiFi.h>
#include <PubSubClient.h>
#include <ESP32Servo.h>
#include <Arduino.h>

#include "AudioFileSourcePROGMEM.h"
#include "AudioGeneratorWAV.h"
#include "AudioOutputI2SNoDAC.h"

// VIOLA sample taken from https://ccrma.stanford.edu/~jos/pasp/Sound_Examples.html
#include "av.h"
#include "du.h"

Servo main_door;
Servo gate;

AudioGeneratorWAV *wav_adwaith;
AudioGeneratorWAV *wav_durga;
AudioFileSourcePROGMEM *file_adwaith;
AudioFileSourcePROGMEM *file_durga;
AudioOutputI2SNoDAC *out_adwaith;
AudioOutputI2SNoDAC *out_durga;

const int switch_door = 13;
const int kitchen_fan = 27;
const int ac_light = 26;
const int led_red = 18;
const int led_blue = 4;
const int led_green = 5;
const int main_doorPin = 12;
const int gatePin = 14;

bool kitchen_fan_status = false;
bool ac_status = false;
bool main_door_status = false;
bool gate_status = false;

// WiFi setup
const char *ssid = "KOCHUPARAMBIL";
const char *password = "rakhy1363";

// MQTT setup
const char *mqtt_server = "b37.mqtt.one";
const char *mqtt_user = "89biln7212";
const char *mqtt_password = "5678deghlz";

WiFiClient espClient;
PubSubClient client(espClient);

void playSound_adwaith()
{
          // Initialize audio components
          file_adwaith = new AudioFileSourcePROGMEM(adwaith, sizeof(adwaith));

          out_adwaith = new AudioOutputI2SNoDAC();

          out_adwaith->SetGain(1.0); // Set maximum volume

          wav_adwaith = new AudioGeneratorWAV();

          if (wav_adwaith->begin(file_adwaith, out_adwaith))
          {
                    Serial.println("Playing sound...");
                    while (wav_adwaith->isRunning())
                    {
                              if (!wav_adwaith->loop())
                                        wav_adwaith->stop();
                    }
                    Serial.println("Sound playback completed.");
          }
          else
          {
                    Serial.println("Failed to start playback.");
          }

          // Clean up
          delete wav_adwaith;
          delete file_adwaith;
          delete out_adwaith;
}
void playSound_durga()
{
          // Initialize audio components

          file_durga = new AudioFileSourcePROGMEM(durga, sizeof(durga));

          out_durga = new AudioOutputI2SNoDAC();
          out_durga->SetGain(1.0); // Set maximum volume

          wav_durga = new AudioGeneratorWAV();

          if (wav_durga->begin(file_durga, out_durga))
          {
                    Serial.println("Playing sound...");
                    while (wav_durga->isRunning())
                    {
                              if (!wav_durga->loop())

                                        wav_durga->stop();
                    }
                    Serial.println("Sound playback completed.");
          }
          else
          {
                    Serial.println("Failed to start playback.");
          }

          // Clean up
          delete wav_durga;
          delete file_durga;
          delete out_durga;
}

// Function to send a message to the server
void sent_msg(const String &msg_to_send)
{
          client.publish("89biln7212/", msg_to_send.c_str());
}

// Function to handle received messages
void received_msg(const String &msg)
{
          if (msg == "Kitchen_fan")
          {
                    kitchen_fan_status = !kitchen_fan_status;
                    digitalWrite(kitchen_fan, kitchen_fan_status ? HIGH : LOW);
          }
          else if (msg == "livingroom_fan")
          {
                    ac_status = !ac_status;
                    digitalWrite(ac_light, ac_status ? HIGH : LOW);
          }
          else if (msg.indexOf("gate") != -1)
          { // Use indexOf() instead of find()
                    gate_status = !gate_status;
                    gate.write(gate_status ? 0 : 90);
          }
          else if (msg.indexOf("maindoor") != -1)
          {
            if(msg.indexOf("durga") != -1){
               playSound_durga();
               main_door.write(0);
               delay(2000);
               main_door.write(90);
            }
            else if(msg.indexOf("adwaith") != -1){
              playSound_adwaith();
              main_door.write(0);
              delay(2000);
              main_door.write(90);
              }
             else{
            main_door.write(0);
            delay(2000);
            main_door.write(90);
             }  }
          else if (msg.indexOf("rgb") != -1)
          { // Use indexOf() instead of find()
                    String rgb_value = msg;
                    rgb_value.replace("rgb", "");
                    int commaIndex1 = rgb_value.indexOf(',');
                    int commaIndex2 = rgb_value.indexOf(',', commaIndex1 + 1);

                    String rStr = rgb_value.substring(0, commaIndex1);
                    String gStr = rgb_value.substring(commaIndex1 + 1, commaIndex2);
                    String bStr = rgb_value.substring(commaIndex2 + 1);

                    // Convert the color components from String to integers
                    int r = rStr.toInt();
                    int g = gStr.toInt();
                    int b = bStr.toInt();
                    analogWrite(led_red, r);
                    analogWrite(led_green, g);
                    analogWrite(led_blue, b);
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
          Serial.print("Message received: ");
          Serial.println(message);
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

void setup()
{
          Serial.begin(115200);
          pinMode(switch_door, INPUT);
          pinMode(kitchen_fan, OUTPUT);
          pinMode(ac_light, OUTPUT);
          pinMode(led_blue, OUTPUT);
          pinMode(led_green, OUTPUT);
          pinMode(led_red, OUTPUT);
          main_door.attach(main_doorPin);
          gate.attach(gatePin);

          setup_wifi();
          client.setServer(mqtt_server, 1883);
          client.setCallback(callback);
}

void loop()
{
          if (!client.connected())
          {
                    reconnect();
          }
          client.loop();

          if (digitalRead(switch_door) == HIGH)
          {
                    
                    delay(3000);
                    sent_msg("door unlocked");
          }
}
