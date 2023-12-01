#Sistema que determina los dias de vacaciones de un trabajador 
#haciendo uso unicamente de if anidados
print("===========================================")
print("=======Sistema de control vacacional=======")
print("===========================================")

nombre = input("Introduzca su nombre: ")
print("\nBienvenido" + " " + nombre)
clave = int(input("Por favor ingrese su número de clave: "))
tiempo = int(input("Por favor ingrese sus años de trabajo: "))

#Uso de la sentencia if anidados para validar la información
if clave == 1:
    if tiempo == 1:
        print("Felicidades" , nombre , "tiene 6 dias de vacaciones") # Si la condición se cumple se generan los dias de vacaciones
    elif tiempo >= 2 and tiempo <= 6:
        print("Feliciedades" , nombre , "tiene 14 dias de vacaciones")
    elif tiempo > 7:
        print("Felicidades" , nombre , "tiene 20 dias de vacaciones")
elif clave == 2:
    if tiempo == 1:
        print("Felicidades" , nombre , "tiene 7 dias de vacaciones")
    elif tiempo >= 2 and tiempo <= 6:
        print("Felicidades" , nombre , "tiene 15 dias de vacaciones")
    elif tiempo > 7:
        print("Felicidades" , nombre , "tiene 22 dias de vacaciones")    
elif clave == 3:
    if tiempo == 1:
        print("Felicidades" , nombre , "tiene 10 dias de vacaciones")
    elif tiempo >= 2 and tiempo <= 6:
        print("Felicidades" , nombre , "tiene 20 dias de vacaciones")
    elif tiempo > 7:
        print("Felicidades" , nombre , "tiene 30 dias de vacaciones")        
else:
    print("La clave  ", clave, "no existe")    