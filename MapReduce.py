import re
import time
import threading
class MapReduce:

    def __init__(self):
        self.test = 0

    def readFile(fn):
        regexp = '[*/.,:;.0-9]'
        bufsize = 5000000
        lock = threading.Lock()
        linesread = []
        splitted = []
        i = 0
        with open("bigfile.txt", "rb") as infile:
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
                lock.acquire()
                linesread.append(lines)
                t = threading.Thread(target=my_MapReduce.split(linesread, splitted))
                t.start()
                #print "new thread"
                linesread = []
                lock.release()
        #my_MapReduce.split(linesread, splitted)
        infile.close()
        return splitted

    def split(self, linesread, splitted):
        [splitted.append(line.split()) for line in linesread]

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

    #for line in lines:
    #    for word in line:
    #        print word

    end = time.time()
    print(end - start)
