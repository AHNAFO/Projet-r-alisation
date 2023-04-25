from Source import Source
import random


class MSMSource2(Source):

    def __init__(self):
        super().__init__("MSM2", "tab")
    
    def generateNumberSequence(self, lengthTab):
        self.seed = random.randint(1000, 9999)
        results = []
        for i in range(lengthTab):
            self.seed = int(str(self.seed**2).zfill(8)[2:6])
            results.append(self.seed)
        self.setNumberSequence(results[:-1])
        self.setNextNumber(results[-1])
        return results

# Example usage
prng = MSMSource2()
random_numbers = prng.generateNumberSequence(10)
print(random_numbers)