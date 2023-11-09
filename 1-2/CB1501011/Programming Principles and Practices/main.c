#include <stdio.h>
#include <string.h>


int main(void) {
  char str1[256] = "Hello World !!!\n Good Day !!!";
  char str2[256] = "Hello PNU CSE !!!";
  char str3[256];

  printf("strlen(str1) = %d, strlen(str2) = %d\n", strlen(str1),
         strlen(str2));

  printf("strcpy(str3,str1) = %s\n", strcpy(str3, str1));

  printf("strcmp(str1,str3) = %d, strcmp(str2,str3) = %d",
         strcmp(str1, str3), strcmp(str2, str3));

  return 0;
}