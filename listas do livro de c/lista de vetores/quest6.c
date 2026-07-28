#include <stdio.h>

int main(){
    int v[10];
    int i, soma = 0;
    for(i=0; i<10;i++){
        scanf("%d", &v[i]);
        if(v[i]%2==0){
            soma ++;
        }
    }
    printf("%d", soma);

    return 0;
}