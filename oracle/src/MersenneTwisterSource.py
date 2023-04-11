from Source import Source
import random
import time

class MersenneTwisterSource(Source):

    def __init__(self):
        super().__init__("Mersenne Twister", "tab")

    def generateNumberSequence(self, lengthTab):
        random.seed(time.time())

        # python utilise Mersenne twister dans son module Random
        mersenne_twister = random.Random()
        random_numbers = [mersenne_twister.getrandbits(32) for _ in range(lengthTab - 1)]
        
        self.setNumberSequence(random_numbers)
        self.setNextNumber(mersenne_twister.getrandbits(32))
    