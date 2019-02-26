import re
import time
import sys
class MapReduce:

    def __init__(self):
        self.test = 0

    def readFile(self):
        regexp = '[*/.,:;.0-9]'
        bufsize = 5000000
        linesread = []
        splitted = []
        with open("file1.txt", "rb") as infile:
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

        print dictionary

        
    def reduce(self):
        print ""

if __name__ == '__main__':

    start = time.time()
    my_MapReduce = MapReduce()
    lines = my_MapReduce.readFile()
    
    mapwords = my_MapReduce.map(lines)

    my_MapReduce.shufle(mapwords)

    end = time.time()
    print(end - start)
