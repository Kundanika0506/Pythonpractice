#include <stdio.h>
int factor(int num){
    int sum = 0;
    for(int i = 1; i<num;i++){
        if(num%i==0)
        sum=sum+i;
    }
    return sum;
}
int main(){
    int num1 = 6;
    int num2= 28;
    int sum1= factor(num1);
    int sum2=factor(num2);
    if(sum1/num1== sum2/num2)
        printf("Friendly pair");
    else
        printf("Not Friendly pair");


}