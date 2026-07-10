#include <stdio.h>

int main()
{
   int a=0;
   int b=1;
   int contador=2;
   int termo;
   int i=0;
   
   printf("digite o termo que quer descobrir:\n");
   scanf("%d",&termo);
   
   if(termo==2){
       printf("o 2 termo da sequência de fibonacci é: 1");
   }
   
   else{
   for(contador=2; contador<termo; ){
       i=a+b;
       a=b;
       b=i;
       contador+=1;
   }
   
   printf("o %d termo da sequência de fibonacci é: %d\n", termo, i);
   }

    return 0;
}
