num = int(input())
i = 1
div = 0

while i <= num:
    if num%i==0:
        div=div+1
    i = i + 1
if div == 2:
    print('primo')
else:
    print('não é primo')