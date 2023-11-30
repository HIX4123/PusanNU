const int TRIG_PIN = 2;
const int ECHO_PIN = 3;
const int MOTION_PIN = 8;

const int LED1_PIN = 11;
const int LED2_PIN = 12;

void setup() {
  Serial.begin(9600);
  pinMode(ECHO_PIN, INPUT);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(MOTION_PIN, INPUT);
}

int led1Bright = 0;

void detectMotion(int motion) {
  if (motion == 1) {
    Serial.println("Motion detected");
    digitalWrite(LED2_PIN, HIGH);
  } else {
    digitalWrite(LED2_PIN, LOW);
  }
}

void measureDistance() {
  digitalWrite(TRIG_PIN, HIGH);
  delay(10);
  digitalWrite(TRIG_PIN, LOW);
  // Reads the ECHO_PIN, returns the sound wave travel time in microseconds
  float duration = pulseIn(ECHO_PIN, HIGH);
  float distance = duration * 340 / 10000 / 2;
  Serial.println(String("Distance(cm): ") + distance);
  delay(500);
  if (distance > 100) {
    led1Bright = 0;
  } else {
    led1Bright = map(distance, 100, 0, 0, 255);
  }
  Serial.println(led1Bright);
  analogWrite(LED1_PIN, led1Bright);
}

void loop() {
  int motion = digitalRead(MOTION_PIN);
  detectMotion(motion);
  measureDistance();
}