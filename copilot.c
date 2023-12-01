#include <stdio.h>
#include <stdlib.h>

int main(void) {
  char *str = (char *)malloc(sizeof(char) * 20);
  strcpy(str, "1,2,3,4,5,6\n7,8,9.10");
  puts(str);

  int numOfNums = 1;
  for (char *tmp = str; *tmp != '\0'; tmp++) {
    if (*tmp == ',') {
      numOfNums++;
    } else if (*tmp == '\n') {
      numOfNums++;
      *tmp = ',';
    }
  }
  printf("numOfNums: %d\n", numOfNums);
  puts(str);
}