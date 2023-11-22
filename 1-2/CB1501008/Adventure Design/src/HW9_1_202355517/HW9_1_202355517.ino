#include <Servo.h>
Servo myServo;

int servoPin = 11;
int servoAngle = 0;
int servoAngleDelta = 10;
int buttonPin[2] = {14, 15};

void setup() {
  myServo.attach(servoPin);
  for (int i = 0; i < 2; i++) {
    pinMode(buttonPin[i], INPUT);
  }
}

int timeprev = millis();

void checkButton() {
  servoAngleDelta = digitalRead(buttonPin[0]) == HIGH ? 10 : servoAngleDelta;
  servoAngleDelta = digitalRead(buttonPin[1]) == HIGH ? -10 : servoAngleDelta;
}

void limitAngle() {
  servoAngle = servoAngle > 180 ? 180 : (servoAngle < 0 ? 0 : servoAngle);
}

void loop() {
  checkButton();
  int timenow = millis();
  if (timenow - timeprev > 1000) {
    servoAngle += servoAngleDelta;
    limitAngle();
    myServo.write(servoAngle);
    timeprev = timenow;
  }
}