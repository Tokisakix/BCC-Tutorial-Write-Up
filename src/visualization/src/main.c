#include <stdio.h>
#include "func.h"

int main() {
    printf("main start.\n");
    for (int j = 1 * 4; j--;){
        func_a();
        func_b();
        func_c();
    }
    printf("main end.\n");
    return 0;
}