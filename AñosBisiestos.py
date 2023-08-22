def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

anio = int(input("Introduce un año: "))
if es_bisiesto(anio):
    print("El año", anio, "es bisiesto")
else:
    print("El año", anio, "no es bisiesto")