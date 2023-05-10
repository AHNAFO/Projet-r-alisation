from Predictor import Predictor
from LCGSource import LCGSource
# https://github.com/TomasGlgg/LCGHack/blob/master/main.py


class LCGOracle(Predictor):

    def __init__(self):
        super().__init__("LCG", "tab")

    def predictNextNumber(self):
        sequence = self.getNumberSequence()

        # self.setNextNumberPredicted(0)
        self.predict_lcg(sequence[-3], sequence[-2], sequence[-1])

    def predict_lcg(self, r0, r1, r2):
        m = 2**31 - 1
        a = ((r1 - r2) * pow(r0 - r1, -1, m)) % m
        c = (r1 - a * r0) % m
        source = LCGSource(r0, a, c, m)
        source.setNumberSequence([r0, r1, r2])
        self.setNextNumberPredicted((a * r2 + c) % m)

        # print(source.ge())

        # return (a, c)
