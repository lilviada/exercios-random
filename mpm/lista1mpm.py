#Na chamada da sua escola, uma professora fala seu nome completo, juntando primeiro nome, nome do meio, e sobrenome.
#Já outra professora chama apenas seu primeiro nome e o sobrenome.
#Dadas três linhas contendo respectivamente seu nome, nome do meio e sobrenome, imprima duas linhas correspondentes 
#a como cada uma das suas duas professoras fazem.

print("digite o primeiro nome:")
prinnome = input()
print("digite o nome do meio:")
meionome = input()
print("digite o sobrenome")
sobrenome = input()

print(prinnome, meionome, sobrenome)
print(prinnome, sobrenome)

#Quando vai chegando o aniversário, sempre vem aquela pergunta: "Quantos anos você vai fazer?"
# Dados:
# o nome de uma pessoa na primeira linha
# a idade atual ao na segunda linha (número inteiro)
# Calcule a idade após o próximo aniversário e imprima uma mensagem personalizada.

print("digite seu nome")
nome = input()
print("digite sua idade atual")
idade = int(input())

aniversario = idade + 1


print(nome, "vai completar", aniversario, "anos")

#Você está em um local onde todo mundo está esperando para ser atendido. O local é organizado e todo mundo tem uma senha em papel.
# Você sabe que a chamada, mostrada em um grande painel, é feita em ordem crescente no número da senha para respeitar a ordem de chegada
# como em uma fila organizada...
# Dada uma linha com o número mostrado no painel, calcule qual o próximo a ser chamado.

print("digite a senha que está no painel")
senha = int(input())

print("a próxima senha a ser chamada será:", senha + 1)

#Na mesma fila controlada por senhas, você está segurando o papel com seu número e está alerta para quando será a sua vez...
#Dada uma linha com número da sua senha, calcule qual o número que vai estar no painel imediatamente antes de você ser chamada.

print("digite sua senha")
senha = int(input())

print("a senha imediatamente antes da sua é:", senha - 1)

#Na mesma fila controlada por senhas, você está segurando o papel com seu número e quer saber quantos faltam para a sua vez... você vê no painel um número anterior ao seu....
#Dada uma linha com o número mostrado no painel, e o número da sua senha em outra linha, calcule quantos faltam para a sua vez

print("digite sua senha:")
senha = int(input())
print("digite a senha que está no painel:")
painel = int(input())

restante = senha - painel

if restante < 0:
    restante = restante * -1
    print("há", restante, "senhas na sua frente")
else:
    print("há", restante, "senhas na sua frente")

#Sabe como a nota da redação do ENEM é calculada?
#Primeiro, cada pessoa corretora dá notas de 0 a 200 para cada uma das 5 competências, que podem totalizar até 1000 pontos.
#Dadas as cinco notas de uma pessoa corretora, calcule a pontuação total dessa pessoa corretora.

print("digite sua nota na competência 1:")
c1 = int(input())
print("digite sua nota na competência 2:")
c2 = int(input())
print("digite sua nota na competência 3:")
c3 = int(input())
print("digite sua nota na competência 4:")
c4 = int(input())
print("digite sua nota na competência 5:")
c5 = int(input())

total = c1 + c2 + c3 + c4 + c5

print("o total da sua nota foi:", total)

#Quando criamos um PIN, todo mundo já ouviu que não é seguro usar datas óbvias, como o ano de nascimento de pessoas próximas. Mas existe uma forma divertida de transformar anos importantes em um PIN um pouco menos frágil.
#Considere utilizar, por exemplo, o ano de duas datas importantes para você sem ser aniversários de ninguém próximo. Por exemplo, o ano em que você aprendeu a andar de bicicleta ou a jogar xadrez. Esses dois anos são importantes para a sua história e não fazem parte de documento algum. Quando você soma os dois, você obtém um número menos óbvio que pode servir como inspiração para um PIN.
#Dados dois valores de anos em duas linhas diferentes, informe o PIN resultante do uso a estratégia indicada.

print("um ano relevante na sua vida que não seja uma data de aniversário:")
ano1 = int(input())
print("pensa em outro e digita mo")
ano2 = int(input())

pin = ano1 + ano2

print("um pin massa pra tu usar:", pin)

#Quando alguém diz: "Chego em 91 minutos", imediatamente pensamos que o valor equivale a 1 hora e 31 minutos
#Dado um número inteiro representando minutos, calcule o valor de horas e minutos, e imprima os dois valores linhas separadas

print("digite a quantidade de minutos:")
total = int(input())

horas = total//60
minutos = total%60

print(total, "minutos equivalem a", horas, "horas e", minutos, "minutos")

#Em várias situações do dia a dia precisamos fazer contas rápidas, por exemplo para calcular o troco do supermercado, o placar de um jogo, ou tempo que falta para concluir uma tarefa.
# 
# Dado dois números inteiros, você deve calcular e mostrar:

#a soma
#a subtração
#a multiplicação
#a potência (primeiro número elevado ao segundo)
#a divisão inteira
#o resto da divisão inteira
#a divisão com casas decimais, mostrando apenas uma casa decimal.
#Você pode assumir que nunca será dado um valor nulo no denominador, ok?

