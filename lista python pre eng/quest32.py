masc = 0 
fem = 0
x = 4
massa = 0
ida = 0

for i in range(x):
    print("indique o sexo da pessoa com M para masculino e F para feminino:")
    sex = input()
    if sex == "F":
        fem = fem + 1
        print("insira a massa da pessoa")
        massa += int(input())
    else:
        masc = masc + 1
        print('insira a idade da pessoa')
        ida += int(input())

if fem > 0:
    media_massa = massa / fem
else:
    media_massa = 0

if masc > 0:
    media_idade = ida / masc
else:
    media_idade = 0

print("total sexo masc:", masc)
print("total sexo fem:", fem)
print("média de idade do sexo masc:", media_idade)
print("média de massa do sexo feminino:", media_massa)