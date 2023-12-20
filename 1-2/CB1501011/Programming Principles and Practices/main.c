#include <stdio.h>
#include <string.h>

typedef struct test {
  int a;
  float b;
  char *c;
  char d[10];
} Test;

void printTestDot(Test t) {
  // t.c = "cherry";
  // memcpy(t.d, "dragonfruit", 11);
  printf("%d %f %s %s\n", t.a, t.b, t.c, t.d);
}

void printTestArrow(Test *t) {
  // t->c = "eggplant asdf";
  // strcpy(t->d, "fig asdf");
  printf("%d %f %s %s\n", t->a, t->b, t->c, t->d);
}

void swapTest(Test *a, Test *b) {
  Test temp = *a;
  *a = *b;
  *b = temp;
}

void isortTest(Test *list, int size) {
  for (Test *i = list; i < list + size; i++) {
    for (Test *j = i + 1; j > list && j->a < (j - 1)->a; j--) {
      swapTest(j, j - 1);
    }
  }
}

void bsortTest(Test *list, int size) {
  for (Test *i = list; i <= list + size; i++) {
    for (Test *j = i; j <= list + size; j++) {
      if (j->a < i->a) swapTest(i, j);
    }
  }
}

int main(void) {
  // struct test t1 = {1, 2.0, "apple", "banana"};
  // Test t2 = {3, 4.0, "carrot", "durian"};
  Test list[11] = {
      {4, 2.0, "apple", "banana"},         {3, 4.0, "carrot", "durian"},
      {6, 6.0, "eggplant", "fig"},         {1, 8.0, "grape", "honeydew"},
      {2, 10.0, "ice cream", "jackfruit"}, {8, 12.0, "kiwi", "lemon"},
      {0, 14.0, "mango", "nectarine"},     {7, 16.0, "orange", "peach"},
      {9, 18.0, "quince", "raspberry"},    {5, 20.0, "strawberry", "tangerine"},
      {10, 22.0, "ugli", "watermelon"}};
  // printTestDot(t1);
  // printTestArrow(&t2);
  bsortTest(list, 11);
  for (Test *i = list; i <= list + 11; i++) printTestArrow(i);
}