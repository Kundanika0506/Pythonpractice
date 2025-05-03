#include <stdio.h>
void arrReverse(int arr[], int len){
    for (int i = len-1; i>=0;i--)
        printf("%d ",arr[i]);
}
int main(){
    int arr[]= {1,2,3,4,5,6,7,8,9,10,11,12};
    int len = sizeof(arr)/sizeof(arr[0]);
    printf("the reverse of the array is\n");
    arrReverse(arr,len);
}