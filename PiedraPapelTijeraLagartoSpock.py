import random

print("Piedra Papel Tijera Lagarto Spock")
manos = ["piedra", "papel", "tijera", "lagarto", "spock"]
manoInes = random.randint(0, 4)
manoJuan = random.randint(0, 4)
ganador  = ""
print("Ines ha sacado " + manos[manoInes] + " y Juan " + manos[manoJuan])

if manoJuan == 0 and manoInes == 1:
    print("Ha ganado Ines")
elif manoJuan == 2 and manoInes == 1:
    print("Ha ganado Juan")
elif manoJuan == 3 and manoInes == 1:
    print("Ha ganado Ines")
elif manoJuan == 4 and manoInes == 1:
    print("Ha ganado Juan")

elif manoJuan == 0 and manoInes == 2:
    print("Ha ganado Juan")
elif manoJuan == 1 and manoInes == 2:
    print("Ha ganado Ines")
elif manoJuan == 3 and manoInes == 2:
    print("Ha ganado Juan")
elif manoJuan == 4 and manoInes == 2:
    print("Ha ganado Ines")

elif manoJuan == 1 and manoInes == 0:
    print("Ha ganado Juan")
elif manoJuan == 2 and manoInes == 0:
    print("Ha ganado Ines")
elif manoJuan == 3 and manoInes == 0:
    print("Ha ganado Juan")
elif manoJuan == 4 and manoInes == 0:
    print("Ha ganado Ines")

elif manoJuan == 1 and manoInes == 3:
    print("Ha ganado Juan")
elif manoJuan == 2 and manoInes == 3:
    print("Ha ganado Ines")
elif manoJuan == 0 and manoInes == 3:
    print("Ha ganado Ines")
elif manoJuan == 4 and manoInes == 3:
    print("Ha ganado Juan")

elif manoJuan == 1 and manoInes == 4:
    print("Ha ganado Ines")
elif manoJuan == 2 and manoInes == 4:
    print("Ha ganado Juan")
elif manoJuan == 0 and manoInes == 4:
    print("Ha ganado Juan")
elif manoJuan == 3 and manoInes == 4:
    print("Ha ganado Ines")

elif manoInes == manoJuan:
    print("Han empatado")
