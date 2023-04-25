from Predictor import Predictor
from MSMSource import MSMSource
class MSMOracle(Predictor):

    def __init__(self, numberSq):
        super().__init__("MiddleSquare", "tab")
        self.setNumberSequence(numberSq)

    def predictNextNumber(self):
        sequence = self.getNumberSequence()
        digits  = len(str(sequence[0]))
        last_number = sequence[-1]
        seed_str = str(last_number**2).zfill(digits*2)
        mid = len(seed_str) // 2
        self.setNextNumberPredicted(int(seed_str[mid-digits//2:mid+digits//2]))
        self.numberSequence.append(self.getNextNumberPredicted())
        return self.getNextNumberPredicted()


# to generate MSQ sequence https://sadale.net/27/online-middle-square-method-generator
