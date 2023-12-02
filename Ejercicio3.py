# Desarrollar un programa que solicite tres números 
# enteros, posteriormente, el programa deberá determinar e insicar
# atravez de un mensaje, cuál de los tres números es el más grande

print("********************************")
print("***El número más grande es...***")
print("********************************")

print("A continuación deberá ingresar 3 números")
numero_1 = float(input("Por favor ingrese el primer número: "))
numero_2 = float(input("Por favor ingrese el segundo número: "))
numero_3 = float(input("Por favor ingrese el ultimó número: "))
if numero_1 > numero_2 and numero_1 > numero_3: # Comparamos el primer número con los demas
    print("El número mayor es ", numero_1) # Si la condicion se cumple 
elif numero_2 > numero_3: # Comparando el primer y tercer número
    print("El número mayor es", numero_2) # Si la condicion se cumple
else: # De lo contrario el ultimao número sera el mayor
    print("El número mayor es", numero_3)
