class Shuffler:
    def __init__(self, listMapped):

        self.listMapped = listMapped
        self.dictionary = {}


    def shuffle(self):
        for word in self.listMapped:
            if self.dictionary.has_key(word[0]):
                self.dictionary[word[0]].append(word)
            else:
                self.dictionary[word[0]] = []
                self.dictionary[word[0]].append(word)

        return self.dictionary