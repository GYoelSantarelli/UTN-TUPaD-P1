n1 = int(input("Ingrese un numero que no sea 0: "))
n2 = int(input("Ingrese un numero que no sea 0: "))
if n1 == 0 or n2 == 0:
    print("Uno de los números que ingresaste es 0, vuelve a introducir un número que nos sea 0")
suma = n1 + n2
resta = n1 - n2
division = n1 / n2
multiplicacion = n1 * n2

print(f"La suma de los dos números da: {suma}")
print(f"La resta de los dos números da: {resta}")
print(f"La división entre los dos números da: {division}")
print(f"La multiplicación entre los dos números da: {multiplicacion}")