def printHexagon(n, c):
    for i in range(1, 2 * n, 1):
        print(abs(i - n) * " " + c * int((n - abs(n - i) - 1) * 2 + n))

input = input("Hexagon options: ")
[n,_,c] = input
        
printHexagon(int(n), c)