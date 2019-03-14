# En aquesta classe processem la llista del map i agrupem les paraules
# Retornem llista paraula : { { paraula: 1 } , {paraula: 1 } }
class Shuffler:
    def __init__(self, listMapped):
        self.listMapped = listMapped
        self.dictionary = {}

    def shuffle(self):
        # Per cada paraula, si existeis una entrada al diccionari
        # La afegim a la llista de paraules d'aquesta entrada
        # Sino existeix una entrada, creem una nova i afegim a la llista
        for word in self.listMapped:
            if self.dictionary.has_key(word[0]):
                self.dictionary[word[0]].append(word)
            else:
                self.dictionary[word[0]] = []
                self.dictionary[word[0]].append(word)

        return self.dictionary