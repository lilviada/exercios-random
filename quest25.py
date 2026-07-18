print("SELECIONE A ALTERNATIVA DA OPERAÇÃO QUE QUER REALIZAR: \nA) ADIÇÃO\nB) SUBTRAÇÃO\nC) MULTIPLICAÇÃO\nD) DIVISÃO")

op = input()

if op != "A" and op != "B" and op != "C" and op != "D":
    while op != "A" and op != "B" and op != "C" and op != "D":
        print("SELECIONE A ALTERNATIVA DA OPERAÇÃO QUE QUER REALIZAR: \nA) ADIÇÃO\nB) SUBTRAÇÃO\nC) MULTIPLICAÇÃO\nD) DIVISÃO")
        op = input()

else:
    print("digite o primeiro valor")
    n1 = float(input())
    print("digite o segundo valor")
    n2 = float(input())

    if op == "A":
        print(n1+n2)
    elif op == "B":
        print(n1-n2)
    elif op == 'C':
        print(n1*n2)
    else:
        print(n1/n2)


    