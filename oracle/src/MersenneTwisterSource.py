from Source import Source
import random

class MersenneTwisterSource(Source):

    def __init__(self):
        super().__init__("Mersenne Twister", "tab")

    def getRandomSequence(self, lengthTab):
        
        random.seed(42)
        mersenne_twister = random.Random()
        random_numbers = [mersenne_twister.random() for _ in range(lengthTab)]
        

        

        
        return random_numbers
    