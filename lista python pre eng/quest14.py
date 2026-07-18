id = int(input())

if id < 5:
    print("idade inválida")
elif id >= 5 and id <=7:
    print("categoria: infantil A")
elif id >= 8 and id <=10:
    print("categoria: infantil B")
elif id >= 11 and id <=13:
    print("categoria: juvenil A")
elif id >= 14 and id <=17:
    print("categoria: juvenil B")
else:
    print("categoria: sênior")
