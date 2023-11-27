#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
  return (*(unsigned int *)a - *(unsigned int *)b);
}

unsigned int calc_intercept(unsigned int n) { return round((float)n * 0.15); }

void scan_nums(unsigned int *nums, unsigned int n) {
  while (n--) scanf("%d", nums++);
}

int calc_sum(unsigned int *nums, unsigned int n, unsigned int intercept) {
  unsigned int sum = 0;
  for (unsigned int *i = nums + intercept; i < nums + n - intercept; i++)
    sum += *i;
  return sum;
}

int main(void) {
  unsigned int n;
  scanf("%d", &n);

  unsigned int intercept = calc_intercept(n);
  unsigned int difficulty[n];
  scan_nums(difficulty, n);

  qsort(difficulty, n, sizeof(unsigned int), compare);

  unsigned int sum = calc_sum(difficulty, n, intercept);

  printf("%d", (int)round((float)sum / (n - 2 * intercept)));

  return 0;
}