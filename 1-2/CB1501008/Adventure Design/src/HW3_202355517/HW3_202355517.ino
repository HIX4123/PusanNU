const int NUM_PINS = 4;

int pins[] = {2, 3, 4, 5};
int state = 0, dx = 1;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < NUM_PINS; ++i) {
    pinMode(pins[i], OUTPUT);
    digitalWrite(pins[i], LOW);
  }
}

void loop() {
  state += dx;

  if (state == 0 || state == 3) {
    dx = -dx;
  }

  for (int i = 0; i < NUM_PINS; ++i) {
    Serial.print(i <= state ? "O " : "X ");
    digitalWrite(pins[i], i <= state ? HIGH : LOW);
  }

  Serial.println();
  delay(1000);
}