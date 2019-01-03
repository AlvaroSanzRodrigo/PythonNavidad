import random

print("Juego del quince")

dadoCarmen1 = random.randint(1, 10)
dadoCarmen2 = random.randint(1, 10)
dadoCarmen3 = random.randint(1, 10)
print("Gloria ha sacado un " + str(dadoCarmen1) + ", " + str(dadoCarmen2) + " y " + str(dadoCarmen3))
dadoDavid1 = random.randint(1, 10)
dadoDavid2 = random.randint(1, 10)
dadoDavid3 = random.randint(1, 10)
print("Héctor ha sacado un " + str(dadoDavid1) + ", " + str(dadoDavid2) + " y " + str(dadoDavid3))
sumaCarmen = dadoCarmen1 + dadoCarmen2 + dadoCarmen3
sumaDavid = dadoDavid1 + dadoDavid2 + dadoDavid3

if sumaCarmen > 15:
    print("Gloria saca más de 15 así que pierde")
elif sumaDavid > 15:
    print("Héctor saca más de 15 así que pierde")
elif sumaDavid > sumaCarmen:
    print("Gana Héctor")
else:
    print("Gana Gloria")