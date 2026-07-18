quant = int(input())
nota = 0

for i in range(quant):
    nota = nota + int(input())
nota = nota/quant

if nota < 4:
    print('média:', nota, 'reprovado :(')
elif nota >= 4 and nota < 7:
    print('média', nota, "AF")
else:
    print('média', nota, "pasou pabens")