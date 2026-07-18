x = 5
exc = 0 
bom = 0
reg = 0
exid = 0
total = 0

for i in range(x):
    print("idade:")
    idade = int(input())
    print("opnião:")
    op = int(input())
    total += 1
    if op == 1:
        reg += 1
    elif op == 2:
        bom += 1
    elif op == 3:
        exid += idade
        exc += 1
    else:
        print("erro")
medex = exid // exc
perc = (100*bom)/total

print("media idade de excelente", medex)
print("quantidade regular:", reg)
print("porcentagem bom:", perc)

