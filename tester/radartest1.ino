#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // Serial ports for communications with the radar. RX=10, TX=11
int incomingByte = 0;            // For incoming bytes from the radar

void setup() {
  Serial.begin(9600);          // Open serial communications with PC
  mySerial.begin(256000);        // Open serial communications with radar
}

void loop() {
  // reply only when you receive data:
  if (mySerial.available() > 0) {
    incomingByte = mySerial.read();     // Read the incoming byte
    Serial.print(incomingByte, HEX);    // Print the incoming byte
    Serial.print(" ");
  }
}