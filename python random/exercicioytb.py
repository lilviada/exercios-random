#criar um programa que peça o primiero termo e a razão de uma PA e com base nisso imprima 
# os 10 primeiros termos da PA e continue pedindo a quantidade de termos que o usuario quer
# ver posteriores aos que ja foram impressos. quando o usuario digitar 0 o programa 
#  imprime a quantidade de termos que foram impressos

termo = float(input('primeiro termo: '))
razao = float(input('razão da PA: '))
soma = 0

for i in range (10):
    print(termo, "→", end=" ")
    termo = termo + razao
    soma += 1
print('pausa')
quant = 1
while quant != 0:
    quant = int(input('quantos termos voce quer mostrar a mais? ' ))
    for i in range(quant):
        print(termo, "→", end=" ")
        termo = termo + razao
        soma += 1
    print('pausa')
print(f'progressão finalizada com {soma} termos mostrados')

