# cette classe retourne un tableau de n nombre random.
# le nombre n est defini par les besoins de son predicteur respectif


class Source(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def setNumberSequence(self, numberSequence):
        self.numberSequence = numberSequence

    def setNextNumber(self, nextNumber):
        self.nextNumber = nextNumber

    def getNumberSequence(self):
        return self.numberSequence

    def getNextNumber(self):
        return self.nextNumber

    def generateNumberSequence(self, lengthTab):
        pass
