#include <stdio.h>
#include <math.h>

int main()
{
  int n = 10;
  int v[n], i;
  
  for (i = 0; i < 10; i++){ 
      printf("Digite o valor:\n");
      scanf("%d",&v[i]);
  }

float total = 0;
for(i=0;i<10;i++){
total += i;
}

float media = total/10;
float x = 0, y = 0, quad =0;

for(i=0;i<10;i++){

x = i - media;

quad = x*x;
y+=quad;

}

double vari =0;

vari = y/10;

double desvpad = 0;

desvpad = sqrt(vari);

printf("o desvio padrão da sequência digitada é: %lf\n", desvpad); 

    return 0;
}
