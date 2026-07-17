#As crianças da escola perto de sua casa estão aprendendo a contar e a professora pediu para você fazer um jogo para elas observarem uma contagem em ação.
#Seu programa deve ler um valor inteiro positivo e imprimir, um por linha, os valores entre 0 e o valor imediatamente anterior ao inteiro lido.

numero = int(input())

for i in range (numero):
    print(i)

#Seu jogo foi um sucesso e professora perdiu outra versão.
#Seu programa deve ler um valor inteiro positivo e imprimir, um por linha, os valores entre 1 e o inteiro lido, inclusive.

numero = int(input())

for i in range (numero):
    print(i+1)

#Sâo muitas as crianças do Ensino Fundamental que foram prejudicadas com a falta de escola presencial durante a pandemia. Para ajudar, você quer fazer um programa que gera tabuadas para elas treinarem.
#Dado um número entre 1 e 11, imprimir os valores da tabulada para multiplicações de 1 a 11

numero = int(input())
tab = 11

if numero>11 or numero <=0:
    print("digite um numero entre 1 e 11")

for i in range (tab):
    print((i+1)*numero)

#Que delícia que é pode ajudar as crianças! Elas querem mais e mostram o que querem!

#Elas fornecem três linhas e deram exemplos de como querem que seu programa informe a saída para eles estudarem :

#primeira linha: numero do qual queremos calcular a tabuada (valor entre 1 e 99)
# segunda linha: primeiro valor da tabuada a ser gerado (valor entre 1 e 999)
# terceira linha: último valor da tabuada a ser gerado (valor entre 1 e 999)

num = int(input())
inic = int(input())
fim = int(input())
print("tabuada do", num, "de", inic, "até", fim) 

while inic <= fim:
    for i in range ((fim-inic)+1):
        i = num * inic
    inic = inic + 1
    print(num, "X", inic-1, "=", i)

#Bora enrolar? enrolar o quê? qualquer coisa: você define!
#dados o nome do que você vai enrolar, e o números de vezes que você vai enrolar, você deve.. enrolar! mostrando a cada passo o que você está enrolando ;-)

coisa = input()
vezs = int(input())

for i in range(vezs):
    print("enrolando", coisa, i+1)

#Desenhar é legal. Programar é legal. Desenhar programando é mais legal ainda.
#Dado um inteiro N, imprima uma grade N×N de símbolos com um espaço entre eles. Nas duas diagonais, você imprime +; nas demais posições você imprime *

numero = int(input())

linha_inicial = ""

for i in range(numero * numero):
    linha = i // numero
    coluna = i % numero
    if linha == coluna or linha + coluna == numero - 1:
        simbolo = "+"
    else:
        simbolo = "*"
    linha_inicial = linha_inicial + simbolo + " "

    if coluna == numero - 1:
        print(linha_inicial)
        linha_inicial = ''

#A ONG que cuida de animais perto de sua casa estará fazendo uma feira de apresentação de animais que precisam de tutores. Nem todo mundo consegue adotar um bicho carente, mas consegue fazer doações em moedas. E você pode ajudar fazendo um programa que conte o valor recebido.
# Dado o número de moedas e o valor de cada moeda, informe o valor recebido.

moed = int(input())
total = 0

for i in range(moed):
    total = total + float(input())
print(total)

#Dado um número de apostas realizadas por uma pessoa e o valor de cada uma, informe quanto a pessoa gastou com 'bets'

aposta = int(input())
total = 0

for i in range(aposta):
    total = total + float(input())
print(total)