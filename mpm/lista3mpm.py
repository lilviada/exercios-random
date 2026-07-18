#A professora do Ensino Infantil está ajudando seus alunos a entenderem contagem. Ela pediu sua ajuda para demonstrar o conceito por meio de exemplos:
# a professora fornece vários nomes de animais e as crianças têm que contar quantos são
# a professora indica que a lista acabou com a frase 'final feliz'
# seu programa deve ler os nomes até a frase final, e informar quantos nomes foram lidos antes da frase final.

animal = input()
contador = 0 

while animal != "final feliz":
    animal = input()
    contador = contador + 1
print(contador)

#A professora do Ensino Fundamental está ajudando seus alunos a entenderem valores pares e ímpares. Ela pediu sua ajuda para demonstrar os conceitos por meio de exemplos:
# a professora fornece vários valores positivos e termina com um valor negativo para indicar o término da entrada
# o programa deve infomar quantos valores pares e quantos valores ímpares foram lidos antes da condição de término

num = 1
par = 0
impar = 0

while num > 0:
    num = int(input())
    if (num % 2) == 0:
        par = par + 1
    else:
        impar = impar + 1

print("pares:", par, "impares:", (impar-1))

#Você ficou encarregada de programar uma nova linha de robôs que possuem um cesto para fazer feira: as pessoas vão à feira e o robô segue atrás. Na feira, as pessoas vão comprando frutas, legumes e verduras, que são colocados no cesto do robô.
# Cada modelo na nova linha de robôs tem um peso máximo que consegue carregar. Quando esse peso máximo é alcançado ou superado, o robô deve avisar. Se o peso total for igual à capacidade do robô, o último item pode permanecer no cesto. Se o peso total ultrapassar a capacidade, o último item deve ser retirado.
# Dada a capacidade de um modelo de robô de feira, seu programa deve aceitar pesos de itens até que a capacidade seja alcançada ou superada. Quando isso acontecer, o programa deve imprimir a mensagem correta.

print("digite a capacidade do robô:")
cap = int(input())
total = 0

while total < cap:
    total = total + int(input())

if cap<total:
    print("Fim de feira: levo tudo menos o último item")
else:
    print("Fim de feira: levo tudo mas não cabe mais nada")

#A professora do Fundamental está ensinando as crianças que existem números positivos, que existe o valor nulo, e que existem números negativos. Ela pediu sua ajuda para fazer um programa que recebe valores inteiros de entrada até que seja dado um valor negativo, e informa quantos valores positivos foram lidos.

num = 0
contador = 0

while num >= 0:
    num = int(input())
    if num > 0:
        contador = contador + 1
print(contador)
     
#As monitoras têm que procurar os nomes das alunas nas listas de presença para marcar frequência e você topou ajudar! Dado um nome alvo em uma linha inicial, seu programa deve ler nomes em novas linhas até que um nome igual ao alvo seja dado, e informar quantos nomes foram lidos antes do alvo.

contador = 0
alvo = input()
nome = input()

if alvo == nome:
    print(contador)
else:
    contador = contador + 1

while nome != alvo:
    nome = input()
    contador = contador + 1

contador = contador - 1
print(contador)

#A professora está estudando a diferença salarial entre homens e mulheres em uma mesma função. Para isso, ela pediu sua ajuda para criar um programa que leia pares de salários, sendo sempre o salário do homem primeiro e o da mulher em seguida. A leitura termina quando o par -1 e -1 for informado.
#O programa deve contar quantos pares indicam igualdade salarial entre homem e mulher naquela posição, e imprimir esse total.

print("digite o salario do home")
hom = float(input())
print("digite o salario da muler")
mul = float(input())

conatdor = 0

while hom and mul >= 0:
    hom = float(input())
    mul = float(input())
    if hom == mul:
        conatdor = conatdor +1
else:
    conatdor = conatdor

print(conatdor)

#Muitas vezes a gente tem uma quantidade de massa para pão de queijo e não sabe exatamente quantos pães vamos conseguir enrolar. Seu programa ajuda você a registrar quantos paes você conseguiu enrolar, como no exemplo.

contador = 0
pao = input()
if pao != "pao":
        print("muler isso n eh pao, digita direito cachorra")
else:
      contador  = contador + 1

while pao != "fim":
    pao = input()
    if pao != "pao":
        print("muler isso n eh pao, digita direito cachorra")
    else:
        contador  = contador + 1
print(contador)

#A professora do Ensino Fundamental está ajudando seus alunos a entenderem como funcionam operações de entrada e saída em um caixa de banco. Ela pediu sua ajuda para criar um programa que leia valores numéricos representando essas operações:

#Valores positivos representam depósitos.
#Valores negativos representam saques.
#A leitura termina quando for digitado o valor 0.
#O programa deve calcular e imprimir o saldo final ao fim do dia.

saldo = 0
mov = float(input())

if mov > 0:
    saldo = saldo + mov
elif mov < 0:
    saldo = saldo - mov

while mov != 0:
    mov = float(input())
    saldo = saldo + mov
print(saldo)

