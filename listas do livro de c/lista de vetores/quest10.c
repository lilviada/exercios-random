#include <stdio.h>

int main(){

    int v[100];
    int i, num = 1;

    for(i=0; i<100; i++){
        if(num%7!=0){
            v[i] = num;
        }
        else{
            num++;
            v[i] = num;
        }
        num ++;
        printf("%d\n", v[i]);
    }

    return 0;
}