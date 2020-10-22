#include<stdio.h>
__asm__("syscall");
__asm__("pop %rax;ret;");
__asm__("pop %rdx;ret;");
char binsh[10] = "/bin/sh";
void vuln()
{
    char buf[50];
    gets(buf);
}

int main(){
    vuln();
    return 0;
}
