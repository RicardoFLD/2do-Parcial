usuario = "marcos23"
contrasenna = "Exoticbutters"
intentos = 0
saldo = 0
sesion = True

while  intentos < 3:
    intentoUsuario = input("Ingrese el nombre de usuario: ")
    intentoContrasenna = input("Ingrese la contraseña: ")

    if intentoUsuario.lower() == usuario and intentoContrasenna == contrasenna and intentos < 3:
        print ("Bienvenido")
        break
    elif intentos < 3:
        print ("Usuario o contraseñas incorrecto, intentelo de nuevo")
        intentos += 1
    
    if intentos >= 3:
        print("Sistema bloqueado")
        sesion = False

while sesion == True:
 
    print ("Qué le gustaría realizar\n\
    1. Depositar dinero de la cuenta\n\
    2. Sacar dinero de la cuenta\n\
    3. Ver saldo\n\
    4. Salir")
    opcion = int(input("Num. de opción: "))

    if opcion == 1:
        deposito = int(input("ingrese lo que desea depositar: "))
        saldo = saldo + deposito
        print ("su saldo es: ", saldo)       
    elif opcion == 2:
        retiro = int(input("¿Cuánto desea retirar? "))
        if retiro > saldo:
         print("No tiene saldo suficiente")
        else:
            saldo = saldo - retiro
            print("Usted retiró: ", retiro)
            print("Su saldo actual es: ", saldo)     
    elif opcion == 3:
        print ("Su saldo es: ", saldo)
    elif opcion == 4:
            sesion = False
            break
    else:
         print("Opcion inválida, digite una opción válida")
    print("¿Desea continuar?")
    rsp = input("Si/No: ")
    if rsp.lower() == "no":
        sesion = False
    elif rsp.lower() == "si":
        sesion = True