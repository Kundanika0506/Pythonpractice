#include <stdio.h>
int checkHarshad(int num){
    int temp= num;
    int sum = 0;
    while(temp !=0){
        sum+= temp %10;
        temp/= 10;
    }
    return num%sum==0;
}
int main(){
    int num = 153;
    if(checkHarshad(num))
        printf("%d is Harshad's Number", num);
    else
        printf("%d is not a Harshad's Number", num);

}