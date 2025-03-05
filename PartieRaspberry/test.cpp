#include <WiFi.h>  // Pour ESP32 (si ESP8266, inclure <ESP8266WiFi.h>)

const char* ssid = "TON_SSID";       // Remplace par le nom de ton WiFi
const char* password = "TON_MOT_DE_PASSE"; // Remplace par le mot de passe

void setup() {
    Serial.begin(115200);
    Serial.println("Connexion au WiFi...");
    
    WiFi.mode(WIFI_STA);  // Mode station (client)
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.print(".");
    }

    Serial.println("\nWiFi connecté !");
    Serial.print("Adresse IP : ");
    Serial.println(WiFi.localIP()); 
}

void loop() {
    // Ton code principal ici
}
