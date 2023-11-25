#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int x;
  int y;
} Pos;

int qcmp(const void *a, const void *b) {
  const Pos *foo = a, *bar = b;
  return (foo->y == bar->y) ? (foo->x - bar->x) : (foo->y - bar->y);
}

int main(void) {
  int len;
  scanf("%d", &len);
  Pos pos[len];
  for (Pos *i = pos; i < pos + len; i++) scanf("%d %d", &i->x, &i->y);
  qsort(pos, len, sizeof(Pos), qcmp);
  for (Pos *i = pos; i < pos + len; i++) printf("%d %d\n", i->x, i->y);
}