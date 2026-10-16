while True:
    doc=str(input("Ingrese su tipo de documento"))
    if doc == "CC" or doc == "TI" or doc == "CE":
        print("Documento válido")
        break
    else:
        print("Valor no válido, ingrese de nuevo")