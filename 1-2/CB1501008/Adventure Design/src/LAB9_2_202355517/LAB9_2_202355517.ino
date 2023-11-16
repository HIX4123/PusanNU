int Enable1 = 38; //모터 1
int PWM1 = 9;
int DIR1 = 39;

int Enable2 = 40; //모터 2
int PWM2 = 10;
int DIR2 = 41;

void setup() {
  pinMode(Enable1, OUTPUT);
  digitalWrite(Enable1, HIGH);
  pinMode(PWM1, OUTPUT);
  pinMode(DIR1, OUTPUT);
  pinMode(Enable2, OUTPUT);
  digitalWrite(Enable2, HIGH);
  pinMode(PWM2, OUTPUT);
  pinMode(DIR2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int reading = analogRead(A0);
  int speed = map(reading, 0, 1023, -255, 255);
  if (speed > 0) {
    digitalWrite(DIR1, HIGH);  // 정방향 회전
    int pwm_value = 255 - speed;
    analogWrite(PWM1, pwm_value);
    Serial.print(String("Reading : ") + reading);
    Serial.println(String(", Clockwise : ") + speed);
  } else {
    digitalWrite(DIR1, LOW);  // 역방향 회전
    int pwm_value = abs(speed);
    analogWrite(PWM1, pwm_value);
    Serial.print(String("Reading : ") + reading);
    Serial.println(String(", Anti-clockwise : ") + pwm_value);
  }
  delay(1000);
}
