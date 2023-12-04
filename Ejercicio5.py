# Programa que imprime la sucesión de Fibonacci desde el número 0
# hasta el número 1597, de forma horizontal
print("------------------------------------")
print("---------Serie de Fibonacci---------")
print("------------------------------------")
numero_1, numero_2 = 0, 1
while numero_2 <= 1597:
	print(numero_1, numero_2, end=" ")
	numero_1 += numero_2
	numero_2 += numero_1
