#include<stdio.h> 
void shell(){
    system("/usr/bin/sh");
}
int main(){
    char buf[10];
    gets(buf);
    return 0;
}
