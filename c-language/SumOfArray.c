#include <stdio.h>
int main(){
    int arr[]= {2,4,3,5,6,7,1,8};
    int sum = 0;
    int len= sizeof(arr)/sizeof(arr[0]);
    for (int i = 0; i <len; i++){
        sum = sum+arr[i];
    }
    printf("the sum of the elements in the array is %d",sum);
}