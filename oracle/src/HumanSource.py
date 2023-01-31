from Source import Source

class HumanSource(Source):

    def __init__(self):
        super().__init__("Human", "tab")

    def getRandomSequence(self, lengthTab):
        return