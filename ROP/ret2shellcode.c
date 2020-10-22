#include<stdio.h>
void vuln(){
        char buf[50];
        printf("buf address = %p \n",&buf);
        gets(buf);
}

int main(){
    vuln();
    return 0;
}
