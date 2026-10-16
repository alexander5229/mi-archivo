cantidad = int(input("¿Cuántos términos Fibonacci desea visualizar? "))
a = 0
b = 1
contador = 0
while contador < cantidad:
    print(a)
    siguiente = a + b
    a = b
    b = siguiente
    contador += 1