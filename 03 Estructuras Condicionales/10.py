"""10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año


Periodo del año                                 Estación en el hemisferio norte             Estación en el hemisferio sur

Desde el 21 de diciembre hasta el 20 de
marzo (incluidos)                                       Invierno                                       Verano

Desde el 21 de marzo hasta el 20 de junio
(incluidos)                                            Primavera                                       Otoño

Desde el 21 de junio hasta el 20 de
septiembre (incluidos)                                  Verano                                         Invierno

Desde el 21 de septiembre hasta el 20 de
diciembre (incluidos)                                   Otoño                                         Primavera

Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano."""

hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día del mes es? (1-31): "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = estacion_sur = "Desconocida"

if hemisferio == "N":
    print(f"Estás en el hemisferio norte y la estación es: {estacion_norte}")
elif hemisferio == "S":
    print(f"Estás en el hemisferio sur y la estación es: {estacion_sur}")
else:
    print("Hemisferio no válido.")
