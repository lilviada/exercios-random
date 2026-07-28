#include <stdio.h>

int main(){

    float v[10];
    int i;
    for(i=0; i<10;i++){
        scanf("%f", &v[i]);
    }
    int x, y;
    scanf("%d %d", &x, &y);
    if(x<0 || x>9 || y<0 || y>9 ){
        printf("erro");
    }
    else{
        float soma = v[x] + v[y];
        printf("%f", soma);
    }

    return 0;
}