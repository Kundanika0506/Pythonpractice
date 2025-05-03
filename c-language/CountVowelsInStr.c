#include <stdio.h>
int main(){
    char str[100] = "Kundanika Madireddy";  
    int i, vowels = 0;
    
    
    for(i = 0; str[i]; i++)  
    {
        if(str[i]=='a'|| str[i]=='e'||str[i]=='i'||
           str[i]=='o'|| str[i]=='u'||str[i]=='A'||
           str[i]=='E'||str[i]=='I'||str[i]=='O' ||str[i]=='U')
        {
            vowels++;
        }
    }
 	
    printf("Total number of vowels: = %d\n",vowels);
    
}