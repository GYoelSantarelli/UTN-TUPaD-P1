"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

numero = int(input("Ingrese un número positivo: "))

if numero > 0:
    suma = 0
    for i in range (0, numero + 1):
        suma += i
    print (f"La suma de los números desde 0 hasta {numero} es: {suma}")
else:
    print(f"Debes ingresar un número positivo.")