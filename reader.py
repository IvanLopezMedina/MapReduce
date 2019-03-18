import re
import threading as th

# En aquesta classe llegim el fitxer en chunks de 5MB, treiem caracters especials
class ReaderSplitter:
    def __init__(self, file):
        # Expressio regular per treure caracters no desitjats al text
        self.regexp = '[*?!"$%&()=^+#|@/.,:;.0-9]'
        # Tamany del buffer per llegir el fitxer en chunks de 5MB
        self.BUFSIZE = 5000000
        self.file = file
    
    # Aquesta funcio llegeix el fitxer en trosos i crida al split
    def readFile(self):
        linesread = []
        splitted = []

        f = open(self.file)
        for chunk in self.readInChunks(f):
            linesread.append(chunk)
            # Fiquem les linies a splittar a una llista i ho deixem fent a un thread
            # Mentrestant el fitxer es pot seguir llegint  
            t = th.Thread(target=self.split(linesread, splitted))
            t.start()
            linesread = []
        # Esperem a tots el threads
        t.join()
        f.close()
 
        return splitted

    # La funcio split reb una llista de 5MB i la separa paraules
    def split(self, linesread, splitted):
        # Separem una linea en paraules i ho guardem en una llista
        [splitted.append(line.split()) for line in linesread]

    def readInChunks(self, fileObj):
        # Try catch per controlar la memoria
        try:
            while True:
                # Llegim el tamany del buffer 
                data = re.sub(self.regexp, '', fileObj.read(self.BUFSIZE))
                if not data:
                    break
                # Continuem llegint fins trobar un salt de linea
                while (data[-1:] != '\n'):
                    char = re.sub(self.regexp, '', fileObj.read(1))
                    if not char:
                        break
                    else:
                        data += char
                # Retornem el chunk llegit amb yield que es mes eficient que return
                yield data
        except MemoryError as err:
            print("Error de memoria no tens suficient RAM, llegint actual" + err)
            yield data