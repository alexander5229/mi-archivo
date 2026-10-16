suma = 0
cantidad = 0
nota = float(input("Ingrese una calificación (-1 para terminar): "))
while nota != -1:
    suma += nota
    cantidad += 1
    nota = float(input("Ingrese una calificación (-1 para terminar): "))
if cantidad > 0:
    promedio = suma / cantidad
    print("El promedio de las calificaciones es:", promedio)
