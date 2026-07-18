a = int(input())
b = int(input())
c = int(input())

if a <= 0 or b <= 0 or c <= 0:
    print("erro")
else:
    if a == b == c:
        print("equilatero")
    elif a == b or b == c or c == a:
        print("isosceles")
    else:
        print("escaleno")
