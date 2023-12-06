// 5번
/*
정수 배열에서 고유값의 개수를 세는 count_distinct_values() 함수를 완성합니다.

필요한 경우 자신만의 함수를 추가할 수 있습니다.

int count_distinct_values(int *values);
* @요약: 정수 배열이 인자로 주어질 때 해당 배열 내에 서로 다른 정수의 개수를
세는 함수이다. 배열의 유효 항목은 모두 음수가 아니다. 음수가 쓰일 경우 그것은
배열의 끝은 나타내기 위함이다. main()에 정의된 "test_values"라는 정수 배열 예를
살펴보라. 만약 count_distinct_values(test_values)가 호출되면 함수는 6을
반환하여야 한다. 이 배열 안에는 1, 2, 3, 4, 5 그리고 7이라는 6개의 서로 다른
수가 있기 때문이다. 배열의 마지막 값인 "-1"은 유효한 값이 아니며 단지 배열의
끝을 나타내기 사용되었다.

* 반환값: 배열의 고유값 개수입니다.

* @param : 값 - 정수 배열에 대한 포인터
*/

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) { return *(int *)a - *(int *)b; }

int count_distinct_values(int *values) {
  int *front = values, *rear;
  for (rear = values; *rear++ != -1;)
    ;
  int valuesLength = rear - front - 1;

  qsort(values, valuesLength, sizeof(int), compare);

  int count = 0;
  for (int i = 0; i < valuesLength; i++) {
    count += values[i] == values[i + 1] ? 0 : 1;
  }
  return count;
}

int *generate_numbers(int nnums) {
  int *pnum = (int *)malloc(sizeof(int) * (nnums + 1));
  int *pcur = pnum;

  assert(pnum);

  while (pcur < pnum + nnums) *pcur++ = rand() / 100000;

  *pcur = -1;

  return pnum;
}
int main(void) {
  int test_values[] = {1, 2, 1, 2, 1, 3, 4, 5, 4, 7, -1};
  int *rand_values = test_values;
  int test_case = 1;

  srand(10);
  scanf("%d", &test_case);

  switch (test_case) {
    case 2:
      rand_values = generate_numbers(100);
      break;
    case 3:
      rand_values = generate_numbers(10000);
      break;
    case 4:
      rand_values = generate_numbers(30000);
      break;
    default:
      break;
  }
  printf("# of distinct values = %d\n", count_distinct_values(rand_values));

  if (test_case > 1) free(rand_values);

  return 0;
}
