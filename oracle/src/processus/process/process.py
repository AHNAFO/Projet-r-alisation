import sys
sys.path.append("C:\\Users\\Ulysse Dahiez\\Documents\\AP4\\projet_recherche\\oracle\\Projet-realisation\\oracle\\src\\source\\generator\\MersenneTwisterSource.py")
print(sys.path)
import MersenneTwisterSource 


def process():
    listeDeSources = [MersenneTwisterSource]

    resultatsDesSources = {}
    for source in listeDeSources:
        resultatsDesSources[source.name] = source.getRandomSequence(625)

    
