m = int(input("Número de juegos ganados por el jugador A: "))
n = int(input("Número de juegos ganados por el jugador B: "))

if m < 6 and n < 6:
    print("El set todavía no termina")
elif abs(m - n) < 2:
    print("El resultado es inválido")
elif m == 6 and n < 5:
    print("A ganó el set")
elif n == 6 and m < 5:
    print("B ganó el set")
elif m == 7 and n == 5:
    print("A ganó el set")
elif n == 7 and m == 5:
    print("B ganó el set")
elif m == 7 and n == 6:
    print("A ganó el set")
elif n == 7 and m == 6:
    print("B ganó el set")
else:
    print("El resultado es inválido")