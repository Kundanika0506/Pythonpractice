#include <stdio.h>
int main(){
    int arr[]={2,3,5,6,7,8,12,11,9};
    int maxi = arr[0];
    int len = sizeof(arr)/sizeof(arr[0]);
    for (int i = 0; i<len; i++){
        if(arr[i]>maxi){
            maxi = arr[i];
        }
    }
    printf("%d is the largest element in the array",maxi);
}