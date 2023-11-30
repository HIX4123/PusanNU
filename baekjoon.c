#include <math.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int num;
  unsigned int count;
} Counter;

int numsCompare(const void *a, const void *b) { return *(int *)a - *(int *)b; }
int counterCompare(const void *a, const void *b) {return *(Counter *)a.count - *(Counter *)b.count;}

void getNums(int *nums, unsigned int numOfNums) {
  for (int i = 0; i < numOfNums; i++) {
    scanf("%d", &nums[i]);
  }
  qsort(nums, numOfNums, sizeof(int), numsCompare);
}

int getAverage(int *nums, unsigned int numOfNums) {
  int sum = 0;
  for (int i = 0; i < numOfNums; i++) {
    sum += nums[i];
  }
  return round((double)sum / numOfNums);
}

int getMedian(int *nums, unsigned int numOfNums) { return nums[numOfNums / 2]; }

int getMode(int *nums, unsigned int numOfNums) {
  Counter counters[numOfNums];
  counters[0].num = nums[0];
  counters[0].count = 1;
  for (int i = 1, index = 0; i < numOfNums; i++) {
    if (nums[i] == counters[index].num) {
      counters[index].count++;
    } else {
      counters[++index].num = nums[i];
      counters[index].count = 1;
    }
  }
  qsort(counters, numOfNums, sizeof(Counter), counterCompare);
}

int main(void) {
  unsigned int numOfNums;
  scanf("%d", &numOfNums);
  int nums[numOfNums];

  getNums(nums, numOfNums);
  int average = getAverage(nums, numOfNums);
  int median = getMedian(nums, numOfNums);
  int mode = getMode(nums, numOfNums);

  return 0;
}