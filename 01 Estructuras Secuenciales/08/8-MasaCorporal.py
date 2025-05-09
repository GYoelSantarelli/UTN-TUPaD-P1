altura = float(input("Ingrese su altura expresada en metros: "))
peso = float(input("Ingrese su peso indicado en kilogramos: "))
masaCorporal = round(peso / altura**2, 2)

print(f"Su indice de masa corporal es de {masaCorporal}")