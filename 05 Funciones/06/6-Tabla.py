def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
if __name__ == "__main__":
    numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)