int pins[] = {2, 3, 4, 5};
int values[] = {0, 63, 127, 191};

void setup() {
  for (int i = 0; i < 4; ++i) {
    pinMode(pins[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i < 4; ++i) {
    analogWrite(pins[i], values[i]);
    values[i] = (values[i] + 1) % 256;
  }
  delay(10);
}