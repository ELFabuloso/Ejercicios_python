# Desarrollar un programa que muestre en pantalla, la tabla de 
# multiplicar de un número cualquiera, este número deberá ser 
# solicitado e ingresado desde teclado por el usuario.
# Utilizar el ciclo for o bucle for
# La tabla debe contener las multiplicaciones que van desde el 0 hasta el 10
print("***************************")
print("***Tablas de multiplicar***")
print("***************************")
numero = int(input("Digite el número de la tabla de multiplicar que desea ver: "))
multi = 0
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")
    
print("Fin del programa") 