pesos = int(input("What do you have left in pesos? "))
soles = int(input("What do you have left in soles? "))
reais = int(input("What do you have left in reais? "))

total = (pesos * 0.00025) + (reais * 0.18) + (soles * 0.29)
print(total)
