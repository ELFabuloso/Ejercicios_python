# Hacer un progama que pida una frase desde teclado 
# y que al imprimir la frase sea sin vocales
# Considerar que el usuario puede ingresar vocales en mayusculas

string = input("Ingrese una frase: ")#Pide al usuario una frase
sin_vocal = ""#Cadena vacia donde se almacenaran las vacales

for caracter in string:#Caracter sera la variable donde se almacenara cada letra del string
    #Se compara cada una de las letras (caracter) con las vocales
    #Si se cumple continua con la comparación
    if caracter.lower()=="a":
        continue
    elif caracter.lower()=="e":
        continue
    elif caracter.lower()=="i":
        continue
    elif caracter.lower()=="o":
        continue 
    elif caracter.lower()=="u":
        continue
    else:
        #cada caracter que cumpla con las condiciones anteriores se agregaran
        #en la cadena vacia sin_vocal
        sin_vocal += caracter  
    print(caracter,end="")
