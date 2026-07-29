#include <stdio.h>

int main(){

    int tamanho; 
    float v[tamanho], q[tamanho];

    printf("digite a quantidade de numeros que voce queer entre 1 e 20:\n");
    scanf("%d", &tamanho);

    while(tamanho <= 0 || tamanho > 20){
        printf("quantidade invalida, por favor digite um valor entre 1 e 20:\n");
        scanf("%d", &tamanho);
    }

    int i;

    for(i=0; i<tamanho; i++){
        printf("digite o valor %d:\n", (i+1));
        scanf("%f", &v[i]);
    }
    for(i=0; i<tamanho; i++){
        printf("%f\n", v[i]);
    }
    for(i=0; i<tamanho; i++){
        q[i] = v[i]*v[i];
        printf("%f\n", q[i]);
    }

    printf("fim");

    return 0;
}