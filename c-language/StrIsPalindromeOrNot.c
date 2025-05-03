#include <stdio.h>
#include <string.h>
int main(){
    char str[10]= "malyalam";
    int i, len, rev= 0;
    len = strlen(str);
    for (i =0; i<len; i++){
        if(str[i] ==str[len - i - 1] ){
            rev = 1;
            break;
        }
    }
    if(rev){
        printf("%s is a palindrome", str);

    }
    else
        printf("%s is not a palindrome", str);
}