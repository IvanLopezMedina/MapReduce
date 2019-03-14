class Reducer:
    def __init__(self, dictShuffled):
        self.dictShuffled = dictShuffled
        self.finalDictionary = {}

    def reduce(self):
        # Recorremos cada palabra del diccionario y contamos el numero de veces que esta repetida
        # y las guardamos en un diccionario donde la clave es la palabra y el valor el numero de veces repetidas
        
        for key, value in self.dictShuffled.items():
            cont = 0
            for key, num in value:
                cont += num
            self.finalDictionary[key] = cont
        
        for key, value in self.finalDictionary.items():
            print key , " : " , value