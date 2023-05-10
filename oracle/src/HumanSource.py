from Source import Source

class HumanSource(Source):
    def __init__(self):
        super().__init__("Human", "tab")

    def generateNumberSequence(self, lengthTab):
        return self.setNumberSequence('10101000001010101101001010001000100100101111111001011110010111')
