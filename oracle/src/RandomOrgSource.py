from Source import Source
import RandomOrgAPI as ROA

class RandomOrgSource(Source):

    def __init__(self):
        super().__init__("Random Org", "tab")

    def generateNumberSequence(self, lengthTab):
        self.setNumberSequence(ROA.getListRandomOrg(lengthTab))