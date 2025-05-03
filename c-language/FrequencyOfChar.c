#include<stdio.h> 
int main(){
    char str[100] ="kundanika";
    int i;
    int freq[200] = {0};
    
    for(i = 0; str[i] != '\0'; i++)
    {
        freq[str[i]]++;
    }
    
    for(i = 0; i < 200; i++)
    {
        if(freq[i] != 0){
            printf("The frequency of %c is %d\n", i, freq[i]);
        }
    }
}