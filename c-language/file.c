#include <stdio.h>
int main(){
    FILE *ptr;
    ptr= fopen("KundanC.txt","w");
    int num=444;
    fprintf(ptr,"%d",num);
    fclose(ptr);
}

