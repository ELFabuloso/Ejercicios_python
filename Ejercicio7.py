# Desarrollar un programa que invierta una cadena de caracteres, y a su vez, esta cadena deberá ser ingresada
# por el usuario desde teclado.
# No se permite modificar la cadena de caracteres original
# Utilizar el bucle o ciclo for

string = input("Introduce una frase o palabra que sera invertida: ") 
string_reversed = ""
for i in string:
    string_reversed = i + string_reversed
print(f"Frase o palabra invertida: {string_reversed}")
