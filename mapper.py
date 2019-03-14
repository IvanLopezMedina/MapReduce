# En aquesta classe processem una llista de totes les paraules separades
# Retornem una llista on cada element es un diccionari paraula -> 1
class Mapper:
    def __init__(self, lines):
        self.mapwords = []
        self.lines = lines

    def mapping(self):
        # Per cada paraula, afegeix a la llista un diccionari paraula , 1
        for line in self.lines:
            [self.mapwords.append((word, 1)) for word in line]
        
        return self.mapwords