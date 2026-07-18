#O tempo todo a equipe do projeto MPM.PPM precisa mostrar o impacto de suas ações voluntárias para que o projeto posso continuar.
# Para compreender melhor a escala desse esforço, considere o número total de voluntárias, o número de monitorias que cada uma ofertou, e o número médio de alunas que participou cada monitoria.
# Escreva um programa que leia esses três valores e informe o número total de atendimentos nas monitorias.

volu = int(input())
moni = int(input())
alu = int(input())

total = volu * moni * alu

print(total)

#As voluntárias do projeto MPM.CF2 se organizam para que sempre tenha uma volunária atendendo alunas em cada um dos dias da semana: impressionante né?

#As alunas que fazem o MPM.CF2 sabem que devem participar de pelo menos 3h de monitoria por semana, e você quer ajudar! Dado o número de minutos que uma aluna participou de monitoria em uma semana, você deve fazer um programa verifica se a aluna fez o suficiente, ficou devendo ou fez a mais.

min = int(input())

if min == 180:
    print("suficiente")
elif min < 180:
    print("ficou devendo")
else:
    print("fez a mais")

#O curso MPM.CF2 tem aulas semanais, e alguém tem que controlar a presença das alunas durante o curso todo. A cada momento, a coordenação pode precisar consultar quantas alunas estiveram presentes em cada aula, por exemplo, para informar aos orgãoes competentes. Para ajudar a equipe de voluntárias, você deve fazer um programa que, dado o número de semanas já ocorridas, leia o número de alunas presentes em cada aula e informe o número total de presenças.

sema = int(input())
alu = 0

for i in range(sema):
    alu = alu + int(input())

print(alu, "presenças em", sema, "aulas")

#Cada vez que uma aluna acerta um exercício, as voluntárias ficam muito muito muito felizes: as voluntárias corrigem os exercícios e comemoram a cada acerto. Seu programa deve ler o número de exercicios corretos que cada monitora vai corrigindo e, no final, verificar quantas vezes elas comemoraram. O final da correção é indicado por um valor negativo.

entrada = int(input())
              
if entrada <=0:
    print("acertos: 0")
else:
    acertos = entrada
    while entrada >= 0:
        entrada = int(input())
        acertos = acertos + entrada
    print("corretos:", acertos + 1)