from functools import reduce
from operator import pow
import math

input = int(input("Entrada: "))
legiones = []

while input > 0:
    n = math.floor(math.sqrt(input))
    input -= pow(n, 2)
    legiones.append(n)

def addShields(suma, legion):
    return suma + (4 * 3 + 4 * 2 * (legion - 2) + pow(legion - 2, 2))

result = reduce(addShields, legiones, 0)

print(result)