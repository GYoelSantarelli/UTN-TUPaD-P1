"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

numero = input("Ingrese un número entero: ")

if numero[0] == "-" :
    numero = numero[1:]
else:
    cantidad_digitos = len(numero)

print(f"El número tiene {cantidad_digitos} dígito(s).")