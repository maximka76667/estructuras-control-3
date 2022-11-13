def printHexagon(n, c):
    for i in range(1, 2 * n, 1):
        # Cantidad de espacios en linea = abs(i - n)
        # Cantidad de symbols en linea = int((n - abs(n - i) - 1) * 2 + n)
        print(abs(i - n) * " " + int((n - abs(n - i) - 1) * 2 + n) * c)

input = input("Hexagon options (n c): ")
[n,_,c] = input
        
printHexagon(int(n), c)