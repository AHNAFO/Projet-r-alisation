from Source import Source
import random
'''
a est le multiplicateur dans la formule LCG. Il doit être un entier positif qui est relativement premier au module m. La valeur par défaut de a est 1103515245.
c est l'incrément dans la formule LCG. Il doit être un entier positif qui est inférieur à m. La valeur par défaut de c est 12345.
m est le module dans la formule LCG. Il doit être un entier positif et doit être plus grand que les valeurs de a et c. La valeur par défaut de m est 2**31-1, qui est un nombre premier de Mersenne.
'''


class LCGSource(Source):
    def __init__(self, seed=None, a=None, c=None, m=2**31-1):
        super().__init__("LCG", "tab")
        self.seed = seed if seed else random.randint(0, 100_000_000)
        self.a = a if a else random.randint(0, 100_000_000)
        self.c = c if c else random.randint(0, 100_000_000)
        self.m = m
        print(self.a, self.c, self.m, self.seed)

    def generateNumberSequence(self, lengthTab):
        random_numbers = []
        x = self.seed
        for i in range(lengthTab):
            x = (self.a * x + self.c) % self.m
            random_numbers.append(x)
        self.seed = x
        self.setNumberSequence(random_numbers)


""" lcg = LCGSource()
lcg.generateNumberSequence(20)
print(lcg.getNumberSequence()) """
