#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int priority;
  int index;
} Doc;

typedef struct {
  Doc dat[100];
  int rear, front;
} Queue;

Queue *initQueue() {
  Queue *q = (Queue *)malloc(sizeof(Queue));
  q->rear = q->front = 0;
  return q;
}

int is_empty(Queue *q) { return q->rear == q->front; }

int is_full(Queue *q) { return (q->rear + 1) % 100 == q->front; }

void enqueue(Queue *q, Doc item) {
  if (is_full(q)) {
    printf("Queue is full\n");
    exit(0);
  }
  q->rear = (q->rear + 1) % 100;
  q->dat[q->rear] = item;
}

Doc dequeue(Queue *q) {
  if (is_empty(q)) {
    printf("Queue is empty\n");
    exit(1);
  }
  q->front = (q->front + 1) % 100;
  return q->dat[q->front];
}

Doc peek(Queue *q) {
  if (is_empty(q)) {
    printf("Queue is empty\n");
    exit(1);
  }
  return q->dat[(q->front + 1) % 100];
}

void getQueue(Queue *q, int numDocs) {
  for (int i = 0; i < numDocs; i++) {
    Doc doc;
    scanf("%d", &doc.priority);
    doc.index = i;
    enqueue(q, doc);
  }
}

int max(Queue *q) {
  int max = 0;
  for (int i = q->front + 1; i <= q->rear; i++) {
    if (max < q->dat[i].priority) {
      max = q->dat[i].priority;
    }
  }
  return max;
}

int main(void) {
  int numCases, numDocs, targetDoc;
  Queue *docs;
  scanf("%d", &numCases);

  while (numCases--) {
    docs = initQueue();
    scanf("%d %d", &numDocs, &targetDoc);
    getQueue(docs, numDocs);
    int count = 0;
    for (;;) {
      if (peek(docs).priority == max(docs)) {
        count++;
        if (peek(docs).index == targetDoc) {
          printf("%d\n", count);
          break;
        } else {
          dequeue(docs);
        }
      } else {
        enqueue(docs, dequeue(docs));
      }
    }
  }
  return 0;
}