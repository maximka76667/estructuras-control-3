def printHexagon(n, c):
    for i in range(1, 2 * n, 1):
        # Cantidad de espacios en linea = abs(i - n)
        # Cantidad de symbols en linea = int((n - abs(n - i) - 1) * 2 + n)
        print(abs(i - n) * " " + int((n - abs(n - i) - 1) * 2 + n) * c)

data = input("Hexagon options (n c): ")
# n = data[0], c = data[2], _ - espacio
[n, _, c] = data
        
printHexagon(int(n), c)
