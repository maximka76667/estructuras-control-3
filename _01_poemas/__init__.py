import re

# FUNCTIONS
def takeSoundsFromLastStressedVowel(word):
    # Se usa para encontrar penultima vocal en el verso     
    isFirstFound = False
    
    # Bucle desde la ultima letra hasta la primera
    for i in range(len(word) - 1, -1, -1):
        # Expresion regular para encontrar vocales
        if (re.match('[aouei]', word[i])):
            # Si ultima vocal ya iba encontrada - esa es la penultima
            if(isFirstFound):
                # Devolvemos todos los sonidos desde la penultima vocal
                return word[i:len(word)]
            
            # Ultima vocal encontrada
            isFirstFound = True
            continue
        
        # Si tiene solo una vocal devuelve toda la palabra         
        if(i == 0):
            return word
            
def getAssonanceRhyme(rima):
    return "".join(re.findall('[aouie]', rima))
            
def isPareado(rimas):
    return len(rimas) == 2 and rimas[0] == rimas[1]

def isTerceto(rimas):
    return len(rimas) == 3 and rimas[0] == rimas[2] != rimas[1]

def isCuarteto(rimas):
    return rimas[0] == rimas[3] != rimas[1] == rimas[2]

def isCuarteta(rimas):
    return rimas[0] == rimas[2] != rimas[1] == rimas[3]

def isSeguidilla(rimas):
    rimas = list(map(getAssonanceRhyme, rimas))
    return rimas[1] == rimas[3] != rimas[0] != rimas[2]

def isCuadernaVia(rimas):
    return rimas[0] == rimas[1] == rimas[2] == rimas[3]

def getTypesFourLinesPoem(rimas):
    return [isCuarteto(rimas), isCuarteta(rimas), isSeguidilla(rimas), isCuadernaVia(rimas)]

# ***FUNCTIONS***

# PROGRAMM START

lastWords = []
poemTypes = ["Pareado", "Terceto", ["Cuarteto", "Cuarteta", "Seguidilla", "Cuaderna Via"], "Desconocido"]

n = int(input("N: "))

# Si tiene menos que 2 versos y mas que 4 es desconocido
if n < 2 or n > 4:
    print(poemTypes[-1])
    exit()

# Pedimos la poema
for i in range(0, n, 1):
    lastWords.append(input())

# Todos los sonidos desde la penultima vocal de cado verso
rimas = list(map(takeSoundsFromLastStressedVowel, lastWords))

# De dos versos
if isPareado(rimas):
    print(poemTypes[0])
    exit()
    
# De tres versos
elif isTerceto(rimas):
    print(poemTypes[1])
    exit()

# De cuatro versos
elif n == 4:
    isCuatroVersos = getTypesFourLinesPoem(rimas).index(True)
    if(isCuatroVersos != -1):
        print(poemTypes[2][isCuatroVersos])
        exit()

# Desconocido
print(poemTypes[-1])
