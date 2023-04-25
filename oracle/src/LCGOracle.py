from Predictor import Predictor

#https://github.com/TomasGlgg/LCGHack/blob/master/main.py

class LCGOracle(Predictor):

    def __init__(self):
        super().__init__("LCG", "tab")

    def predictNextNumber(self):


        self.setNextNumberPredicted(0)
    
    