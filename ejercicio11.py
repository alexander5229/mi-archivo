numeropositivo = int(input("Ingrese un número entero positivo: "))
factorial = 1
contador = 1
while contador <= numeropositivo:
    factorial = factorial * contador
    contador += 1
print("El factorial de", numeropositivo, "es:", factorial)
