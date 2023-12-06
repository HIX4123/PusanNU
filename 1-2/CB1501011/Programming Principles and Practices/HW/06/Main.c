// 6번
/*
주어진 파일에서 음이 아닌 정수 값들을 읽어 들이는 read_numbers_binary(),
read_numbers_csv() 함수를 완성하라. 이 함수는 읽어 들인 정수 값들을 모두
포함하고 있는 정수 배열의 포인터를 반환하여야 한다. 값을 저장하는 정수 배열들은
함수 내에서 동적으로 할당되어야 하며 모든 유효 값의 끝에 "-1" 값을 덧붙여 배열의
끝임을 표시하여야 한다.

read_numbers_binary() 가 읽을 파일은 save_numbers_binary()라는 함수에 의해
만들어졌으며 read_numbers_csv()는 save_numbers_csv()라는 함수에 의해 만들어졌다.
이들 함수의 코드는 주어진 코드에 포함되어 있다. 구현한 함수가 제대로 값들을 읽어
오는 지 간단히 확인하기 위하여 정수 배열의 값 중 가장 큰 값을 구하는 get_max()
함수가 호출된다. 이 함수 역시 소스 코드 내에 포함되어 있다.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

int sizeofFile(char *filename) {
  FILE *fd = fopen(filename, "r");
  
  fseek(fd, 0, 2);
  int size = ftell(fd);
  fclose(fd);
  
  return size;
}

int getNumOfNums(char *str) {
	int numOfNums = 1;
	for (char *tmp = str; *tmp != '\0'; tmp++) {
		if (*tmp == ',' || *tmp == '\n') numOfNums++;
	}
	
	return numOfNums;
}

int * read_numbers_binary(char *filename) {
  FILE *fd = fopen(filename, "rb");
  
  int binLength = sizeofFile(filename) / sizeof(int);
  int *nums = (int *)calloc(binLength + 1, sizeof(int));
  
  fread(nums, sizeof(int), binLength, fd);
  nums[binLength] = -1;
	
	fclose(fd);
	
	return nums;
}

int * read_numbers_csv(char *filename) {
	FILE *fd = fopen(filename, "rt");
	
	char *str = (char *)malloc(sizeofFile(filename) + sizeof(char));
	for (char *i = str;
		   fgets(i, sizeofFile(filename) + sizeof(char), fd) != NULL;
		  )
		while (*i++ != '\n') ;
	
	fclose(fd);
  
	int numOfNums = getNumOfNums(str);
	int *nums = (int *)calloc(numOfNums + 1, sizeof(int));
	char *token = strtok(str, ",");
	for (int i = 0; token; i++) {
		nums[i] = atoi(token);
		token = strtok(NULL, ",\n");
	}
	nums[numOfNums] = -1;
	
	free(str);
	
	return nums;
}
void save_numbers_binary(int *pn, char *filename) {
	FILE *fd = fopen(filename, "wb");
	int *pcur = pn;
	
	if (fd) {
		while (*pcur >= 0) pcur++;
		fwrite(pn, sizeof(int), pcur-pn, fd);
		fclose(fd);
	}
}

void save_numbers_csv(int *pn, char *filename) {
	FILE *fd = fopen(filename, "wt");	// Explicitly specify text mode
	int *pcur = pn;
	
	if (fd) {
		while (*pcur >= 0) {
			fprintf(fd, "%d", *pcur++);	
			while (*pcur >= 0) {
				fprintf(fd, ",%d", *pcur++);
				if ( (pcur-pn) % 8 == 0) {
					fprintf(fd, "\n");
					break;
				}
			}
		}
		fclose(fd);
	}
}

int get_max(int *values) {
	int nmax = 0;
	
	if (values) {
		while (*values >= 0) {
			if (*values > nmax)
				nmax = *values;
			values++;
		}
	}
	return nmax;
}

int * generate_numbers(int nnums) {
	int *pnum = (int *)malloc(sizeof(int)*(nnums+1));
	int *pcur = pnum;

	assert(pnum);	
	
	while (pcur < pnum + nnums) 
		*pcur++ = rand();
	
	*pcur = -1;
	
	return pnum;	
}
int main(void) {
	int testcase = 1, bbinary = 0;
	char *filename = "output"; 
	int test_values1[] = {1, 9, 178, 15, 2345, 2, 2, 34, 12, 5, -1};
	int *values = test_values1;
	
	scanf("%d", &testcase);
	switch (testcase) {
		case 2 :
			bbinary = 1;
		break;				
		case 3 :
			srand(11);
			values = generate_numbers(100);			
			break;
		case 4 :
			bbinary = 1;
			srand(21);
			values = generate_numbers(100);			
			break;			
		case 5 :
			srand(11);
			values = generate_numbers(10000);
			break;
		case 6 :
			srand(21);
			bbinary = 1;
			values = generate_numbers(10000);
			break;
		default :
			break;			
	}
	if (bbinary) {
		save_numbers_binary(values, filename);
		printf("Max : %d\n", get_max(read_numbers_binary(filename)));
	}
	else {
		save_numbers_csv(values, filename);		
		printf("Max : %d\n", get_max(read_numbers_csv(filename)));
	}
	
	return 0;
}