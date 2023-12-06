// 3번
/*
주어진 소스 코드를 완성하여 강의 슬라이드에 설명된 정기 예금의 이자를 계산하는
프로그램을 작성하세요.

int inter_calc(int dep, double rate, int yrs);
* @요약: 전체 예치 기간 동안 예치금에 대한 총 이자를 계산합니다. 예치금 , 이자율
, 예치 기간 연도의 총 이자는 다음과 같습니다. 기간이 1년보다 짧으면 이자는
0입니다.

* 반환값: 총 이자를 가장 가까운 정수로 반올림한 값입니다.

* @param : dep - 입금된 금액

                 rate - 연간 이자율(0.018 == 1.8%)

           yrs - 예금 기간(년)

명령어 인자가 없으면 아래와 같이 사용법을 출력하여야 한다.

Usage: bankint <deposit_money> <interest_rate(%)> <term(year(s))>
Default interest = 1.8%, Default term = 1 year

이 문제에서 main() 함수를 종료할 때는 "return 0"를 사용하라. "exit(1)" 또는
"return 1" 등은 원치 않는 결과를 발생시킬 수 있다.

각 테스트케이스에서 입력을 해당 테스트케이스의 명령어 인자로 간주하라.
*/

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DEF_RATE 1.8  // default rate (%)
#define DEF_TERM 1    // default term (yr)

int inter_calc(int dep, double rate, int yrs) {
  // printf("%d %f %d\n", dep, rate, yrs);
  return (int)round(dep * pow(1 + rate, yrs) - dep);
}

int main(int argc, char *argv[]) {
  int myargc = 1, i;
  char my_cmd_line[1000];
  char *myargv[20] = {"bankint", NULL};
  char *token = NULL;

  gets(my_cmd_line);

  token = strtok(my_cmd_line, " ");

  while (token) {
    myargv[myargc++] = token;
    token = strtok(NULL, " ");
  }

  return mymain(myargc, myargv);
}

int mymain(int argc, char *argv[]) {
  int deposit;
  double rate = DEF_RATE / 100;
  int term = DEF_TERM;

  if (argv[1] == NULL) {
    printf(R"(Usage: bankint <deposit_money> <interest_rate(%)> <term(year(s))>
Default interest = 1.8%, Default term = 1 year)");
    return 0;
  }

  deposit = atoi(argv[1]);
  rate = argv[2] == NULL ? rate : atof(argv[2]) / 100;
  term = argv[3] == NULL ? term : atoi(argv[3]);

  printf("Total Interest = KRW %d\n", inter_calc(deposit, rate, term));

  return 0;
}