#include<stdio.h>  
int main(){
    char str[100] = "4PREP2INSTA6";
    int i,sum = 0;
    
    for (i= 0; str[i] != '\0'; i++)
    {
        if ((str[i] >= '0') && (str[i] <= '9')) 
        {
            sum += (str[i] - '0');

        }
    }
    printf("Sum of all digits: %d",sum);
}