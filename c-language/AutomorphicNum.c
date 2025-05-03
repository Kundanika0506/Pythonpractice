#include <stdio.h>
int main(){
    int num1= 5;
    int num2= num1*num1;
    if(num2%10==num1){
        printf("%d is an automorphic number", num1);
    }
    else{
        printf("%d is not an automorphic number", num1);
    }

}