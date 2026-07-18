x = 100

for i in range(x):
    print("insira o codigo do funcionario")
    cod = input()
    print("digite o numero mensal de horas trabalhadas")
    hora = int(input())
    print("insira o turno de trabalho do funcionario")
    tur = int(input())
    while tur < 1 or tur > 3:
        print("turno invalido digite novamente")
        tur = int(input())
    print("digite a caegoria do funcionario")
    cat = int(input())
    while cat < 8 or cat > 9:
        print("categori invalida, digite novamente")
        cat = int(input())
    print("digite o valor da hora de serviço do funcionário")
    valor = float(input())
    sal = hora * valor
    print("o funcionario", cod, "deve receber", sal, "reais de salario esse mes")