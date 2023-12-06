// 2번
/*
표준 라이브러리 함수인 fseek(), ftell()을 활용하여 파일의 크기를 구하는
프로그램을 작성하라. 대상 파일의 이름은 명령어 인자로 전달된다.

파일 크기를 출력하려면 다음 코드를 참조하세요.

printf("file %s size : %d\n", argv[1], filesize);

명령어 인자가 없으면 아래와 같이 사용법을 출력하여야 한다.

Usage : fsize <file>

이 문제에서 main() 함수를 종료할 때는 "return 0"를 사용하라. "exit(1)" 또는
"return 1" 등은 원치 않는 결과를 발생시킬 수 있다.

각 테스트케이스에서 입력을 해당 테스트케이스의 명령어 인자로 간주하라. 예를 들어
프로그램 실행 후 아무런 입력 없이 단순히 "enter"를 누르면 명령어 인자가 없는
것으로 간주되며 프로그램은 "Usage" 메시지를 출력하여야 한다. 입력으로
"libgcc_s.so"를 입력하면 파일명으로 간주된다. 평가를 위한 테스트케이스에 포함된
파일의 이름은 "libgcc_s.so", "libgcc_eh.a", "libgcc.a"이다.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  int myargc = 1, i;
  char my_cmd_line[1000];
  char *myargv[20] = {"fsize", NULL};
  char *token = NULL;

  chdir("/usr/lib/gcc/x86_64-linux-gnu/11");
  gets(my_cmd_line);

  token = strtok(my_cmd_line, " ");

  while (token) {
    myargv[myargc++] = token;
    token = strtok(NULL, " ");
  }

  return mymain(myargc, myargv);
}

int mymain(int argc, char *argv[]) {
  if (argv[1] == NULL) {
    printf("Usage : fsize <file>");
    return 0;
  }

  FILE *fd = NULL;
  fd = fopen(argv[1], "r");

  int front = ftell(fd);
  fseek(fd, 0, 2);
  int rear = ftell(fd);

  printf("File %s size : %d", argv[1], rear - front);

  return 0;
}