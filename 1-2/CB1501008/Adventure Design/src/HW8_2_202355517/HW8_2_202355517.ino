#include <LiquidCrystal.h>

LiquidCrystal lcd(44, 45, 46, 47, 48, 49);

void readTemperature() { return analogRead(A1); }

int readIlluminance() { return analogRead(A2); }

void setup() {
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.write('TEMPERATURE:');
  lcd.setCursor(0, 1);
  lcd.write('ILLUMINANCE:');
}

void loop() {
  lcd.setCursor(13, 0);
  lcd.print(String(readTemperature()));
  lcd.setCursor(13, 1);
  lcd.print(String(readIlluminance()));
  delay(1000);
}