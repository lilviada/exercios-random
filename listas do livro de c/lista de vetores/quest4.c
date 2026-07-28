#include <stdio.h>

int main(){

    int v[] = {1, 0, 5, -2, -5, 7};

    int soma = v[0] + v[1] + v[5];

    printf("soma: %d\n", soma);

    v[3] = 100;
    int i;

    for(i=0;i<6;i++){
        printf("%d\n", v[i]);
    }

    return 0;
}