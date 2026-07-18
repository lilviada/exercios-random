num = int(input())

a = ""
b = "+"
c = 0

for i in range(num):
    if c == i:
        print(a + b)
    c += 1
    a += "*"
    
