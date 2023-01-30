import Source
import random
class MersenneTwisterSource(Source):

    def __init__(self):
        super()

    def getRandomSequence(lengthTab):
        
        random.seed(42)
        mersenne_twister = random.Random()

        random_numbers = [mersenne_twister.random() for _ in range(624)]


        

        
        return random_numbers
    