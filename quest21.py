a = 80000
b = 200000
ano = 0
while a < b:
    a = a + (a*3)/100
    b = b + (b*1.5)/100
    ano = ano + 1
print(ano)