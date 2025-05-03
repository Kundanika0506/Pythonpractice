#include <stdio.h>
int main(){
    int num1 = 36;
    int num2 = 60;
    int hcf = 1;
    for(int i = 1; i<= num1 || i <= num2; i++){
        if (num1%i==0 && num2%i==0)
            hcf = i;
    }
    printf("%d is the hcf of %d and %d", hcf,num1,num2);
}