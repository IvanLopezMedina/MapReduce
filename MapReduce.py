import time
import sys
import reader, mapper, shuffler, reducer
import gc

if __name__ == '__main__':
    start = time.time()
    for file in sys.argv[1:]:
        print "----------- "
        print file, ":"
        print "----------- "

        # Amb la classe reader fem la lectura del fitxer i el split
        read = reader.ReaderSplitter(file)
        lines = read.readFile()

        print "Im done reading"
        
        # Amb la classe mapper afegim una parella clau valor { paraula: 1 }
        # als elements de la llista obtinguda del split
        map = mapper.Mapper(lines)
        lines = ''
        read = ''
        gc.collect()
        mapwords = map.mapping()

        print "Im done mapping"
        # Amb la classe shuffler creem un diccionari per cada paraula no repetida
        # per cada paraula creem una llista on fiquem totes les tuples iguals
        shuffle = shuffler.Shuffler(mapwords)
        del map
        del mapwords
        gc.collect()
        dictShuffled = shuffle.shuffle()
        
        print "Im done shuffling"
        # Amb la classe reducer, processem el diccionari i fem un sumatori per cada paraula
        # de totes les claus de la llista
        reduce = reducer.Reducer(dictShuffled)
        del dictShuffled
        del shuffle
        gc.collect()
        reduce.reduce()
        del reduce
        gc.collect()
        print "Im done reducing"
        
        print "----------- "
        print "    end     "
        print "----------- "
        end = time.time()
        print(end - start)
