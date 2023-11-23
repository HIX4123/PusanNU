void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);
}
void loop() {
  if (Serial1.available()) {  // Serial1 포트에서 데이터 수신 여부 확인
    String temperature =
        Serial1.readStringUntil('\n');  // 개행 문자가 나올 때까지 문자열 읽기
    Serial.print("Current Temperature: ");
    Serial.println(temperature);  // PC로 온도값 전송 (디버깅 용도)
  }
}