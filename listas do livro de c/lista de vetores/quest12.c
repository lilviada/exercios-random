#include <stdio.h>

int main(){

    int v[10], w[10];
    int i, j;

    for(i=0;i<10;i++){
        scanf("%d", &v[i]);
    }

    for(i=0; i<9;i++){
        for(j=i+1; j<10;j++){
            if(v[i] == v[j]){
                printf("%d\n", v[i]);
        }

        }
    }


    return 0;
}