#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include <VL53L0X.h>
// bard1 water level:
//  WiFi credentials
const char *ssid = "mi";
const char *password = "N@123456";

// MQTT Broker settings
const char *mqtt_broker = "b37.mqtt.one";
const char *topic = "89biln7212/";
const char *mqtt_username = "89biln7212";
const char *mqtt_password = "5678deghlz";
const int mqtt_port = 1883;

// Variables for storing incoming message

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
}
void sent_msg(msg){
          client.publish(topic, msg.c_str(),true);
}

void loop()
{

          sent_msg("bard1 water level: 230");
              sent_msg("bard1 obstacles: 230");
                  sent_msg("bard1 gas: 230");
                      sent_msg("bard2 water level: 230");
                          sent_msg("bard2 obstacles: 230");
                              sent_msg("bard2 gas: 230");
                                  sent_msg("bard3 water level: 230");
                                      sent_msg("bard3 obstacles: 230");
                                          sent_msg("bard3 gas: 230");
                                              delay(1000); // Delay between readings
          sent_msg("bard1 water level: 30");
              sent_msg("bard1 obstacles: 30");
                  sent_msg("bard1 gas: 30");
                      sent_msg("bard2 water level: 30");
                          sent_msg("bard2 obstacles: 30");
                              sent_msg("bard2 gas: 30");
                                  sent_msg("bard3 water level: 30");
                                      sent_msg("bard3 obstacles: 30");
                                          sent_msg("bard3 gas: 30");
                                          delay(1000); // Delay between readings
}

// Function to activate a channel on the TCA9548A I2C multiplexer
