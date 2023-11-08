#include <stdio.h>
#include <math.h>

int main() {

   int ai = 10 ;
   printf("\n 교수님, 단술 %d 병만  사주세요. ㅋㅋㅋㅋ \n", ai*10);
   int i = 10 ;
   for(i=1 ; i <= 20 ; i++){
    printf("\n sin(%3d) = %8.5f", i, sin( (float)i) ) ;
   }

}
