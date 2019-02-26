import re
import time
import sys as s
class MapReduce:

    def __init__(self):
        self.test = 0
        self.filesArgv = []

    def readFile(self,file):
        regexp = '[*/.,:;.0-9]'
        bufsize = 5000000
        linesread = []
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
                    else :
                        lines += char
                        #Launch thread
                linesread.append(lines)      
                my_MapReduce.split(linesread, splitted)
                linesread = []
        infile.close()
        return splitted

    def readFiles(self):
        self.filesArgv.append(str(s.argv[i]) for i in range(len(s.argv)))

    def split(self, linesread, splitted):
        [splitted.append(line.split()) for line in linesread]

    def map(self, lines):
        mapwords = []
        for line in lines:
            for word in line:
                mapwords.append((word, 1))
        return mapwords

    def shufle(self, mapwords):
        dictionary = {}

        for word in mapwords:
            if dictionary.has_key(word[0]):
                dictionary[word[0]].append(word)
            else:
                dictionary[word[0]] = []
                dictionary[word[0]].append(word)

        #print dictionary
        return dictionary
        
    def reduce(self,dictionary):
        print dictionary

if __name__ == '__main__':

    start = time.time()
    my_MapReduce = MapReduce()
    my_MapReduce.readFiles()

    my_MapReduce.filesArgv = ["Sample.txt",
                              "file1.txt"]  # fichero hardcodeados para probar que funciona la lectura de n ficheros
    #Esto se borra y se pasa por arg en el comando

    for file in my_MapReduce.filesArgv:
        lines = my_MapReduce.readFile(file)
        mapwords = my_MapReduce.map(lines)
        dict = my_MapReduce.shufle(mapwords)
        my_MapReduce.reduce(dict)

    end = time.time()
    print(end - start)
