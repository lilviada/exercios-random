num = int(input())

if num < 0:
    print('erro')
elif num == 0:
    print('1')
else:
    n = num - 1
    while n >= 1:
        num = num * n
        n = n - 1
    print(num)
