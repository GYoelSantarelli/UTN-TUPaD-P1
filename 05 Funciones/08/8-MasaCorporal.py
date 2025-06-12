def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
if __name__ == "__main__":

    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")