import math
from datetime import datetime
import string
acel=0
Pi = math.pi
latitud1=0
longitud2=0 
def distancia (latitud1,longitud1,latitud2,longitud2):
    radio = 6371.08
    lat = (latitud2 - latitud2) * (math.pi / 180)
    log = (longitud2 - longitud1) * (math.pi / 180)
   
    a = math.sin(lat / 2) * math.sin(lat / 2) + math.cos(latitud1 * (math.pi / 180)) * math.cos(latitud2 * (math.pi / 180)) * math.sin(log / 2) * math.sin(log / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radio * c
    return d

print("rellene los datos a continuacion")
nombre = input("Ingrese su nombre:\n")
apellido = input("Ingrese su apellido:\n")
rut = input("Ingrese su rut:\n")
correo=input("Ingrese su correo:\n")
clave=input("Ingrese su clave:\n")
edad=int(input("Ingrese su edad:\n"))
matricula=input("Ingrese su matricula:\n")
marca=input("Ingrese su marca:\n")
modelo=input("Ingrese su modelo:\n")


if edad < 18:
    print("No puede ingresar al sistema")
elif edad > 18:
    print("Su rut es:", rut,", su nombre es:", nombre,", su apellido es:", apellido,", su correo es:", correo,", su edad es:", edad,", su matricula es:", matricula, ", fecha de registro:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("Presione 1 para iniciar sesion. ")
    print("Presione 2 para comenzar una carrera ")
    opc  = input()
    if opc == "1":
        verficacionCorreo=input("Ingrese su correo:\n")
        verficacionContraseña=input("Ingrese su clave:\n")
        if verficacionCorreo == correo and verficacionContraseña == clave:
            print("Bienvenido", nombre, ", matricula numero", matricula, datetime.now().strftime("Dia %d del %m del %Y %H:%M:%S"))
            opcion = string()
        
            encendido= False
            carrera = input("Presione 1 para comenzar una carrera\nPresione 2 para salir\n")
            if carrera == "1":
                while opcion != "8":
                    print("1. - Ingresar ubicación GPS Inicial, LATITUD")
                    print("2. - Ingresar ubicación GPS Inicial, LONGITUD")
                    print("3. - Encender el vehículo.")
                    print("4. - Acelerar vehículo")
                    print("5. - Descelerar vehículo")
                    print("6. - Apagar Vehículo")
                    print("7. - Girar Vehículo.")
                    print("8. - Finalizar carrera")
                    opcion= input()
                    if opcion == "1":
                        latitud1 = float(input("Ingrese la latitud inicial:\n"))
                        print("Latitud ingresada correctamente\n")
                    elif opcion == "2":
                        longitud1 = float(input("Ingrese la longitud inicial:\n"))
                        print("Longitud ingresada correctamente\n")
                    elif opcion == "3":
                         print("Encendiendo vehículo...\n")
                         encendido = True
                    elif opcion == "4" and encendido:
                        acel +=10
                        print("Usted está viajando a", acel, "Km/h\n")
                    elif opcion == "5" and encendido:
                        if acel<10:
                            print("Usted está detenido\n")
                        elif acel>=10:
                                if acel==10:
                                    acel =0
                                    print("Usted está detenido\n")
                                elif acel>10:
                                        acel -=10
                                        print("Usted está viajando a", acel, "Km/h\n")
                    elif opcion == "6" and encendido:
                        print("Apagando vehículo...\n")
                        encendido = False
                    elif opcion == "7" and encendido:
                        print("Girando vehículo...\n")
                    elif opcion == "8":
                        print("terminando carrera...\n")
                        latitud2 = float(input("Ingrese la latitud de destino:\n"))
                        longitud2 = float(input("Ingrese la longitud de destino:\n"))
                        distancia = distancia(latitud1, longitud1, latitud2, longitud2)
                        print("Distancia recorrida:", round(distancia, 2), "Km")
                        print("Total a pagar por el viaje: $", round(distancia*(220*1.8)))
                    else: print("Puede que el motor este apagado o no haya ingresado una opción válida\n")
            elif carrera == 2:
                print("cerrando sistema")
            else:
                print("Opción no válida")
        else:
            print("correo o clave incorrectos")
    elif opc == 2:
            print("Tiene que registrarse para poder comenzar una carrera\n")
    else:
            print("Opción no válida")    





                   
                   

