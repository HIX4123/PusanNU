#include <SoftwareSerial.h>
    SoftwareSerial mySerial(4, 5);
const int tempSensorPin = A0;  // 온도 센서 핀 설정 (A0)

void setup() {
  Serial.begin(9600);  // Serial1을 사용하여 9600 baud로 통신 시작
  mySerial.begin(9600);
  pinMode(tempSensorPin, INPUT);
}

void loop() {
  int sensorValue = analogRead(tempSensorPin);  // 온도 센서에서 값을 읽음
  float voltage = sensorValue * 5.0 / 1024.0;  // 아날로그 값을 전압으로 변환
  float temperature = voltage * 100.0;  // LM35는 10mV/°C의 출력을 가짐
  Serial.print(voltage);
  Serial.print(" V :");
  Serial.print(temperature);  // 온도값을 시리얼로 전송
  Serial.print('\n');  // 문자열의 끝을 나타내기 위한 개행 문자 전송
  mySerial.print(temperature);  // 온도값을 시리얼로 전송
  mySerial.print('\n');  // 문자열의 끝을 나타내기 위한 개행 문자 전송
  delay(1000);           // 1초 대기
}