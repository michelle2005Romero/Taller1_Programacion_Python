estatura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
edad = int(input("Ingrese su edad: "))

imc = peso / estatura ** 2

if edad < 45:
    if imc < 22.0:
        print("Su condición de riesgo es baja")
    elif imc < 27.0:
        print("Su condición de riesgo es moderada")
    else:
        print("Su condición de riesgo es alta")
else:
    if imc < 22.0:
        print("Su condición de riesgo es moderada")
    elif imc < 27.0:
        print("Su condición de riesgo es alta")
    else:
        print("Su condición de riesgo es muy alta")