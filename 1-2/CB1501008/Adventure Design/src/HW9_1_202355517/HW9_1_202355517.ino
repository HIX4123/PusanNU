#include <Servo.h>
Servo myServo;
int servoPin = 11;

void setup() {
  myServo.attach(servoPin);  // 서보 모터 연결
}
void loop() {
  myServo.write(180);
  while (1)
    ;
}
