#include <stdio.h>

int main() {
  char S[1001], i;
  fgets(S, 1000, stdin);
  printf("%c", S[getchar() - '1']);
}