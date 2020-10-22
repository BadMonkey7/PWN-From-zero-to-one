#include<stdio.h>
void vuln()
{
    char buf[50];
    gets(buf);
}

int main(){
    vuln();
    return 0;
}
