const int NUM_PINS = 4;

int pins[] = {2, 3, 4, 5};
int pin_button = 14;  // 버튼 연결 핀
int state = -1, dx = 1;
boolean state_previous = false;  // 버튼의 이전 상태
boolean state_current;           // 버튼의 현재 상태

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < NUM_PINS; ++i) {
    pinMode(pins[i], OUTPUT);
    digitalWrite(pins[i], LOW);
  }
  pinMode(pin_button, INPUT);
}

void loop() {
  state_current = digitalRead(pin_button);  // 버튼 상태 읽기
  if (state_current) {                      // 버튼을 누른 경우
    if (state_previous == false) {          // 이전 상태와 비교
      dx *= -1;
      Serial.print("Button pressed\n");
      state_previous = true;
    }
    // delay(50);  // 디바운싱
  } else {
    state_previous = false;
  }

  state += dx;

  switch (state) {
    case -1:
      state = 3;
      break;
    case 4:
      state = 0;
      break;
  }

  for (int i = 0; i < NUM_PINS; ++i) {
    Serial.print(i == state ? "O " : "X ");
    digitalWrite(pins[i], i == state ? HIGH : LOW);
  }

  Serial.println();
  delay(1000);
}