acumulador = 0
while True:
    numeros=int(input("Ingrese número real"))
    if numeros == 0:
        break
    acumulador += numeros 
    print(f"La suma total es: {acumulador}")