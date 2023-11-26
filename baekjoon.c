#include <stdio.h>
#include <string.h>

int main(void) {
  char str[102];
  int small, big, flag;
  while (fgets(str, 102, stdin) && strcmp(str, ".\n")) {
    small = 0, big = 0, flag = 1;
    for (char *p = str; *p; p++) {
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
        flag = 0;
        break;
      }
    }
    if (small || big) flag = 0;
    printf("%s\n", flag ? "yes" : "no");
  }
}