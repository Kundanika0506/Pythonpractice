#include <stdio.h>
int main(){
    int n = 10;
    int a = 0;
    int b = 1;
    int c;
    printf("%d\n%d\n",a,b);

    for (int i = 2; i < n; i++){
        c = a + b;
        a = b;
        b = c;

        printf("%d\n",c);

    }
}