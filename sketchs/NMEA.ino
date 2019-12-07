
#include <SoftwareSerial.h>

SoftwareSerial gps(2, 3); // RX, TX
char c;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(9600);
  
  gps.begin(4800);
  Serial.println("NMEA Multiplexer…Test Montage");
}

// the loop function runs over and over again forever
void loop() {
   if (gps.available()) {
    c = gps.read();
    if ( c == '\n' ) {
      Serial.println('X');
    } else {
      Serial.print(c);
    }
   }
}
