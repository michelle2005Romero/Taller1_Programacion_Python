numeros = []

for i in range(4):
    numero = int(input("Introduce un número: "))
    numeros.append(numero)

numeros.sort()

print("Números ordenados de menor a mayor:", numeros)