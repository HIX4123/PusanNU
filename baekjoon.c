
#include <stdio.h>
typedef struct student {
  int id;
  char *pname;
  double points;
} STUD;

int main(void) {
  int i;  // index
  STUD pnucse[] = {{1, "Choi", 9.9}, {2, "Park", 0.1}, {3, "Kim", 5.0},
                   {4, "Lee", 3.0},  {5, "Moon", 9.5}, {6, "Kang", 7.0},
                   {7, "Jeon", 0.9}, {-1, NULL, 0}};

  STUD *ptr = pnucse;

  for (; ptr->id >= 0; ptr++) {
    printf("[%d:%s] = %lf\n", ptr->id, ptr->pname, ptr->points);
  }

  return 0;
}