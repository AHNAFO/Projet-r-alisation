class Predictor(object):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def setNumberSequence(self, numberSequence):
        self.numberSequence = numberSequence

    def setNextNumberPredicted(self, nextNumberPredicted):
        self.nextNumberPredicted = nextNumberPredicted

    def getNumberSequence(self):
        return self.numberSequence

    def getNextNumberPredicted(self):
        return self.nextNumberPredicted

    def generateNumberSequence(self):
        pass

    def predictNextNumber(self):
        self.setNextNumberPredicted(0)
        pass
