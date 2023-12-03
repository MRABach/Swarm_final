#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // Serial ports for communications with the radar. RX=10, TX=11
int incomingByte = 0;            // For incoming bytes from the radar
const int sequenceLength = 4;    // Length of the frame header
uint8_t targetSequence[] = {0xA9, 0xFF, 0x03, 0x00}; // The frame header
uint8_t receivedValues[sequenceLength];   // Array for checking the radar
int currentIndex = 0;   // Current index in the array

void setup() {
  Serial.begin(250000);     // Open serial communications with PC
  mySerial.begin(256000);   // Open serial communications with radar
}

void loop() {
  if (mySerial.available()) {
    // Read the byte recieved by the serial port
    uint8_t receivedValue = mySerial.read();  

    // Check if recieved value matches the expected frame header
    if (receivedValue == targetSequence[currentIndex]) {
      receivedValues[currentIndex] = receivedValue;
      currentIndex++;

      // If the whole frame is recieved
      if (currentIndex == sequenceLength) {
        // Print the header
        Serial.print("Correct header recieved: ");
        for (int i = 0; i < sequenceLength; i++) {
          Serial.print(receivedValues[i], HEX);
          Serial.print(" ");
        }
        Serial.println();
        // Print the following bytes (26 bytes between the following header)
        for (int i = 0; i < 26; i++) {
            incomingByte = mySerial.read();
            Serial.print(incomingByte, HEX);
            Serial.print(" ");
        }
        Serial.print("\n\n");
        currentIndex = 0;   // Reset the index for next iteration
      }
    } else {
      // If recieved value doesnt match expected header, reset index and start over
      currentIndex = 0;
    }
  }
}
