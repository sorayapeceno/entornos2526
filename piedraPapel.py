import random
apuestaHumana = int(input("Introduce 1 para Piedra, 2 para Papel o 3 para Tijera"))

apuestaMaquina = random.randint(1,3)
print("Maquina",apuestaMaquina)
print("Humana",apuestaHumana)

