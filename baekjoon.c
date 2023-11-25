#include <stdio.h>

int main(int n) {
  scanf("%d", &n);
  printf("%d", 7 % n % 3 ? n - 2 * n / 5 * 2 : -1);
}