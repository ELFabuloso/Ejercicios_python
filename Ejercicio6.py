# Desarrollar un programa que elimine una palabra que forme parte
# de una cadena de caracteres
# La caneda de caracteres deberá ser solicitada desde teclado.
# La palabra a elim8inar deberá ser solicitada desde teclado.

string = input("Introduce una frase: ")
palabra = input("Introduce la palabra que desas eliminar: ")
subsring = ""

indice = string.find(palabra) #Se localiza la posicion de la palabra que deseamos eliminar
substring = string[0 : indice] + string[indice + len(palabra) + 1 : ] #Corte de la frase 

print(f"Cadena resultante: {substring}")