// 1번
/*
주어진 소스코드를 완성하여 각 줄 앞에 줄 번호가 표시된 소스코드를 표시하는
프로그램을 작성합니다.

줄 번호 출력 FSF로 "%2D"를 사용합니다.


소스 코드 파일의 이름(경로 포함)은 파일명이 가리키는 문자열로 제공됩니다.

"data/stdint-wrap.h"를 사용하여 대상 파일의 내용을 확인할 수 있습니다.
*/

#include <stdio.h>

int main(void) {
  char *filename = "data/stdint-wrap.h";
  FILE *fp = NULL;
  char buf[256];
  int line_number = 1;

  fp = fopen(filename, "r");
  for (int i = 1; fgets(buf, 256, fp) != NULL; i++) printf("%2d : %s", i, buf);
        fclose(fp);

        return 0;
}
