# En aquesta classe processem el diccionari ja amb el shuffle aplicat, que te per cada paraula
# una llista de diccionaris amb { paraula: 1 } i sumem tots els valors per obtenir el recompte

class Reducer:
    def __init__(self, dictShuffled):
        self.dictShuffled = dictShuffled
        self.finalDictionary = {}

    def reduce(self):
        printDict = {}
        # Mirem per cada paraula del diccionari, les vegades que apareix la paraula sumant el seu valor que sempre es 1
        # les guardem a un diccionari { paraula: valortotal }
        for word, list in self.dictShuffled.items():
            for key, value in list:
                if key in printDict:
                    printDict[key] += value
                else:
                    printDict[key] = value
        # Pintem el diccionari
        for word, value in printDict.items():
            print word , " : " , value
            