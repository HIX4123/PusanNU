#include <AM2302-Sensor.h>

// 정상 작동 확인
#define OK 0
#define ERROR -1

// 핀 번호
#define TEMPHUMID_SENSOR_PIN 7
#define MOISTURE_SENSOR_PIN A0
#define FAN1_PIN 10
#define FAN2_PIN 11
#define FAN3_PIN 12

// 토양 수분량 구분
#define DRY 0
#define HUMID 1
#define WET 2

AM2302::AM2302_Sensor am2302{TEMPHUMID_SENSOR_PIN};

int beginTempHumidSensor() {
  am2302.begin();
  return OK;
}

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    yield();
  }
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  beginTempHumidSensor();
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

void debug() {
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.print("Temperature: ");
  Serial.println(Temperature);

  Serial.print("Humidity:    ");
  Serial.println(Humidity);

  Serial.print("Moisture:    ");
  Serial.println(String(Moisture) + " (" + String(analogRead(A0)) + ")");
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
  if (getTempHumid() != OK) {
    Serial.println("Error: Could not get temperature and humidity");
  }
  if (getMoisture() != OK) {
    Serial.println("Error: Could not get moisture");
  }
  debug();
  delay(1000);
}