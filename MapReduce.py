import re
import time
import sys as s
import threading as th
class MapReduce:

    def __init__(self):
        self.finalDictionary = {}
        self.mapwords = []

    def readFile(self, file):
        # Leeemos un solo fichero y eliminamos los caracteres raros con una Regular Expression
        #
        # Guardamos las lineas en una lista y llamamos al split para separar la linea en palabras
        regexp = '[*?!"$%&()=^+#|@/.,:;.0-9]'
        bufsize = 5000000
        splitted = []

        with open(file, "rb") as infile:
            while True:
                lines = re.sub(regexp, '', infile.read(bufsize))
                if not lines:
                    break
                while (lines[-1:] != "\n"):
                    char = re.sub(regexp, '', infile.read(1))
                    if not char:
                        break
                    else:
                        lines += char
                linesread = []
                linesread.append(lines)
                t = th.Thread(target=my_MapReduce.split(linesread, splitted))
                t.start()
                #my_MapReduce.split(linesread, splitted)


        infile.close()
        return splitted


    def split(self, linesread, splitted):
        # Separamos una linea en palabras y lo guardamos en una lista
        [splitted.append(line.split()) for line in linesread]
        my_MapReduce.map(splitted)
        #[splitted.append(list(line)) for line in linesread] #SEPARA PRO LETRAS

    def map(self, lines):
        for line in lines:
            [self.mapwords.append((word, 1)) for word in line]
        

    def shufle(self, mapwords):
        dictionary = {}
        for word in mapwords:
            if dictionary.has_key(word[0]):
                dictionary[word[0]].append(word)
            else:
                dictionary[word[0]] = []
                dictionary[word[0]].append(word)

        return dictionary
        
    def reduce(self, dictionary):
        # Recorremos cada palabra del diccionario y contamos el numero de veces que esta repetida
        # y las guardamos en un diccionario donde la clave es la palabra y el valor el numero de veces repetidas
        self.finalDictionary = {}
        for key, value in dictionary.items():
            cont = 0
            for key, num in value:
                cont += num
            self.finalDictionary[key] = cont
        
        for key, value in self.finalDictionary.items():
            print key , " : " , value

if __name__ == '__main__':

    start = time.time()
    my_MapReduce = MapReduce()

    argvHardcode = ["file1.txt", "bigfile.txt"]

    for file in argvHardcode[0:]:
    #for file in s.argv[1:]:
        print "----------- "
        print file, ":"
        print "----------- "

        lines = my_MapReduce.readFile(file)
        #mapwords = my_MapReduce.map(lines)
        dict = my_MapReduce.shufle(my_MapReduce.mapwords)
        my_MapReduce.reduce(dict)
        my_MapReduce.mapwords = []
        print "----------- "
        print "    end     "
        print "----------- "

    end = time.time()
    print(end - start)
