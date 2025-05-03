#include <stdio.h>
int main(){
    int num = 7;
    int count = 0;
    for(int i =1; i<=num ; i=i+1){
        if(num%i==0){
            count=count+1;
        }
     }
    if (count==2){
        printf("%d is a prime number",num);
    }
    else{
        printf("%d is not a prime number",num);
    }
}
