# $\text{Adventure Design Final Summary}$

---

## 스피커; OUTPUT

![스피커 사진](image.png)

- PWM 신호를 사용하여 단음 재생
- 50% duty cycle
  - duty cycle : PWM 신호에서 high level이 차지하는 비율

```ino
tone(핀, 주파수, /*지속시간*/); // AnalogWrite()는 주파수 조절 불가
delay(지속시간);
noTone(핀);
```

[`pitches.h`](https://github.com/codebendercc/arduino-library-files/blob/master/examples/02.Digital/toneMelody/pitches.h) : 주파수를 정의한 헤더 파일

- 용례: `NOTE_C4` `NOTE_ES5`

---

## 온도 센서; INPUT

![온도 센서](image-1.png)

- `analogRead(핀)` : 0~1023
- $\rightarrow$ $V$: `map(analogRead(핀), 0, 1023, 0, 5);`
- $\rightarrow$ $\degree C$: `map(analogRead(핀), 0, 1023, 0, 500);`
- $\rightarrow$ $\degree F$: `map(analogRead(핀), 0, 1023, 32, 932);`
  - $\degree F = \dfrac{9}{5}\degree C + 32$

---

## 조도 센서; INPUT

![조도 센서](image-2.png)

### CdS(황화 카드뮴) 셀

- $광량 \propto \dfrac{1}{저항}$
- 저렴하고 간단
- 느리고 부정확

## 7세그먼트; OUTPUT

![7세그먼트](image-3.png)

- Anode: 위아래 VCC, LOW에 ON
- Cathode: 위아래 GND, HIGH에 ON
- 0babcdefg. 시계방향, 가운데 순서

### 4자리 7세그먼트

![4자리 7세그먼트](image-4.png)

- 주황색: 자릿수 선택 핀
- 파란색: 세그먼트 선택 핀

- 잔상 효과로 12개의 핀을 사용(원래는 10개)

```ino
// 숫자 0~9
byte patterns[] = {
  0xFC, 0x60, 0xDA, 0xF2, 0x66, // 0, 1, 2, 3, 4
  0xB6, 0xBE, 0xE4, 0xFE, 0xE6, // 5, 6, 7, 8, 9
}
// 자릿수 선택 핀
int digit_select_pin[] = {66, 67, 68, 69};
// 세그먼트 선택 핀
in segment_pin[] = {58, 59, 60, 61, 62, 63, 64, 65};

// 한 자릿수 표시
void show_digit(int pos, int number) {
  // 자릿수 선택
  for (int i = 0; i < 4; i++) {
    digitalWrite(digit_select_pin[i], !(i == pos));
  }
  // 세그먼트 선택
  for (int i = 0; i < 8; i++) {
    digitalWrite(segment_pin[i], bitRead(patterns[number], 7 - i));
  }
}

// 4자리 표시
void show_4_digit(int number) {
  int digit[4];
  for (int i = 0; i < 4; i++) {
    digit[i] = number % 10;
    number /= 10;
  }
  for (int i = 0; i < 4; i++) {
    show_digit(i, digit[i]);
    delay(5);
  }
}
```

- `millis()`를 이용해야 함
  - `delay()`를 사용하면 잔상 효과를 얻지 못함

---

## LCD; OUTPUT

![LCD](image-5.png)

- 저전력

`LiquidCrystal.h` 라이브러리 사용

```ino
#include <LiquidCrystal.h>

LiquidCrystal lcd(핀1, 핀2, 핀3, 핀4, 핀5, 핀6);

// 커스텀 문자(5×8)
byte customCh[] = {
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000
};

lcd.createChar(커스텀 문자 번호, customCh);
lcd.write(byte(커스텀 문자 번호));

void setup() {
  lcd.begin(열개수, 행개수);
}

lcd.write('문자');
lcd.print("문자열");
lcd.setCursor(열(0~15), 행(0~1));
lcd.clear();
```

### 구조

![LCD 구조](image-6.png)

- 패널 + 컨트롤러 = 모듈
- 데이터 버스를 통해 컨트롤러에 명령 전달 $\rightarrow$ 컨트롤러가 패널에 명령 전달
- DDRAM: 텍스트 표시 영역
- CGRAM: 커스텀 문자 저장 영역
- CGROM: 기본 문자 저장 영역
- 컨트롤러: 컨트롤러
- Power 회로: 전원 회로

## 서보 모터; OUTPUT

![Alt text](image-7.png)

- 50Hz PWM 신호: 20ms 주기
  - 1ms(5%) ~ 2ms(10%) duty cycle

`Servo.h` 라이브러리 사용

```ino
#include <Servo.h>

Servo servo;

// setup()
servo.attach(핀);

// loop()
servo.write(각도);
```

- 최대 제어 가능 서보모터 수
  - Arduino Uno: 12개
  - Arduino Mega: 48개

## DC 모터; OUTPUT

- 최초의 모터
- VCC, GND 두 개 만으로 전류 방향을 바꿔서 회전 방향을 바꿈
- PWM 신호를 사용하여 속도 제어
- 문제점
  - 결선 후 회전 방향을 바꿀 수 없음
    - H-bridge 회로를 사용하여 해결
      ![H-브리지 회로](image-8.png)
  - 전력돼지새끼
  - 전용 드라이버가 필요함
    - L293D 모터 드라이버 칩

### L293D 모터 드라이버 칩

![L293D 모터 드라이버 칩](image-9.png)

|L293D 핀(왼쪽↓)|L293D 핀(오른쪽↑)|모터 핀|
|---|---|---|
|EN1|EN2|모터 활성화|
|IN1|IN3|속도 제어|
|OUT1|OUT3|모터 연결|
|GND, GND|GND, GND|GND|
|OUT2|OUT4|모터 연결|
|IN2|IN4|방향 제어|
|V~MOTOR~||모터 전원|
||VCC|칩 전원|

![Alt text](image-10.png)

```ino
const int ENABLE = 38;
const int PWM = 9;
const int DIR = 39;

void setup() {
  pinMode(ENABLE, OUTPUT);
  pinMode(PWM, OUTPUT);
  pinMode(DIR, OUTPUT);

  digitalWrite(ENABLE, HIGH);
}

void loop() {
  digitalWrite(DIR, HIGH);
  analogWrite(PWM, 255); // -255 ~ 255
  delay(1000);
}
```

## 스텝 모터; OUTPUT

하나의 펄스가 주어지면 분할각 단위로 회전

##UART