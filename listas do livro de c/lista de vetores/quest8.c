#include <stdio.h>

int main(){
    int v[10];
    int i, soma = 0, neg;

    for(i=0;i<10;i++){
        scanf("%d", &v[i]);
        if(v[i]>0){
            soma += v[i];
        }
        if(v[i]<0){
            neg ++;
        }
    }
    printf("%d %d", soma, neg);

    return 0;
}