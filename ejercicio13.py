base = float(input("Ingrese número base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = 1
contador = 0
while contador < exponente:
    resultado = resultado * base
    contador += 1
print("El resultado de la potencia es:", resultado)


