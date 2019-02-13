class MapReduce:

    def __init__(self):
        self.test = 0

    def readFile(self):
        f = open("file1.txt", "r")
        lines = []
        for x in f:
            lines.append(x)
        #If you want to read each character one by one use print(f.read(1)) excluding the unwanted characters
        return lines

    def split(self,lines):
        splitted = []
        for line in lines:
            splitted.append(line.split())

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


