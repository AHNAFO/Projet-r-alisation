from Source import Source
import sympy
import random
import re 
import sys

class BlumBlumShubSource(Source):

    def __init__(self):
        super().__init__("Blum Blum Shub", "tab")

    def getRandomSequence(self, lengthTab):

        x = 3*10**10
        y = 4*10**10

        # x0 = random.randint(1,1e10)
        x0 = 5

        def next_usable_prime(x):
                p = sympy.nextprime(x)
                while (p % 4 != 3):
                    p = sympy.nextprime(p)
                return p

        p = next_usable_prime(x)
        q = next_usable_prime(y)
        M = p*q

        tabToReturn = [x0]

        for i in range(lengthTab) :
            tabToReturn.append((tabToReturn[i]**2)%M)

        return tabToReturn

        #exemple de valeur de retour avec seed (x0) à 5 : [5, 25, 625, 390625, 152587890625, 483064294516962885438, 20772018519563073652, 205383887955409882437, 1009828992224087349751, 913124184850349197683, 980761879802178053404, 870309737459218601102, 647952078631667430994, 94512454024282129514, 663749920216383682032, 1110670786047972415262, 596344176261751549135, 784651469454686430335, 790838821360681691816, 745004287752291712373, 846005292963064350668]