#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
  int dep = 10000000;
  double rate = 2.2;
  int yrs = 2;

  printf("%d", (int)round(dep * pow(1 + rate, yrs) - dep));
}