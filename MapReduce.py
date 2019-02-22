import re
import time
class MapReduce:

    def __init__(self):
        self.test = 0

    def readFile(fn):
        regexp = '([^\s\w]|_)+'
        bufsize = 80
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
                print linesread

        [splitted.append(line.split()) for line in linesread]
        infile.close()
        return splitted

    def map(self):
	    print ""

    def shufle(self):
	    print ""

    def reduce(self):
	    print ""

if __name__ == '__main__':
    start = time.time()
    my_MapReduce = MapReduce()
    lines = my_MapReduce.readFile()

    for line in lines:
        for word in line:
            print word



    end = time.time()
    print(end - start)
