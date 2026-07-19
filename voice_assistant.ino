#include <Servo.h>

Servo myServo;
const int LED_PIN = 13; 

void setup() {
  // Start serial communication at 9600 baud rate
  Serial.begin(9600);
  
  // Set up the LED pin
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW); 
  
  // Attach the servo to digital pin 9
  myServo.attach(9);
  myServo.write(0); 
}

void loop() {
  // Check if Python sent a command over the USB cable
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    // If the command is 'Y', trigger the hardware action
    if (command == 'Y') {
      digitalWrite(LED_PIN, HIGH); // Turn LED on
      myServo.write(180);          // Move servo to 180 degrees
      
      delay(3000);                 // Wait for 3 seconds
      
      digitalWrite(LED_PIN, LOW);  // Turn LED off
      myServo.write(0);            // Reset servo back to 0 degrees
    }
  }
}