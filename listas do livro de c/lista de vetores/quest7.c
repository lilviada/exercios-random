#include <stdio.h>

int main(){
    int x[10];
    int i, menor, maior;

    for(i=0;i<10;i++){
        scanf("%d", &x[i]);
        if(x[i] < menor){
            menor = x[i];
        }
        if(x[i]>maior){
            maior = x[i];
        }
    }
    printf("%d %d", menor, maior);

    return 0;
}