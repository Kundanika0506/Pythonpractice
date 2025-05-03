#include<stdio.h>

int countDistinct(int *array, int size){
    int count = 0;
    for (int i = 0; i < size; i++){
        int j = 0;
        for (j = i+1; j < size; j++)
        {   
            if (array[i] == array[j]){
                break;
            }
        }
        if (j == size)
            count++;
    }
    return count;
}

int main()
{
    int arr[] = {5, 8, 5, 7, 8, 10};
    int size = sizeof(arr)/sizeof(arr[0]);
    
    printf("Distinct items: %d",countDistinct(arr, size));
}
    