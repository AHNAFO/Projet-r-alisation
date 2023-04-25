from Source import Source
import random


class MSMSource_local(Source):

    def __init__(self):
        super().__init__("MSM2", "tab")
        self.seed = random.randint(1000, 9999)
    
    def generateNumberSequence(self, lengthTab):
        seed = self.seed
        results = []
        for i in range(lengthTab):
            seed = int(str(seed**2).zfill(8)[2:6])
            results.append(seed)
        self.setNumberSequence(results)
        return results
    
    def getNextNumber(self):
        lengthTab = len(self.getNumberSequence())
        return self.generateNumberSequence(lengthTab+1)[-1]