#include <SoftwareSerial.h>

SoftwareSerial ESP8266(10, 11);

String NomduReseauWifi = "BRILLARD24"; 
String MotDePasse      = "lmdpaecbrillard#"; 


void sendToESP8266(String commande)
{  
  ESP8266.println(commande);
}

void receiveFromESP8266(const int timeout)
{
  String reponse = "";
  long int time = millis();
  while( (time+timeout) > millis())
  {
    while(ESP8266.available())
    {
      char c = ESP8266.read();
      reponse+=c;
    }
  }
  Serial.print(reponse);   
}

/****************************************************************/
/*                             INIT                             */
/****************************************************************/
void setup()
{

  // Set bitrate speed of serial interfaces
  Serial.begin(9600);
  ESP8266.begin(9600);
  
  Serial.println("######## Init output");
  pinMode(13,OUTPUT); // LED temoin init
  pinMode(8,OUTPUT);

  // Set status of hard reset
  digitalWrite(13, HIGH);
  
  Serial.println("######## Hard reset of ESP8266");
  digitalWrite(8, LOW);
  delay(5000);
  digitalWrite(8, HIGH);
  delay(5000);

  // Set status of hard rese
  digitalWrite(13, LOW);
  
  initESP8266();
}

/****************************************************************/
/*                        BOUCLE INFINIE                        */
/****************************************************************/
void loop() {
  Serial.println("######## Set connexion to host");
  sendToESP8266("AT+CIPSTART=\"TCP\",\"192.168.33.101\",80");
  receiveFromESP8266(500);
  Serial.println("######## HTTP Call");
  String request = "GET /api/id.php HTTP/1.0\r\n";
  request       += "Host: 192.168.33.101\r\n";
  sendToESP8266("AT+CIPSEND="+String(request.length()+2));
  receiveFromESP8266(500);
  sendToESP8266(request);
  receiveFromESP8266(500);
}

/****************************************************************/
/*                Fonction qui initialise l'ESP8266             */
/****************************************************************/
void initESP8266() {  

  Serial.println("######## Starting");
  Serial.println("######## Soft reset of ESP8266");
  sendToESP8266("AT+RST"); 
  receiveFromESP8266(2000);
  Serial.println("####### Set mode as client");
  sendToESP8266("AT+CWMODE=3");
  receiveFromESP8266(5000);
  Serial.println("######## Connextion to wifi");
  sendToESP8266("AT+CWJAP=\""+ NomduReseauWifi + "\",\"" + MotDePasse +"\"");
  receiveFromESP8266(5000);
  Serial.println("######## Get IP adress");
  sendToESP8266("AT+CIFSR");
  receiveFromESP8266(5000);
  Serial.println("######## Set one connexion managed");
  sendToESP8266("AT+CIPMUX=0");
  receiveFromESP8266(5000);
}
