import random

print("Piedra Papel Tijera")
manos = ["piedra", "papel", "tijera"]
manoInes = random.randint(0, 2)
manoJuan = random.randint(0, 2)
ganador  = ""
print("Ines ha sacado " + manos[manoInes] + " y Juan " + manos[manoJuan])

if manoJuan == 0 and manoInes == 1:
    print("Ha ganado Ines")
elif manoJuan == 2 and manoInes == 1:
    print("Ha ganado Juan")
elif manoJuan == 0 and manoInes == 2:
    print("Ha ganado Juan")
elif manoJuan == 1 and manoInes == 2:
    print("Ha ganado Ines")
elif manoJuan == 1 and manoInes == 0:
    print("Ha ganado Juan")
elif manoJuan == 2 and manoInes == 0:
    print("Ha ganado Ines")
elif manoInes == manoJuan:
    print("Han empatado")
