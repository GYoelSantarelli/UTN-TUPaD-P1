"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

numero = input("Ingresa un número entero: ")

if numero[0] == '-':
    numero_invertido = '-' + numero[:0:-1]
else:
    numero_invertido = numero[::-1]

print("Número invertido: ", numero_invertido)