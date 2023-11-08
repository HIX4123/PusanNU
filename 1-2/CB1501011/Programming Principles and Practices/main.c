#include <math.h>
#include <stdio.h>

/**
* @brief : Find an approximation to the square root of a non-negative number
using the Newton's method.
* @return: An approximation to the square root. The square of it should be in
the range [x-epsilon, x+epsilon]. -1 if it can't find an answer.
* @param : x - target number, epsilon - the allowed difference
*/
double findroot_newton(double x, double epsilon) {
  double ans = x / 2.0;
  int numGuesses = 0;

  double diff = fabs(ans * ans - x);

  while (diff >= epsilon) {
    ans = (ans * ans + x) / (2 * ans);

    diff = fabs(ans * ans - x);
    numGuesses = numGuesses + 1;
  }

  printf("# of Guesses = %d   ", numGuesses);

  return ans;
}

int main(void) {
  double x;
  double epsilon = 0.001;
  for (int i = -10000000; i < 10000000; i++) {
    x = i;

    if (x > 0) {
      printf("[  NEWTON  ] sqrt(%g) ~= %g\n", x,
             findroot_newton(x, epsilon));
    }
  }

  return 0;
}