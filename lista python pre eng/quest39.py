a = 1
b = 1
contador = 2
i = 0

termo = int(input())

if termo==1 or termo == 2:
    print("1")
else:
    while contador < termo:
        i = a + b
        a = b
        b = i
        contador+=1
    print(i)
