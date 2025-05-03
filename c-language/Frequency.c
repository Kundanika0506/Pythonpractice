#include <stdio.h>
int main(){
    int arr[]= {3,4,5,2,3,4,7,8,9,1,2,6,12,11,10};
    int len = sizeof(arr)/sizeof(arr[0]);
    int num[len];
    for (int i =0;i<len;i++){
        num[i]=0;
    }

    for (int i=0; i<len; i++){
        if(num[i]==0){
            int count = 1;
            for (int j = i+1; j<len; j++){
                if(arr[i]==arr[j]){
                    count++;
                    num[j]=1;
                 }
            }
            printf("%d occurs %d times\n", arr[i],count);

        }
    }
}