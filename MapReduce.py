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
                #Launch threads
                #t = threading.Thread(target=my_MapReduce.split(linesread, splitted)       
                my_MapReduce.split(linesread, splitted)
                linesread = []
        infile.close()
        return splitted

    def split(self, linesread, splitted):
        [splitted.append(line.split()) for line in linesread]

    def map(self, lines):
        diffwords = []
        for line in lines:
            for word in line:
                if word not in diffwords:
                    diffwords.append(word)
        
        for word in diffwords:
            print word

    def shufle(self):
        print ""

    def reduce(self):
        print ""

if __name__ == '__main__':

    start = time.time()
    my_MapReduce = MapReduce()
    lines = my_MapReduce.readFile()
    
    my_MapReduce.map(lines)

    end = time.time()
    print(end - start)
