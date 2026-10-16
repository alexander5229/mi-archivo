while True:

        calificacion=int(input("Ingrese la nota"))
        if calificacion >= 0.0 and calificacion <= 5.0:
            print("Nota positiva")
            break
        else:
            print("La nota no esta en el rango permitido")
