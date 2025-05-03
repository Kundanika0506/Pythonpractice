#include <stdio.h>
int main(){
    int num;
    scanf("%d",&num);
    int sum = 0;
    for(int i = 1; i<num; i++){  //not including the number 
        if(num%i==0){
            sum = sum+i;
        }
    }
    if(sum>num){
        printf("%d is an abundant number",num);
    }
    else{
        printf("%d is not an abundant number",num);
    }
}