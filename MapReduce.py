import re
import time
#Regular expressions
class MapReduce:

    def __init__(self):
        self.test = 0

    def readFile(self):
        f = open("file1.txt", "r")
        lines = []
        for line in f:
            lines.append(re.sub('([^\s\w]|_)+', '', line))
        f.close()
        return lines

    def split(self,lines):
        splitted = []
        [splitted.append(line.split()) for line in lines]

        return splitted

    def map(self):
	    print ""

    def shufle(self):
	    print ""

    def reduce(self):
	    print ""

if __name__ == '__main__':
    my_MapReduce = MapReduce()
    lines = my_MapReduce.readFile()
    splitlines = my_MapReduce.split(lines)

    for line in splitlines:
        for word in line:
            print word

