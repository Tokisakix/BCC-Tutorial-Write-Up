#include "func.h"

void func_a(){
    for (int i = 10 * 10000000; i--;);
    func_d();
    return;
}

void func_b(){
    for (int i = 20 * 10000000; i--;);
    return;
}

void func_c(){
    for (int i = 35 * 10000000; i--;);
    return;
}

void func_d(){
    for (int i = 5 * 10000000; i--;);
    return;
}