const int PWM = 9;
const int DIR = 39;
const int ENABLE = 38;  // 모터 1
const int buttonPin = 14;
void setup() {
  pinMode(ENABLE, OUTPUT);
  digitalWrite(ENABLE, HIGH);
  pinMode(PWM, OUTPUT);
  pinMode(DIR, OUTPUT);
  pinMode(buttonPin, INPUT);
}

boolean statePrev = false;
boolean stateNow = false;
unsigned int rotateRate[3] = {255, 127, 0};
unsigned int rotateRateIndex = 0;
void loop() {
  if (digitalRead(buttonPin)) {  // 버튼을 누른 경우
    if (statePrev == false) {    // 이전 상태와 비교
      statePrev = true;
      rotateRateIndex = (rotateRateIndex + 1) % 3;
    }
    delay(50);
  } else {
    statePrev = false;
  }

  digitalWrite(DIR, HIGH);
  analogWrite(PWM, rotateRate[rotateRateIndex]);
}
