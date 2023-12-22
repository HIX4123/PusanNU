#include <AM2302-Sensor.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>

#define bluetooth Serial1

// 정상 작동 확인
#define OK 0
#define ERROR -1

// 핀 번호
#define MOISTURE_SENSOR_PIN A0
#define TEMPHUMID_SENSOR_PIN 7
#define FANA1_PIN 8
#define FANA2_PIN 9
#define FANB1_PIN 10
#define FANB2_PIN 11
#define FANC1_PIN 12
#define FANC2_PIN 13

// 토양 수분량 구분
#define DRY 0
#define HUMID 1
#define WET 2

byte degree[8] = {0b00010, 0b00101, 0b00010, 0b00000,  // ° 기호
                  0b00000, 0b00000, 0b00000, 0b00000};
int isAuto = 1;  // 팬 자동 제어 여부

AM2302::AM2302_Sensor am2302{TEMPHUMID_SENSOR_PIN};
LiquidCrystal_I2C lcd(0x27, 16, 3);

int beginTempHumidSensor() {
  am2302.begin();
  return OK;
}

void setupFans() {
  pinMode(FANA1_PIN, OUTPUT);
  pinMode(FANA2_PIN, OUTPUT);
  pinMode(FANB1_PIN, OUTPUT);
  pinMode(FANB2_PIN, OUTPUT);
  pinMode(FANC1_PIN, OUTPUT);
  pinMode(FANC2_PIN, OUTPUT);
  digitalWrite(FANA1_PIN, LOW);
  digitalWrite(FANA2_PIN, LOW);
  digitalWrite(FANB1_PIN, LOW);
  digitalWrite(FANB2_PIN, LOW);
  digitalWrite(FANC1_PIN, LOW);
  digitalWrite(FANC2_PIN, LOW);
}

void setup() {
  Wire.begin();
  Serial.begin(115200);
  bluetooth.begin(9600);
  while (!Serial) {
    yield();
  }
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  setupFans();
  beginTempHumidSensor();

  lcd.init();
  lcd.init();
  lcd.backlight();
  lcd.createChar(0, degree);
}

float Temperature = NULL;
float Humidity = NULL;
int Moisture = NULL;

int getTempHumid() {
  auto status = am2302.read();
  if (status == OK) {
    Temperature = am2302.get_Temperature();
    Humidity = am2302.get_Hunidity();
  } else {
    Serial.print("Error: ");
    Serial.println(status);
    return ERROR;
  }

  return OK;
}

int getMoisture() {
  Moisture = analogRead(MOISTURE_SENSOR_PIN);
  if (0 <= Moisture && Moisture < 300) {
    Moisture = DRY;
    return OK;
  } else if (300 <= Moisture && Moisture < 700) {
    Moisture = HUMID;
    return OK;
  } else if (700 <= Moisture && Moisture <= 950) {
    Moisture = WET;
    return OK;
  }
  return ERROR;
}

void sendBluetoothData() {
  String data = "Temp: ";
  data.concat(Temperature);
  data.concat("°C Humid: ");
  data.concat(Humidity);
  data.concat("% Moist: ");
  switch (Moisture) {
    case DRY:
      data.concat("Dry");
      break;
    case HUMID:
      data.concat("Humid");
      break;
    case WET:
      data.concat("Wet");
      break;
  }
  data.concat(" (");
  data.concat(analogRead(A0));
  data.concat(")");

  bluetooth.print(data);
}

int c;
void recieveBluetoothData() {
  c = bluetooth.read();
  isAuto = 0;
  if (c == 9) {
    isAuto = 1;
  } else if (c == 0) {
    fanOff(1);
    fanOff(2);
    fanOff(3);
  } else if (c == 1) {
    fanOn(1);
    fanOff(2);
    fanOff(3);
  } else if (c == 2) {
    fanOn(1);
    fanOn(2);
    fanOff(3);
  } else if (c == 3) {
    fanOn(1);
    fanOn(2);
    fanOn(3);
  }
}

void printLCD() {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temp : ");
  lcd.print(Temperature);
  lcd.write(0);
  lcd.print("C");
  lcd.setCursor(0, 1);
  lcd.print("Humid: ");
  lcd.print(Humidity);
  lcd.print("%");
  lcd.setCursor(0, 2);
  lcd.print("Moist: ");
  switch (Moisture) {
    case DRY:
      lcd.print("Dry");
      break;
    case HUMID:
      lcd.print("Humid");
      break;
    case WET:
      lcd.print("Wet");
      break;
  }
  lcd.print(" (");
  lcd.print(analogRead(A0));
  lcd.print(")");
  lcd.setCursor(0, 3);
  lcd.print("Power: ");
  if (digitalRead(FANC1_PIN)) {
    lcd.print("3");
  } else if (digitalRead(FANB1_PIN)) {
    lcd.print("2");
  } else if (digitalRead(FANA1_PIN)) {
    lcd.print("1");
  } else {
    lcd.print("0");
  }
  lcd.print(" (");
  lcd.print(isAuto ? "Auto" : "Manual");
  lcd.print(")");
}

void fanOn(int fan) {
  switch (fan) {
    case 1:
      digitalWrite(FANA1_PIN, HIGH);
      digitalWrite(FANA2_PIN, LOW);
      break;
    case 2:
      digitalWrite(FANB1_PIN, HIGH);
      digitalWrite(FANB2_PIN, LOW);
      break;
    case 3:
      digitalWrite(FANC1_PIN, HIGH);
      digitalWrite(FANC2_PIN, LOW);
      break;
  }
}

void fanOff(int fan) {
  switch (fan) {
    case 1:
      digitalWrite(FANA1_PIN, LOW);
      digitalWrite(FANA2_PIN, LOW);
      break;
    case 2:
      digitalWrite(FANB1_PIN, LOW);
      digitalWrite(FANB2_PIN, LOW);
      break;
    case 3:
      digitalWrite(FANC1_PIN, LOW);
      digitalWrite(FANC2_PIN, LOW);
      break;
  }
}

void controlFans() {
  if (!isAuto) {
    return;
  }
  if (Temperature >= 36 || Humidity >= 83) {
    fanOn(1);
    fanOn(2);
    fanOn(3);
  } else if (Temperature >= 33 || Humidity >= 78) {
    fanOn(1);
    fanOn(2);
    fanOff(3);
  } else if (Temperature >= 30 || Humidity >= 75) {
    fanOn(1);
    fanOff(2);
    fanOff(3);
  } else {
    fanOff(1);
    fanOff(2);
    fanOff(3);
  }
}

void debug() {
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println();
  Serial.println("Debugging...");

  Serial.print("Temperature: ");
  Serial.println(Temperature);

  Serial.print("Humidity:    ");
  Serial.println(Humidity);

  Serial.print("Moisture:    ");
  Serial.println(String(Moisture) + " (" + String(analogRead(A0)) + ")");

  Serial.print("Fan A:       ");
  Serial.println(digitalRead(FANA1_PIN));

  Serial.print("Fan B:       ");
  Serial.println(digitalRead(FANB1_PIN));

  Serial.print("Fan C:       ");
  Serial.println(digitalRead(FANC1_PIN));

  Serial.print("Auto Mode:   ");
  Serial.println(isAuto);
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
  if (getTempHumid() != OK) {
    Serial.println("Error: Could not get temperature and humidity");
  }
  if (getMoisture() != OK) {
    Serial.println("Error: Could not get moisture");
  }
  sendBluetoothData();
  if (bluetooth.available()) {
    recieveBluetoothData();
  }
  printLCD();
  controlFans();
  debug();
  delay(1000);
}