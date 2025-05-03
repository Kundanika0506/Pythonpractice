#include <stdio.h>
int main(){
    int arr[]={3,4,1,2,6,9,8,12,4,7,11};
    int len= sizeof(arr)/sizeof(arr[0]);
    int even_count=0;
    int odd_count= 0;

    for (int i = 0;i<len;i++){
        if(arr[i]%2==0){
            even_count++;
        }
        else
            odd_count++;
    }
    printf("Even counts are %d \nOdd counts are %d", even_count, odd_count);
}