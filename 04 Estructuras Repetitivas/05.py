"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
import random

num_random = random.randint(0,9)
intentos = 0
adivinanza = -1

print ("Adivina el número entre 0 y 9")

while adivinanza != num_random:
    adivinanza = int(input("Ingresa cual crees que es el número: "))
    intentos += 1

print(f"Correcto!! El numero era {num_random}")
print(f"Número de intentos: {intentos}")