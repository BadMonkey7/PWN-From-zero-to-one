//
// Created by badmonkey on 2021/4/11.
//

#include "stdio.h"
#include "stdlib.h"
__attribute__((constructor)) void init_function(){
    printf("function executed before main\n");
}
__attribute__((destructor)) void fini_function(){
    printf("function executed after main\n");
}
int main(){
    printf("init_function address = %p\n",init_function);
    printf("fini_function address = %p\n",fini_function);
    return 0;
}