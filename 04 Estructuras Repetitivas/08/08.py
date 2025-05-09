"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe 
indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
(Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 
100 números con un solo cambio)."""

total_num = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingresa {total_num} números enteros:")

for _ in range(total_num):
    numero = int(input("Número: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)
