#include <ESP8266WiFi.h>

WiFiClient client;
String url;
String str="";
char c;
boolean enable_log = false;

String ssid = "raspi-webgui";
String mdp = "ChangeMe";
String server = "10.3.141.1";

int port = 8000;

void setup() {
  Serial.begin(4800);
  WiFi.begin(ssid, mdp);
  if (enable_log) { Serial.print("Connecting"); }
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
     if (enable_log) { Serial.print("."); }
  }
   if (enable_log) { Serial.println(); }
   if (enable_log) { Serial.print("Connected, IP address: "); }
   if (enable_log) { Serial.println(WiFi.localIP()); }
}

void loop() {
  
  if (Serial.available()) {
    
    c = Serial.read();
    
    if ( c == '\n' ) {
      if (!client.connect(server, port)) {
         if (enable_log) { Serial.println("Connection failed"); }
        return;
      }

      // Exemple url: "/api/trames?content=\$INZDA,163119,14,06,2008,-05,00*74";
      url = "/api/trames?content="+str;
      client.print(String("POST ") + url + " HTTP/1.1\r\n" + "Host: "+server+"\r\n" + "Connection: close\r\n\r\n");
      str="";
       
    } else {
      str += c;
    }
     
  }
}  
