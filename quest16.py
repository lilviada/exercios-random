ano = int(input())

if ano % 100 == 0:
    if ano % 400 ==0:
        print("bissexto")
    else:
        print("não é bissexto")
else:
    if ano % 4 == 0:
        print("bissexto")
    else:
        print("não é bissexto")

