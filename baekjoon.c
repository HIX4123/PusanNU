#include <stdio.h>

int main(void) {
  int len;
  scanf("%d", &len);
  int pos[len][2];

  for (int i = len; i--;) {
    scanf("%d %d", &pos[i][0], &pos[i][1]);
  }
  printf("\n");

  int *first = pos, *last = pos + sizeof(pos);
  for (int *i = first; i < last; i++) {
    for (int *j = i + 1; j > first && j[1] < (j - 1)[1]; j--) {
      int tmp = *j;
      *j = *(j - 1);
      *(j - 1) = tmp;
    }
  }

  for (int i = 0; i < len; i++) {
    printf("%d %d\n", pos[i][0], pos[i][1]);
  }
}