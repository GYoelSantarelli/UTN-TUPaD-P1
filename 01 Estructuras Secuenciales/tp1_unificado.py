''' 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.'''

print (f"Hola Mundo!")

''' 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.'''

nombre = input("Ingrese su nombre: ")
print (f"Hola {nombre}!")

''' 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.'''

nombre = input("Ingrese su numbre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

'''4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.'''

import math
pi = math.pi
radio = float(input("Ingrese el radio del círculo: "))
area = pi * ( radio ** 2 )
perimetro = 2 * pi * radio

print(f"El area del círculo es: {area}")
print (f"El perimetro del círculo es: {perimetro}")

'''5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.'''

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos/3600

print(f"{segundos} segundos equivalen a {horas} horas")

'''6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.'''

numero = int(input("Ingrese un numero: "))
print (f"La tabla de multiplicar por {numero} es: ")

for i in range (11):
    print(f"{numero} x {i} = {numero * i}")

'''7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.'''

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

'''8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:
𝐼𝑀𝐶 =
𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚) al cuadrado
'''
altura = float(input("Ingrese su altura expresada en metros: "))
peso = float(input("Ingrese su peso indicado en kilogramos: "))
masaCorporal = round(peso / altura**2, 2)

print(f"Su indice de masa corporal es de {masaCorporal}")

'''9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:'''

celsius = float(input("Ingrese la temperatura en celsius: "))
fahrenheit= round( 9/5* celsius + 32)

print(f"{celsius} °C equivalen a {fahrenheit} °F.")

'''10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.'''

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

promedio = (n1 + n2 + n3) / 3

print (f"Sus números son: {n1}, {n2}, {n3} y el promedio es: {promedio}")