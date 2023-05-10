from Source import Source
'''
a est le multiplicateur dans la formule LCG. Il doit être un entier positif qui est relativement premier au module m. La valeur par défaut de a est 1103515245.
c est l'incrément dans la formule LCG. Il doit être un entier positif qui est inférieur à m. La valeur par défaut de c est 12345.
m est le module dans la formule LCG. Il doit être un entier positif et doit être plus grand que les valeurs de a et c. La valeur par défaut de m est 2**31-1, qui est un nombre premier de Mersenne.
'''


class LCGSource(Source):
    def __init__(self, seed=10, a=1103515245, c=12345, m=2**31-1):
        super().__init__("LCG", "tab")
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def generateNumberSequence(self, lengthTab):
        random_numbers = []
        x = self.seed
        for i in range(lengthTab):
            x = (self.a * x + self.c) % self.m
            random_numbers.append(x % lengthTab)
        self.seed = x
        self.setNumberSequence(random_numbers)


""" lcg = LCGSource()
lcg.generateNumberSequence(20)
print(lcg.getNumberSequence()) """