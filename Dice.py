import random

print("Juego de dados(2)")
dadoCarmen1 = random.randint(1, 6)
dadoCarmen2 = random.randint(1, 6)
print("Carmen ha sacado un " + str(dadoCarmen1) + " y un " + str(dadoCarmen2))
dadoDavid1 = random.randint(1, 6)
dadoDavid2 = random.randint(1, 6)
print("David ha sacado un " + str(dadoDavid1) + " y un " + str(dadoDavid2))
sumaCarmen = dadoCarmen1 + dadoCarmen2
sumaDavid = dadoDavid1 + dadoDavid2
if sumaCarmen>sumaDavid:
    print("Ha ganado Carmen")
elif sumaDavid==sumaCarmen:
    print("Han empatado")
else:
    print("Ha ganado David")
