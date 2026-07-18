a = int(input())
b = int(input())
c = int(input())

delta = (b*b) - 4 * a * c

if delta < 0:
    print("não possui raízes reais")
elif delta == 0:
    x = ((b*-1) + (delta**0.5)) / (2*a)
    print(x)
else:
    x1 = ((b*-1) + (delta**0.5)) / (2*a)
    x2 = ((b*-1) - (delta**0.5)) / (2*a)
    print(x1, x2) 