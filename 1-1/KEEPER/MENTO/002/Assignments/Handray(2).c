#include <stdio.h>

void asdf(int* arg1, int* arg2, int* arg3) {
    arg1 = 5;
    arg2 = 9;
    arg1 = 1;
    arg2 = 2;
    arg3 = arg1;
    arg2 = arg2;
}

// void qwer(long long int arg1, long long int arg2, long long int arg3) {
//     int var1 = 5;
//     int var2 = 9;
//     *(long long int*)(arg1) = 1;
//     *(long long int*)(arg2) = 2;
//     *(long long int*)(arg3) = var1;
//     *(long long int*)(arg2) = var2;
// }

int main() {
    int var1 = 3;
    int var2 = 4;
    int var3 = 5;

    asdf(&var1, &var2, &var3);

    return 0;
}
