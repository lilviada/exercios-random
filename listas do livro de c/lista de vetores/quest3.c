#include <stdio.h>

int main(){

    float v[5];
    int i;
    float soma = 0, media;

    for(i=0;i<5;i++){
        scanf("%f", &v[i]);
        soma += v[i];
    }
    media = soma / 5;

    for(i=0; i<5; i++){
        printf("%f\n", v[i]);
    }
    printf("%f", media);

return 0;
}