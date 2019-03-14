import re
import threading as th

class ReaderSplitter:
    def __init__(self, file):
        self.regexp = '[*?!"$%&()=^+#|@/.,:;.0-9]'
        self.bufsize = 5000000
        self.file = file
    
    def readFile(self):
        linesread = []
        splitted = []
        try:
            with open(self.file, "rb") as infile:
                while True:
                    lines = re.sub(self.regexp, '', infile.read(self.bufsize))
                    if not lines:
                        break
                    while (lines[-1:] != "\n"):
                        char = re.sub(self.regexp, '', infile.read(1))
                        if not char:
                            break
                        else:
                            lines += char
                    
                    linesread.append(lines)
                    t = th.Thread(target=self.split(linesread, splitted))
                    t.start()
                    #my_MapReduce.split(linesread, splitted)
                    linesread = []
                    lines = ''
        except MemoryError as err:
                   print("Error de memoria" + err)

        infile.close()
        return splitted
    
    def split(self, linesread, splitted):
        # Separamos una linea en palabras y lo guardamos en una lista
        [splitted.append(line.split()) for line in linesread]