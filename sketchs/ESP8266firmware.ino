#include <ESP8266WiFi.h>

WiFiClient client;
String url;
String str="";
char c;

void setup() {
  Serial.begin(4800);
  WiFi.begin("BRILLARD24", "lmdpaecbrillard#");
  // Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    // Serial.print(".");
  }
  // Serial.println();
  // Serial.print("Connected, IP address: ");
  // Serial.println(WiFi.localIP());
}

void loop() {
  
  if (Serial.available()) {
    
    c = Serial.read();
    
    if ( c == '\n' ) {
      if (!client.connect("192.168.33.98", 8000)) {
        // Serial.println("Connection failed");
        return;
      }

      // Exemple url: "/api/trames?content=\$INZDA,163119,14,06,2008,-05,00*74";
      url = "/api/trames?content="+str;
      client.print(String("POST ") + url + " HTTP/1.1\r\n" + "Host: 192.168.33.98\r\n" + "Connection: close\r\n\r\n");
      str="";
       
    } else {
      str += c;
    }
     
  }
}  
