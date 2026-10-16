numero_intentos = 0
intentos_permitidos = 3
 
while numero_intentos < intentos_permitidos:
          contra=int(input("Ingrese la contraseña"))
          if contra == 1234:
             print("Acceso concedido")
             break
          else:
             numero_intentos += 1
             print("Contraseña incorrecta")
             print(f"Le quedan {intentos_permitidos - numero_intentos} intentos")
          if numero_intentos == intentos_permitidos:
             print("Cuenta bloqueada")
             