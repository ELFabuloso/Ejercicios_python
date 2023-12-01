# Dessarrollar un programa que solicite un número entero, posteriormente, el programa deberá
# determinar e indicar a través de un mensaje, si el número introducido es par o impar

print("------------------------------------")
print("---Sistema de números par o impar---")
print("------------------------------------")
# Variable donde se guardara el número a ingresar
numero = int(input("Por favor ingrese un número entero: "))

# Inicio para determinar si el número es par o impar
if numero % 2 == 0:
    print("El número", numero ,"es par")
else:
    print("El número", numero , "es impar")
