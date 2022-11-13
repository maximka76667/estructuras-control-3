import re


def takeEndOfWords(word):
    isFirst = False
    for i in range(len(word) - 1, -1, -1):
        if (re.match('[aouei]', word[i])):
            if not isFirst:
                isFirst = True
                continue
            
            if(isFirst):
                return word[i:len(word)]
            
def isPareado(rimas):
    return len(rimas) == 2 and rimas[0] == rimas[1]

def isTerceto(rimas):
    return len(rimas) == 3 and rimas[0] == rimas[2] != rimas[1]

def isCuarteto(rimas):
    return rimas[0] == rimas[3] != rimas[1] == rimas[2]

def isCuarteta(rimas):
    return rimas[0] == rimas[2] != rimas[1] == rimas[3]

def getVocals(rima):
    return "".join(re.findall('[aouie]', rima))

def isSeguidilla(rimas):
    rimas = list(map(getVocals, rimas))
    return rimas[1] == rimas[3] != rimas[0] != rimas[2] != rimas[1]

def isCuadernaVia(rimas):
    return rimas[0] == rimas[1] == rimas[2] == rimas[3]

def checkCuatroVersos(rimas):
    if len(rimas) != 4: 
        return [False, False, False, False]
    return [isCuarteto(rimas), isCuarteta(rimas), isSeguidilla(rimas), isCuadernaVia(rimas)]

def findTrue(matches):
    for i in range(len(matches)):
        if(matches[i]):
            return i
        
    return -1

n = int(input("N: "))

# lastWords = ["borrado","pecada", "pesado", "avocada"]
lastWords = []

names = ["Pareado", "Terceto", ["Cuarteto", "Cuarteta", "Seguidilla", "Cuaderna Via"], "Desconocido"]
    
for i in range(0, n, 1):
    line = input()
    lastWords.append(line.split(" ")[-1])


rimas = list(map(takeEndOfWords, lastWords))

if n == 4:
    isCuatroVersos = findTrue(checkCuatroVersos(rimas))

if isPareado(rimas):
    print(names[0])
elif isTerceto(rimas):
    print(names[1])
elif isCuatroVersos != -1:
    print(names[2][isCuatroVersos])
else:
    print(names[3])
