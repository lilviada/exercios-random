peixe = int(input())
excesso = peixe - 50
multa = excesso * 4

if excesso > 0:
    print("você excedeu", excesso, "quilos e terá de pagar", multa, "reais")
else: 
    print("você não execdeu o limite")