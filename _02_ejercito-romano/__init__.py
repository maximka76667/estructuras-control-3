from functools import reduce
from operator import pow
from math import floor, sqrt

input = int(input("Entrada: "))
legiones = []

while input > 0:
    # n - tamano del lado del legion cuadradatico mas grande posible
    n = floor(sqrt(input))
    # Restamos cuadrado del n del numero de entrada
    input -= pow(n, 2)
    legiones.append(n)

def addShields(suma, legion):
    return suma + (4 * 3 + 4 * 2 * (legion - 2) + pow(legion - 2, 2))

result = reduce(addShields, legiones, 0)

print(result)