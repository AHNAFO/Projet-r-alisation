from Source import Source

class HumanSource(Source):
    def __init__(self):
        super().__init__("Human", "tab")

    def generateNumberSequence(self, lengthTab):
        str(lengthTab)
        val = []
        for bit in lengthTab:
            val.append(bit)
        return self.setNumberSequence(val)
