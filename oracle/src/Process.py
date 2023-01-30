import MersenneTwisterSource


def process():
    listeDeSources = [MersenneTwisterSource]

    resultatsDesSources = {}
    for source in listeDeSources:
        resultatsDesSources[source.name] = source.getRandomSequence(625)

    
