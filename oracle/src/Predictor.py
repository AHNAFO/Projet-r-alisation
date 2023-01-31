class Predictor(object):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def setNumberSequence(self, numberSequence):
        self.numberSequence = numberSequence

    def setNextNumber(self, nextNumber):
        self.nextNumber = nextNumber

    def setNextNumberPredicted(self, nextNumberPredicted):
        self.nextNumberPredicted = nextNumberPredicted

    def getNumberSequence(self):
        return self.numberSequence

    def getNextNumber(self):
        return self.nextNumber

    def getNextNumberPredicted(self):
        return self.nextNumberPredicted

    def generateNumberSequence(self):
        pass

    def predictNextNumber(self):
        # TODO: Override in children
        pass
