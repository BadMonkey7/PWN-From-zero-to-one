#include<stdio.h>
#include <stdlib.h>
char binsh[10] = "/bin/sh";
void vuln(){
    char buf[50];
    gets(buf);
}

int main(){
    system("");
    vuln();
    return 0;
}
