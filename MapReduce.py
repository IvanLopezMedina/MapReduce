import time
import sys
import reader, mapper, shuffler, reducer

if __name__ == '__main__':

    for file in sys.argv[1:]:
        print "----------- "
        print file, ":"
        print "----------- "

        # Amb la classe reader fem la lectura del fitxer i el split
        read = reader.ReaderSplitter(file)
        lines = read.readFile()

        # Amb la classe mapper afegim una parella clau valor { paraula: 1 }
        # als elements de la llista obtinguda del split
        map = mapper.Mapper(lines)
        mapwords = map.mapping()

        # Amb la classe shuffler creem un diccionari per cada paraula no repetida
        # per cada paraula creem una llista on fiquem totes les tuples iguals
        shuffle = shuffler.Shuffler(mapwords)
        dictShuffled = shuffle.shuffle()

        # Amb la classe reducer, processem el diccionari i fem un sumatori per cada paraula
        # de totes les claus de la llista
        reduce = reducer.Reducer(dictShuffled)
        reduce.reduce()

        print "----------- "
        print "    end     "
        print "----------- "
