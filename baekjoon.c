#include <stdio.h>
typedef struct student {
  int id;
  char *pname;
  double points;
} STUD;

void stud_print(STUD *ps);
void stud_swap(STUD *a, STUD *b);
STUD *stud_get_last(STUD *ps_array);
int stud_compare_points(STUD *ps1, STUD *ps2);
STUD *stud_get_lowest_points(STUD *ps_begin, STUD *ps_end);

void stud_print_array_in_decreasing_order(STUD *pnucse) {
  STUD *first = pnucse;
  STUD *last = stud_get_last(pnucse);
  for (; pnucse < last; ++pnucse) {
    for (STUD *i = pnucse + 1; i > first && stud_compare_points(i, i - 1);
         --i) {
      stud_swap(i, i - 1);
    }
  }
  while (first++ <= last) {
    stud_print(first);
  }
}

int main(void) {
  STUD pnucse[] = {{1, "Choi", 9.9}, {2, "Park", 0.1}, {3, "Kim", 5.0},
                   {4, "Lee", 3.0},  {5, "Moon", 9.5}, {6, "Kang", 7.0},
                   {7, "Jeon", 0.9}, {-1, NULL, 0}};

  int test_id = 0;
  scanf("%d", &test_id);

  stud_print_array_in_decreasing_order(pnucse);

  return 0;
}