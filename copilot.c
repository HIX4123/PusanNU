#include <math.h>
#include <stdbool.h>
#include <stdio.h>

typedef struct {
  unsigned int num;
  bool isPrime;
} Prime;

void gen_list(Prime* prime, unsigned int start, unsigned int end) {
  unsigned int rangeWidth = end - start + 1;
  for (unsigned int i = 0; i < rangeWidth; i++) {
    prime[i].num = start + i;
    prime[i].isPrime = true;
  }
}

void check_prime(Prime* prime, unsigned int start, unsigned int end) {
  unsigned int rangeWidth = end - start + 1;
  for (unsigned int i = 0; i < rangeWidth; i++) {
    if (prime[i].num == 1) {
      prime[i].isPrime = false;
      continue;
    }
    for (unsigned int j = 2; j <= sqrt(prime[i].num); j++) {
      if (prime[i].num % j == 0) {
        prime[i].isPrime = false;
        break;
      }
    }
  }
}

Prime* create_and_initialize_primes(unsigned int start, unsigned int end) {
  Prime* primes = malloc((end - start + 1) * sizeof(Prime));
  gen_list(primes, start, end);
  check_prime(primes, start, end);
  return primes;
}

void print_prime(Prime* prime, unsigned int start, unsigned int end) {
  unsigned int rangeWidth = end - start + 1;
  for (unsigned int i = 0; i < rangeWidth; i++) {
    if (prime[i].isPrime) {
      printf("%d\n", prime[i].num);
    }
  }
}

int main() {
  unsigned int start, end;
  scanf("%d %d", &start, &end);

  Prime* primes = create_and_initialize_primes(start, end);
  print_prime(primes, start, end);

  free(primes);
}