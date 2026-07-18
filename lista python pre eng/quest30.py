x = float(input())
y = float(input())

if x == 0 and y == 0:
    print("origem")
elif x == 0:
    print("eixo Y")
elif y == 0:
    print("eixo X")
elif x > 0 and y > 0:
    print("primeiro quadrante")
elif x < 0 and y > 0:
    print("seguundo quadrante")
elif x < 0 and y < 0:
    print("terceiro quadrante")
else:
    print("quarto quadrante")
