int pin_LEDs[] = {2, 3};  // LED 연결 핀
unsigned long time_previous[2], time_current;
unsigned long intervals[] = {1000, 1000};  // 점멸 간격
boolean LED_state[2] = {false};                 // LED

void setup() {
  pinMode(A0, INPUT);
  for (int i = 0; i < 2; ++i) {
    pinMode(pin_LEDs[i], OUTPUT);
    digitalWrite(pin_LEDs[i], LED_state[i]);
  }
  Serial.begin(9600);
  for (int i = 0; i < 2; ++i) {
    time_previous[i] = millis();  // 현재 시간
  }
}

void loop() {
  time_current = millis();
  // Serial.print("Current interval is ");
  // Serial.print(intervals[0]);
  // Serial.print(", ");
  // Serial.print(intervals[1]);
  // Serial.print(" ms.   ");
  // Serial.print("Current time is ");
  // Serial.print(time_current - time_previous[0]);
  // Serial.print(", ");
  // Serial.print(time_current - time_previous[1]);
  // Serial.println(" ms.");
  for (int i = 0; i < 2; ++i) {
    if (time_current - time_previous[i] >= intervals[i]) {
      time_previous[i] = time_current;  // 시작 시간 갱신
      LED_state[i] = !LED_state[i];           // LED 반전
      digitalWrite(pin_LEDs[i], LED_state[i]);
    }
  }
  int adc = analogRead(A0);                     // 가변저항 읽기
  intervals[0] = map(adc, 0, 1023, 500, 1500);  // 점멸 간격으로 변환
  intervals[1] = map(adc, 0, 1023, 1500, 500);  // 점멸 간격으로 변환
}