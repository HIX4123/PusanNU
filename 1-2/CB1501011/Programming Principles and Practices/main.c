// void *malloc(size_t size);
// void *calloc(size_t nmemb, size_t size);
// void *realloc(void *ptr, size_t size);
// void free(void *ptr);

// void *memcpy(void *dest, const void *src, size_t n);

// FILE *fopen(const char *pathname, const char *mode);
// int fclose(FILE *stream);

// // binary
// size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);
// size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);

// //text
// int fgetc(FILE *stream);
// int fputc(int c, FILE *stream);

// char *fgets(char *s, int size, FILE *stream);
// int fputs(const char *s, FILE *stream); // \n, \0 안붙임

// int fscanf(FILE *stream, const char *format, ...);
// int fprintf(FILE *stream, const char *format, ...);

// int feof(FILE *stream); // 파일 끝에 도달했으면 0이 아닌 값을 반환

// char *strtok(char *str, const char *delim);
// int atoi(const char *nptr);
// float atof(const char *nptr);

// fseek(FILE *stream, long offset, int whence); // 0: 시작 1: 현위치 2: 끝
// long ftell(FILE *stream);

#include <stdio.h>
#include <stdlib.h>

// int main(void) {
//   FILE *fd = fopen("test.txt", "r+t");
//   fprintf(fd, "Hello, World!\naqwerty\nasdfgh\nzxcvbn");
//   char *str = (char *)malloc(100);
//   fseek(fd, 0, 0);

//   for (char *i = str; fgets(i, 100, fd) != NULL;)
//     while (*i++ != '\n')
//       ;

//   puts(str);
// }

typedef struct {
  int nums;
  int size;
} Numbers;

int main(void) {
  FILE *fd = fopen("test.bin", "wb");
  Numbers nums = {100, 10};
  fwrite(&nums, sizeof(Numbers), 1, fd);
  fclose(fd);
  FILE *fb = fopen("test.bin", "rb");
  Numbers nums1;
  fread(&nums1, sizeof(Numbers), 1, fb);
  printf("%d %d", nums1.nums, nums1.size);
}