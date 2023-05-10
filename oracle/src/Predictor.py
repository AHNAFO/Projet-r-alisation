class Predictor(object):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def getName(self):
        return self.name

    def setNumberSequence(self, numberSequence):
        self.numberSequence = numberSequence
    
    def setLastNumberSequence(self, lastNumber):
        self.lastNumber = lastNumber

    def setNextNumberPredicted(self, nextNumberPredicted):
        self.nextNumberPredicted = nextNumberPredicted
    
    def getLastNumberSequence(self):
        return self.lastNumber

    def getNumberSequence(self):
        return self.numberSequence

    def getNextNumberPredicted(self):
        return self.nextNumberPredicted

    def generateNumberSequence(self):
        pass

    def predictNextNumber(self):
        self.setNextNumberPredicted(0)
        pass
