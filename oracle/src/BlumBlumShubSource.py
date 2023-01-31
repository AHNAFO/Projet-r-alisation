from Source import Source

class BlumBlumShubSource(Source):

    def __init__(self):
        super().__init__("Blum Blum Shub", "tab")

    def getRandomSequence(self, lengthTab):
        return