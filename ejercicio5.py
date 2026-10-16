while True:
    print("Procesando solicitud")
    confirmacion=str(input("Desea realizar otra opración? (S/N)"))
    if confirmacion == "S" or confirmacion=="s":
        continue   
    else:
        print("Programa finalizado")
        break