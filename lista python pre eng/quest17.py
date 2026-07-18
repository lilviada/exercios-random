sal = float(input())

if sal <= 900:
    print(sal)
elif sal > 900 and sal <= 1500:
   sal = (sal*92)/100
   print("%.2f" % sal) 
elif sal > 1500 and sal <= 2500:
    sal = (sal*90)/100
    print("%.2f" % sal) 
else:
    sal = (sal*88)/100
    print("%.2f" % sal) 
