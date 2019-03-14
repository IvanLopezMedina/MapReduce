import re
import threading as th

# En aquesta classe llegim el fitxer en chunks de 5MB, treiem caracters especials
class ReaderSplitter:
    def __init__(self, file):
        # Expressio regular per treure caracters no desitjats al text
        self.regexp = '[*?!"$%&()=^+#|@/.,:;.0-9]'
        # Tamany del buffer per llegir el fitxer en chunks de 5MB
        self.bufsize = 5000000
        self.file = file
    
    # Aquesta funcio llegeix el fitxer i crida la funcio split, retorna una llista
    def readFile(self):
        linesread = []
        splitted = []
        # Try catch per trobar possibles errors de memoria si el fitxer es massa gran
        try:
            with open(self.file, "rb") as infile:
                while True:
                    # Llegim 5MB, sino trobem final de linea, seguim llegint caracter a caracter

                    lines = re.sub(self.regexp, '', infile.read(self.bufsize))
                    if not lines:
                        break
                    while (lines[-1:] != "\n"):
                        char = re.sub(self.regexp, '', infile.read(1))
                        if not char:
                            break
                        else:
                            lines += char
                    # Fiquem les linies a splittar a una llista i ho deixem fent a un thread
                    # Mentrestant el fitxer es pot seguir llegint
                    linesread.append(lines)
                    t = th.Thread(target=self.split(linesread, splitted))
                    t.start()
                
                    linesread = []
                    lines = ''

        except MemoryError as err:
            print("Error de memoria no tens suficient RAM, llegint part actual" + err)
            infile.close()
            return splitted

        infile.close()
        return splitted

    # La funcio split reb una llista de 5MB i la separa paraules
    def split(self, linesread, splitted):
        # Separem una linea en paraules i ho guardem en una llista
        [splitted.append(line.split()) for line in linesread]