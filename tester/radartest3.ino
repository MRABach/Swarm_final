#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11);                     // Serial ports for communications with the radar. RX=10, TX=11
const int sequenceLength = 4;                        // Length of the frame header
uint8_t targetSequence[] = {0xA9, 0xFF, 0x03, 0x00}; // The frame header
uint8_t receivedValues[sequenceLength];              // Array for checking the radar
int currentIndex = 0;                                // Current index in the array

const int targetLength = 8;         // Length of the target arrays
uint8_t firstTarget[targetLength];  // Array for first target
uint8_t secondTarget[targetLength]; // Array for second target
uint8_t thirdTarget[targetLength];  // Array for third target
int byteIndex = 0;                  // Current index in the target arrays
int incomingByte = 0;               // For incoming bytes from the radar

void setup() {
  Serial.begin(250000);   // Open serial communications with PC and wait for port to open
  mySerial.begin(256000); // Open serial communications with radar
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
        Serial.println("Correct header recieved:");
        for (int i = 0; i < sequenceLength; i++) {
          Serial.print(receivedValues[i], HEX);
          Serial.print(" ");
        }

        // Sort the first 8 bytes into the first array and print
        Serial.println("\nFirst target:");
        for (byteIndex; byteIndex < targetLength; byteIndex++) {
          incomingByte = mySerial.read();
          firstTarget[byteIndex] = incomingByte;
          Serial.print(firstTarget[byteIndex], HEX);
          Serial.print(" ");
        }
        byteIndex = 0;  // Reset the index for next iteration

        // Sort the second 8 bytes into the second array and print
        Serial.println("\nSecond target:");
        for (byteIndex; byteIndex < targetLength; byteIndex++) {
          incomingByte = mySerial.read();
          secondTarget[byteIndex] = incomingByte;
          Serial.print(secondTarget[byteIndex], HEX);
          Serial.print(" ");
        }
        byteIndex = 0;  // Reset the index for next iteration

        // Sort the third 8 bytes into the third array and print
        Serial.println("\nThird target:");
        for (byteIndex; byteIndex < targetLength; byteIndex++) {
          incomingByte = mySerial.read();
          thirdTarget[byteIndex] = incomingByte;
          Serial.print(thirdTarget[byteIndex], HEX);
          Serial.print(" ");
        }
        byteIndex = 0;  // Reset the index for next iteration
        
        // Print the two last remaining bytes into 
        Serial.println("\nFrame tail:");
        for (int i = 0; i < 2; i++) {
          incomingByte = mySerial.read();
          Serial.print(incomingByte, HEX);
          Serial.print(" ");
        }
        currentIndex = 0; // Reset the index for next iteration
        Serial.print("\n\n");
      }
    } 
    else {
      // If recieved value doesnt match expected header, reset index and start over
      currentIndex = 0;
    }
  }
}
