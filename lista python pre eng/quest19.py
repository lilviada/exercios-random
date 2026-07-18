num = int(input())
i = 1

if num <= 0:
    print("erro")
else:
    while i <= num:
        if i%2!=0:
            print(i)
        i = i+1