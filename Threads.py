from multiprocessing import Pool
import time
import codecs
import re

def aplicarMP(line):
    regexp = '[*?!"$%&()=^+#|@/.,:;.0-9]'
    mapwords = []

    lines = re.sub(regexp, '', line)
    splitted = lines.split()

    [mapwords.append((word, 1)) for word in splitted]

    return mapwords


if __name__ == "__main__":
    start = time.time()
    p = Pool(processes=4)

    file_name = 'bigfile.txt'
    lines = []

    bufsize = 500000

    regexp = '[*?!"$%&()=^+#|@/.,:;.0-9]'
    with codecs.open(file_name,'r', encoding="utf8") as f:
        while True:
            lines2 = re.sub(regexp, '', f.read(bufsize))
            if not lines2:
                break
            while (lines2[-1:] != "\n"):
                char = re.sub(regexp, '', f.read(1))
                if not char:
                    break
                else:
                    lines2 += char

            lines.append(lines2)
        #for line in f:
            #lines.append(line.strip())

    dictionary = {}
    finalDictionary = {}

    mapwords = p.map(aplicarMP, lines)

    for wordlines in mapwords:
        for word in wordlines:
            if dictionary.has_key(word[0]):
                dictionary[word[0]].append(word)
            else:
                dictionary[word[0]] = []
                dictionary[word[0]].append(word)


    for key, value in dictionary.items():
        cont = 0
        for key, num in value:
            cont += num
        finalDictionary[key] = cont

    for key, value in finalDictionary.items():
        print key, " : ", value


    end = time.time()
    print end - start
    p.close()
    p.join()