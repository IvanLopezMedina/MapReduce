import time
import sys as s
import reader, mapper, shuffler, reducer

class MapReduce:

    def __init__(self):     
        self.finalDictionary = {}

if __name__ == '__main__':

    start = time.time()
    my_MapReduce = MapReduce()

    argvHardcode = ["file1.txt", "bigfile.txt"]

    for file in argvHardcode[0:]:
    #for file in s.argv[1:]:
        print "----------- "
        print file, ":"
        print "----------- "

        read = reader.ReaderSplitter(file)
        lines = read.readFile()

        map = mapper.Mapper(lines)
        mapwords = map.mapping()

        shuffle = shuffler.Shuffler(mapwords)
        dictShuffled = shuffle.shuffle()

        reduce = reducer.Reducer(dictShuffled)
        reduce.reduce()

        print "----------- "
        print "    end     "
        print "----------- "

    end = time.time()
    print(end - start)
