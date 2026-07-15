#O programa recebe como entrada três linhas:
# a primeira pode conter um entre os seguintes valores: + - * / // % **
# as duas linhas seguintes contêm um inteiro cada
# A saída da é uma linha com o resultado da operação envolvendo os dois valores inteiros dados

print("digite o simbolo da operação qu evc quer fazer:")
op = input()
print("digite o primeiro valor inteiro:")
n1 = int(input())
print("digita o segundo aff:")
n2 = int(input())

if op == "+":
    soma = n1 + n2
    print("a soma é", soma)
elif op == "-":
    sub = n1 - n2
    print("subtrasao é:", sub)     
elif op == "*":
    mult = n1 * n2
    print("mutiplicasao é:", mult)
elif op == "/":
    div = n1/n2
    print("a divissao nao exatda:", div)
elif op == "//":
    div = n1//n2
    print("a divisao exata é", div)
elif op == "%":
    div = n1%n2
    print("o resto da divisao é:", div)
elif op == "**":
    pot = n1**n2
    print("a potecsia:", pot)
else:
    print("nao foi possivel realizar a operacao") 

#Uma pessoa está fazendo uma compra por um site Web. Ela colocou um conjunto de itens no carrinho de compras, e vai pagar a compra com PIX.
# Essa pessoa decidiu nunca gastar mais do ela realmente tem.
# Seu programa deve ler duas linhas, com um valor inteiro cada. O primeiro valor corresponde ao valor em dinheiro que a pessoa tem na conta do banco. O segundo valor corresponde ao total calculado no carrinho de compras.
# Seu programa deve verificar se a pessoa pode ou não realizar a compra de modo a respeitar sua própria decisão, e emitir mensagens correspondentes:
# se o saldo for suficiente, informar 'pode comprar tudo'
# caso contrário, informar 'saldo insuficiente'

print("digite o saldo na sua conta:")
saldo = float(input())
print("digite o valor da compra que quer fazer:")
compra = float(input())

if (saldo - compra) >= 0:
    print("pode comprar tudo")
else:
    print("saldo insuficientekkkk")

# Uma pessoa está fazendo uma compra por um site Web. Ela colocou um conjunto de itens no carrinho de compras, e vai pagar a compra com PIX.
# Essa pessoa decidiu nunca gastar mais do ela realmente tem.
# Seu programa deve ler duas linhas, com um valor inteiro cada.
# o primeiro valor corresponde ao valor em dinheiro que a pessoa tem na conta do banco
# o segundo valor corresponde ao total calculado no carrinho de compras.
# Seu programa deve verificar se a pessoa pode ou não realizar a compra de modo a respeitar sua própria decisão, e emitir mensagens correspondentes.
# Caso a compra não deva ser efetuada para respeitar a decisão, informar 'seu saldo é insuficiente para essa compra'
# Caso a compra possa ser efetuada respeitando a decisão, informar o novo saldo caso a compra seja de fato realizada

print("digite o saldo na sua conta:")
saldo = float(input())
print("digite o valor da compra que quer fazer:")
compra = float(input())

if (saldo - compra) >= 0:
    print("pode comprar tudo. seu saldo após a compra será:", (saldo - compra))
else:
    print("seu saldo é insuficiente para essa compra")

#As teclas A S W D são parte importante de qualquer jogo que utilize o teclado.
# (Quase) Todo mundo sabe que elas correspondem a teclas de direção e sentido.
# Seu programa deve ler um valor correspondente a uma tecla (como uma string, ou seja, usando diretamente o resultado da função input())
# A seguir, seu programa deve identificar se o valor lido corresponde uma das teclas A S W D, que podem ser digitadas com letra minúsculas ou maiúsculas.
# se for uma dessas teclas, informar qual é, em inglês e em letras maísculas
# w e W produzem UP
# s e S produzem DOWN
# a e A produzem LEFT
# d e D produzem RIGHT
# Se nao for uma das letras esperadas, seu programa responde com um ponto de interrogação

tecla = input()

if tecla == "w" or "W":
    print("UP")
elif tecla == "s" or "S":
    print("DOWN")
elif tecla == "a" or "A":
    print("LEFT")
elif tecla == "d" or "D":
    print("RIGHT")
else:
    print("?")

#Seu programa deve ler um valor inteiro correspondente à idade de uma pessoa e, caso a idade seja igual ou maior que 60, informar a idade seguida de 'Melhor idade!'
# Independentemente da idade lida, o programa deve concluir com a mensagem 'Fim'

print("digite sua idade:")
idade = int(input())

if idade < 60:
    print(idade, "é uma idade legal")

else:
    print(idade, "é a melhor idade")

print("fim")  

#Seu programa deve receber duas strings, uma por linha.
# Se ambas forem 'V, o programa deve exibir a resposta 'VV'
# Se ambas as entradas forem 'F', o programa deve exibir a resposta 'FF'
# Se nenhuma dessas condições for atendida, o programa deve exibir a resposta '?' para indicar uma resposta desconhecida.

x = input()
y = input()

if x == "V" and y == "V":
    print("VV")
elif x == "F" and y == "F":
    print("FF")
else:
    print("?")

#Dada a enorme importância do sono, seu programa deve orientar um usuário adulto que informa quantas horas de sono teve na noite anterior.
# Exemplos de entrada e saída para seu programa:
# 8.1 produz "Você dormiu muito bem, parabéns!"
# 8 produz "Você dormiu o suficiente, continue assim!"
# 7.9 produz "Você precisa de mais tempo de sono, cuide-se!"

print("informe sua quantidade de horas de sono:")
sono = float(input())

if sono > 8:
    print("Você dormiu muito bem, parabéns!")
elif sono == 8:
    print("Você dormiu o suficiente, continue assim!")
else:
    print("Você precisa de mais tempo de sono, cuide-se!")

#Atenção: para resolver este problema, você deve usar no máximo uma comparação básica (apenas um if-else)
# Dados dois valores inteiros, sua tarefa é identificar qual é o maior e qual é o menor

print("digite o primeiro valor:")
n1 = int(input())
print("digite o segundo valor:")
n2 = int(input())

if n1 > n2:
    print(n1, "é maior que", n2)
else:
    print(n2, "é maior que", n1)

#Este exercício nos convida a refletir o quanto aprendermos quando realizamos uma única comparação e quando realizamos uma sequência de comparações
# Você deve ler a idade de três irmãs, uma por linha
# e informar qual a mais velha

print("digite a idaede da primeira irmã")
n1 = int(input())
print("digite a idade da segunda irmã")
n2 = int(input())

if n1 > n2:
    velha = n1
elif n1 < n2:
    velha = n2

print("digite a idade da terceira irmã")
n3 = int(input())

if n3 > velha:
    print("a terceira irmã é a mais velha")
elif n1 > n2:
    print("a primeira irmã é a mais velha")
elif n1 < n2:
    print("a segunda irmã é a mais velha")   

#Você deve ler a idade de quatro irmãs, uma por linha, e informar
#qual a mais velha
#qual a mais nova

print("digite a idaede da primeira irmã")
n1 = int(input())
print("digite a idade da segunda irmã")
n2 = int(input())

if n1 > n2:
    velha1 = n1
    nova1 = n2
elif n1 < n2:
    velha1 = n2
    nova1 = n1


print("digite a idade da terceira irmã")
n3 = int(input())
print("digite a idade da quarta irmã")
n4 = int(input())

if n3 > n4:
    velha2 = n3
    nova2 = n4
elif n4 > n3:
    velha2 = n4
    nova2 = n3

if velha1 > velha2:
    if velha1 == n1:
        print("a primeira irmã é a mais velha")
    else:
        print("a segunda irmã é a mais velha")
else:
    if velha2 == n3:
        print("a terceira irmã é a mais velha")
    else:
        print("a quarta irmã é a mais velha")  

if nova1 < nova2:
    if nova1 == n1:
        print("a primeira irmã é a mais nova")
    else:
        print("a segunda irmã é a mais nova")
else:
    if nova2 == n3:
        print("a terceira irmã é a mais nova")
    else:
        print("a quarta irmã é a mais nova")           

#Seu programa deve ler uma letra e verificar a qual algarismo romano ela corresponde.
# responda o valor correspondente se for uma das entradas: I, V, X, L, C, D, M
# dê uma mensagem apropriada se o valor não for um dos valores acima

print("digite o algarismo:")
alg = input()

if alg == "I":
    print("esse algarismo equivale a 1")
elif alg == "V":
    print("esse algarismo equivale a 5")
elif alg == "X":
    print("esse algarismo equivale a 10")
elif alg == "L":
    print("esse algarismo equivale a 50")
elif alg == "C":
    print("esse algarismo equivale a 100")
elif alg == "D":
    print("esse algarismo equivale a 500")   
elif alg == "M":
    print("esse algarismo equivale a 1000")  
else:
    print("não comsigo reconhecer esse caractere")



