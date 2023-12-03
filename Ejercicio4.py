# Dessarrollar una calculadora con las siguientes características
# 1. La calculadora deberá ser capaz de calcular las operaciones de suma, resta
# multiplicación, división, división entera, exponente y modúlo o resto.
print("----------------------------------")
print("---Calculadora de dos variables---")
print("----------------------------------")
# Menú de opciónes
print("Menú de la calculadora\n")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Modúlo o resta")
opcion = int(input("Por favor marque con un número la opción que necesite: "))

# Si selecciona la primera opcuón
if opcion == 1:
    print("Ha seleccionado la primera opcion")
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
    suma = num1 + num2
    print("El resultado de la suma es", suma)
elif opcion == 2:
    print("Ha seleccionado la segunda opcion")
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
    resta = num1 - num2
    print("El resultado de la resta es ", resta)
elif opcion == 3:
    print(" Has seleccionado la tercera opción")
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
    mul = num1 * num2
    print("El resultado de la multiplicación es ", mul)
elif opcion == 4:
    print(" Has seleccionado la cuarta opción")
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
    div = num1 / num2
    print("El resultado de la división es ", div)
elif opcion == 5:
    print("Has seleccionado la quinta opcion")
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
    diventera = num1 // num2
    print("El resultado de la división es ", diventera)
elif opcion == 6:
    print("Has seleccionado la sexta opcion")
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
    potencia = num1 ** num2
    print("El resultado del exponente es ", potencia)
elif opcion == 7:
    print("Has seleccionado la opcion 7")
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
    modulo = num1 % num2
    print("El resultado del exponente es ", modulo)
else:
    print("FIN")
