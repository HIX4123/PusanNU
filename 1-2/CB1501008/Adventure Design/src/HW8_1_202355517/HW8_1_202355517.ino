
const int BUTTON_PIN = 14;
const int NUM_PATTERN[] = {0xFC, 0x60, 0xDA, 0xF2, 0x66,
                           0xB6, 0xBE, 0xE4, 0xFE, 0xE6};
const int DIGIT_PIN[] = {66, 67, 68, 69};
const int SEGMENT_PIN[] = {58, 59, 60, 61, 62, 63, 64, 65};
const int SEGMENT_DELAY = 5;

void initPins() {
  for (int i = 0; i < 4; i++) {
    pinMode(DIGIT_PIN[i], OUTPUT);
  }
  for (int i = 0; i < 8; i++) {
    pinMode(SEGMENT_PIN[i], OUTPUT);
  }
}

// 해당 자리에 숫자 하나를 표시하는 함수
void show_digit(int pos, int number) {  // (위치, 출력할 숫자)
  for (int i = 0; i < 4; i++) {
    if (i + 1 == pos)  // 해당 자릿수의 선택 핀만 LOW로 설정
      digitalWrite(DIGIT_PIN[i], LOW);
    else  // 나머지 자리는 HIGH로 설정
      digitalWrite(DIGIT_PIN[i], HIGH);
  }
  for (int i = 0; i < 8; i++) {
    boolean on_off = bitRead(NUM_PATTERN[number], 7 - i);
    digitalWrite(SEGMENT_PIN[i], on_off);
  }
}

void show_3_digit(int number) {
  number = number % 1000;
  int hundreads = number / 100;  // 백 자리
  number = number % 100;
  int tens = number / 10;  // 십 자리
  int ones = number % 10;  // 일 자리
  show_digit(1, hundreads);
  delay(SEGMENT_DELAY);
  show_digit(2, tens);
  delay(SEGMENT_DELAY);
  show_digit(3, ones);
  delay(SEGMENT_DELAY);
}

int time_previous, time_current;
void setup() {
  initPins();
  time_previous = millis();
  Serial.begin(9600);
  Serial.println("Hello World");
}

boolean toggle_button = false;
int number = 0;
void loop() {
  boolean state_previous = false;
  String strnum = String(number);

  if (digitalRead(BUTTON_PIN)) {
    if (state_previous == false) {
      toggle_button = !toggle_button;
      state_previous = true;
    }
  } else {
    state_previous = false;
  }

  time_current = millis();
  if (time_current - time_previous >= 1000) {
    if (toggle_button == false) {
      number++;
    } else {
      number--;
    }
    if (number == 1000) number = 0;
    if (number == -1) number = 999;
    time_previous = time_current;
  }
  show_3_digit(number);
}
