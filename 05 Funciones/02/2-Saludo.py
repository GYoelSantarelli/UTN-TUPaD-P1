def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
if __name__ == "__main__":
    nombre_usuario = input("Ingresa tu nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo)
