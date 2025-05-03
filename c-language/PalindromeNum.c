#include <stdio.h>
int main(){
    int num = 121;
    int temp = num;
    int rem;
    int ans = 0;
    while(num!=0){
        rem = num%10;
        ans = ans*10+rem;
        num= num/10;
    }
    if(ans==temp){
        printf("%d is a palindrome number",temp);
    }
    else{
        printf("%d is not a palindrome number",temp);
    }
}