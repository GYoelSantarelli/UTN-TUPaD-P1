"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

inicio = int(input ("Ingrese el primer número entero: "))
fin = int(input ("Ingrese el segundo número entero: "))

if inicio > fin:
    inicio, fin = fin, inicio

suma = 0
for i in range (inicio + 1, fin):
    suma += i
print(f"La suma de los numeros entre {inicio} y {fin} es: {suma}")