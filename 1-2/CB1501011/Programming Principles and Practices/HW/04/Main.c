// 4번
/*
rand() 함수를 이용하여 음이 아닌 정수 난수를 생성하는 프로그램을 작성하라.
생성해야할 난수의 수와 seed 값은 명령어 인자로 주어진다.

main() 함수에 명령어 인자를 처리하는 코드를 추가하라. main() 함수의 Usage
메시지를 보면 명령어 인자, N과 seed를 어떻게 처리할 지 이해할 수 있을 것이다.
N은 필수 인자이며 seed는 선택적 인자이며 기본값은 10이다.

아래에 설명된 generate_numbers()를 완료해야 합니다.

int * generate_numbers(int nnums);
* @요약: rand() 함수를 이용하여 nnums 개의 음이 아닌 난수 정수를 생성하고 이를
동적으로 할당한 정수 배열에 저장하고 그 주소를 반환하는 함수. 유효한 값의 끝, 즉
배열의 끝을 표시하기 위하여 마지막에 음의 값을 추가하라. 예를 들어 nnums=5이고
생성한 난수 값이 3,5,19,0,8 이라면 동적으로 할당된 배열은 3,5,19,0,8,-1 값을
가져야 한다.

* 반환값: 난수를 저장하는 동적으로 할당된 메모리의 포인터/주소입니다.

* @param : nnums - 생성할 난수 개수입니다.

각 테스트케이스에서 입력을 해당 테스트케이스의 명령어 인자로 간주하라. 예를 들어
프로그램 실행 후 아무런 입력 없이 단순히 "enter"를 누르면 명령어 인자가 없는
것으로 간주되며 프로그램은 "Usage" 메시지를 출력하여야 한다. 입력으로 "10"을
입력하면 인자 <N>에 해당하는 값으로 간주된다.
*/

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *generate_numbers(int nnums) {
  int *nums = (int *)malloc(sizeof(int) * (nnums + 1)), i;
  for (i = 0; i < nnums; i++) {
    nums[i] = rand();
  }
  nums[i] = -1;
  return nums;
}
void print_nums(int *pn) {
  int i = 0;
  while (pn[i] >= 0) {
    printf("%d ", pn[i++]);
    if (i % 5 == 0) printf("\n");
  }
}

int main(int argc, char *argv[]) {
  int myargc = 1, i;
  char my_cmd_line[1000];
  char *myargv[20] = {"generate_numbers", NULL};
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
  int N = 10, seed = 10;
  int *rand_values = NULL;

  if (argc < 2) {
    printf("Usage : %s < N > [<seed>]\n\n", argv[0]);
    puts("N : Mandatory, Number of random numbers to generate");
    puts(
        "seed : An optional seed value to seeds the random number generator, "
        "defalut = 0");
    return 0;
  }

  N = atoi(argv[1]);
  seed = argv[2] ? atoi(argv[2]) : seed;

  srand(seed);
  rand_values = generate_numbers(N);
  print_nums(rand_values);

  return 0;
}