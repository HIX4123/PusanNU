#include <ADXL345.h>
#include <Wire.h>

ADXL345 adxl;  // variable adxl is an instance of the ADXL345 library

void setupADXL() {
  adxl.powerOn();
  adxl.setActivityThreshold(75);
  adxl.setInactivityThreshold(75);
  adxl.setTimeInactivity(10);
  adxl.setActivityX(1);
  adxl.setActivityY(1);
  adxl.setActivityZ(1);
  adxl.setInactivityX(1);
  adxl.setInactivityY(1);
  adxl.setInactivityZ(1);
  adxl.setTapDetectionOnX(0);
  adxl.setTapDetectionOnY(0);
  adxl.setTapDetectionOnZ(1);
  adxl.setTapThreshold(50);
  adxl.setTapDuration(15);
  adxl.setDoubleTapLatency(80);
  adxl.setDoubleTapWindow(200);
  adxl.setFreeFallThreshold(7);
  adxl.setFreeFallDuration(45);
  adxl.setInterruptMapping(ADXL345_INT_SINGLE_TAP_BIT, ADXL345_INT1_PIN);
  adxl.setInterruptMapping(ADXL345_INT_DOUBLE_TAP_BIT, ADXL345_INT1_PIN);
  adxl.setInterruptMapping(ADXL345_INT_FREE_FALL_BIT, ADXL345_INT1_PIN);
  adxl.setInterruptMapping(ADXL345_INT_ACTIVITY_BIT, ADXL345_INT1_PIN);
  adxl.setInterruptMapping(ADXL345_INT_INACTIVITY_BIT, ADXL345_INT1_PIN);
  adxl.setInterrupt(ADXL345_INT_SINGLE_TAP_BIT, 1);
  adxl.setInterrupt(ADXL345_INT_DOUBLE_TAP_BIT, 1);
  adxl.setInterrupt(ADXL345_INT_FREE_FALL_BIT, 1);
  adxl.setInterrupt(ADXL345_INT_ACTIVITY_BIT, 1);
  adxl.setInterrupt(ADXL345_INT_INACTIVITY_BIT, 1);
}

void printXYZ(int x, int y, int z) {
  Serial.print("values of X , Y , Z: ");
  Serial.print(x);
  Serial.print(" , ");
  Serial.print(y);
  Serial.print(" , ");
  Serial.println(z);
}

void printAcceleration(double ax, double ay, double az) {
  Serial.print("X=");
  Serial.print(ax);
  Serial.println(" g");
  Serial.print("Y=");
  Serial.print(ay);
  Serial.println(" g");
  Serial.print("Z=");
  Serial.print(az);
  Serial.println(" g");
  Serial.println("**********************");
}

void printInterrupts(byte interrupts) {
  if (adxl.triggered(interrupts, ADXL345_SINGLE_TAP)) Serial.print("tap ");
  if (adxl.triggered(interrupts, ADXL345_DOUBLE_TAP))
    Serial.print("double tap ");
  if (adxl.triggered(interrupts, ADXL345_FREE_FALL)) Serial.print("freefall ");
  if (adxl.triggered(interrupts, ADXL345_INACTIVITY))
    Serial.print("inactivity ");
  if (adxl.triggered(interrupts, ADXL345_ACTIVITY)) Serial.print("activity ");
  Serial.println();
}

void setup() {
  Serial.begin(9600);
  setupADXL();
}

void loop() {
  int x, y, z;
  adxl.readXYZ(&x, &y, &z);
  printXYZ(x, y, z);

  byte interrupts = adxl.getInterruptSource();
  printInterrupts(interrupts);

  double xyz[3];
  adxl.getAcceleration(xyz);
  printAcceleration(xyz[0], xyz[1], xyz[2]);

  delay(500);
}