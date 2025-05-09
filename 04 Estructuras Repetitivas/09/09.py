"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

total_num = 100

suma = 0

print(f"Ingresa {total_num} números enteros: ")

for i in range(total_num):
    numero = int(input("Números: "))
    suma += numero

media = suma / total_num

print(f"La media de los valores ingresados es : {media}")