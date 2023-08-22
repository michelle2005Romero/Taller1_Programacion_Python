a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("El triángulo es inválido")
elif a == b == c:
    print("El triángulo es equilátero")
elif a == b or a == c or b == c:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")