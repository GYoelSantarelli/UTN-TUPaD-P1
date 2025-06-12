def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
if __name__ == "__main__":
        
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius:.2f}°C equivalen a {fahrenheit:.2f}°F")