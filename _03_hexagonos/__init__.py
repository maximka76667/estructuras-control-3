def printHexagon(n, c):
    for i in range(1, 2 * n, 1):
        # Cantidad de espacios en linea = abs(i - n)
        # Cantidad de symbols en linea = int((n - abs(n - i) - 1) * 2 + n)
        print(abs(i - n) * " " + int((n - abs(n - i) - 1) * 2 + n) * c)

# n (longitud del lado) = input[0], c (caracter del hexagono) = input[2], _ - espacio
[n, _, c] = input("Hexagon options (n c): ")
        
printHexagon(int(n), c)
