# Función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Programa principal
if __name__ == "__main__":
    
    base = float(input("Ingresa la base (número real): "))
    exponente = int(input("Ingresa el exponente (entero no negativo): "))

    if exponente < 0:
        print("Por favor, ingresa un exponente entero no negativo.")
    else:
        resultado = potencia(base, exponente)
        print(f"{base}^{exponente} = {resultado}")