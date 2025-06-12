def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Programa principal
if __name__ == "__main__":

    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    promedio = calcular_promedio(a, b, c)
    print(f"El promedio de los tres números es: {promedio:.2f}")

