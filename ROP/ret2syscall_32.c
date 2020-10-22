#include<stdio.h>
__asm__("int $0x80;");
__asm__("pop %eax;ret;");
__asm__("pop %ecx;ret;");
__asm__("pop %edx;ret;");
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
