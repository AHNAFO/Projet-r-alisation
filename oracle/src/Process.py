from MersenneTwisterSource import MersenneTwisterSource


def process():
    listeDeSources = [MersenneTwisterSource()]
    

    resultatsDesSources = {}
    for source in listeDeSources:
        resultatsDesSources[source.getName()] = source.getRandomSequence(624)
    print(resultatsDesSources)


if __name__ == "__main__":
    process() 