x = int(input())
y = int(input())
pot = 0
a = y

while a > 1:
    pot += x*x
    a -= 1
print(x, "elevado a", y, "é", pot)
