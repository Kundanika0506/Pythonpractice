#include <stdio.h>
int main(){
    int num= 9;
    for(int i = 1; i<num; i++){
        if(i*i==num){
            printf("%d is a perfect square",num);
        }
        else{
            printf("%d is not a perfect square",num);
        }

    }
}