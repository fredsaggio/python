def calcDistancia(xa, ya, xb , yb):
    return ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5;

print(calcDistancia(1, 1, 3, 4)); # D = 3.605

print(calcDistancia(0, 0, 10, 10)); # D = 14.142

print(calcDistancia(2, 7, 20, 30)); # D = 29.206