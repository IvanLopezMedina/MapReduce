class Mapper:
    def __init__(self, lines):
        self.mapwords = []
        self.lines = lines


    def mapping(self):
        for line in self.lines:
            [self.mapwords.append((word, 1)) for word in line]
        
        return self.mapwords