quant = int(input())
maior = 0

for i in range(quant):
    num = int(input())
    if num > maior:
        maior = num
print(maior)