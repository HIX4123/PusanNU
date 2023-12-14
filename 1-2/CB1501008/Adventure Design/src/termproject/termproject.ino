/*
 *	AM2302-Sensor_Example.ino
 *
 *	Author: Frank Häfele
 *	Date:	21.11.2023
 *
 *	Object: Measure Sensor Data of AM2302-Sensor with Arduino IDE
 */

#include <AM2302-Sensor.h>

AM2302::AM2302_Sensor am2302{20};

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    yield();
  }
  Serial.print(F("\n >>> AM2302-Sensor_Example <<<\n\n"));

  // put your setup code here, to run once:
  // set Pin
  am2302.begin();
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH);
  auto status = am2302.read();
  Serial.print("\n\nstatus of sensor read(): ");
  Serial.println(status);

  Serial.print("Temperature: ");
  float temp = am2302.get_Temperature();
  Serial.println(temp);

  Serial.print("Humidity:    ");
  Serial.println(am2302.get_Hunidity());
  digitalWrite(LED_BUILTIN, LOW);
  delay(5000);
}