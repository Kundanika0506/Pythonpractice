#include <stdio.h>
int main(){
    int arr[]={2,4,5,6,7,2,1,9,10};
    int mini= arr[0];
    int len= sizeof(arr)/sizeof(arr[0]);
    for (int i = 0; i <len; i++){
        if(arr[i]<mini){
            mini=arr[i];
        }
    }
    printf("%d is the smallest element in the array",mini);

}