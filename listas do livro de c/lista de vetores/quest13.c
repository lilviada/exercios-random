#include <stdio.h>

int main(){

    int v[10];
    int i, j;

    for(i=0; i<10; i++){
        scanf("%d", &v[i]);
        if(i>0){
            for(j=i-1; j<i;j++){
                if(v[i] == v[j]){
                    printf("este valor ja foi digitado anteriormente, digita outro:\n");
                    scanf("%d", &v[i]);
                }
            }
        }
    }
    
    for(i=0; i<10; i++){
        printf("%d\n", v[i]);
    }
    return 0;
}