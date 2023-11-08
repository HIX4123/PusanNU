void setup() {
  Serial.begin(9600);  // 시리얼 포트 초기화
}

void loop() {
  int state = 1;
  char buffer[128];
  int i = 0;
  String str[5];
  while (true) {
    if (state == 1) {
      Serial.print("Enter a String --> ");
      state = 2;
    }
    while (Serial.available()) {
      int len = Serial.readBytesUntil('\n', buffer, 127);
      if (len > 0) {
        buffer[len] = '\0';
        str[i] = String(buffer);
        Serial.println(str[i]);
        state = 1;
        ++i;
        break;
      }
    }
    if (i == 5) {
      i = 0;
      break;
    }
  }

  // 문자열 정렬
  for (int i = 0; i < 4; i++) {
    for (int j = i + 1; j < 5; j++) {
      int compare = str[i].compareTo(str[j]);
      if (compare > 0) {  // 오름차순으로 정렬
        String temp = str[i];
        str[i] = str[j];
        str[j] = temp;
      }
    }
  }
  // 정렬된 문자열 출력3
  Serial.println("After Sorting");
  for (int i = 0; i < 5; i++) {
    Serial.println(String(i) + " : " + str[i]);
  }
}