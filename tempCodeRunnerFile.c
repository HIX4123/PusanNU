#include <stdio.h>
#include <string.h>

int main(void) {
  char str[101];
  int small = 0, big = 0;
  while (fgets(str, 101, stdin) && strcmp(str, ".")) {
    small = 0, big = 0;
    for (char *p = str; *p++;) {
      switch (*p) {
        case '(':
          small++;
          break;
        case ')':
          small--;
          break;
        case '[':
          big++;
          break;
        case ']':
          big--;
          break;
      }
      if (small < 0 || big < 0) {
        printf("no\n");
        break;
      }
    }
    if (small == 0 && big == 0)
      printf("yes\n");
    else
      printf("no\n");
  }
}