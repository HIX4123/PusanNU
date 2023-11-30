#include <ADXL345.h>
#include <Wire.h>

const int LED_TAP_PIN = 2;
const int LED_ACTIVITY_PIN = 3;

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

int tapFlag = 0, activityFlag = 0, prevActivityState = 0;
int toggleTapCount = 0, toggleActivityCount = 0;

void handleTap(byte interrupts) {
  if (adxl.triggered(interrupts, ADXL345_SINGLE_TAP)) {
    Serial.print("tap ");
    tapFlag = !tapFlag;
    digitalWrite(LED_TAP_PIN, tapFlag);
    toggleTapCount++;
    Serial.print("toggleTapCount: ");
    Serial.println(toggleTapCount);
  }
}

void handleActivity(byte interrupts) {
  if (adxl.triggered(interrupts, ADXL345_ACTIVITY)) {
    Serial.print("activity ");
    if (!prevActivityState) {
      activityFlag = !activityFlag;
      toggleActivityCount++;
    }
    prevActivityState = 1;
    digitalWrite(LED_ACTIVITY_PIN, activityFlag);
    Serial.print("toggleActivityCount: ");
    Serial.print(toggleActivityCount);
  } else {
    prevActivityState = 0;
  }
}

void printInterrupts(byte interrupts) {
  handleTap(interrupts);
  if (adxl.triggered(interrupts, ADXL345_DOUBLE_TAP)) Serial.print("double tap ");
  if (adxl.triggered(interrupts, ADXL345_FREE_FALL)) Serial.print("freefall ");
  if (adxl.triggered(interrupts, ADXL345_INACTIVITY)) Serial.print("inactivity ");
  handleActivity(interrupts);
  Serial.println();
}

void setup() {
  Serial.begin(9600);
  pinMode(LED_TAP_PIN, OUTPUT);
  pinMode(LED_ACTIVITY_PIN, OUTPUT);
  setupADXL();
}

void loop() {
  byte interrupts = adxl.getInterruptSource();
  printInterrupts(interrupts);

  delay(500);
}