from MersenneTwisterSource import MersenneTwisterSource


def process():
    #listeDeSources = [MersenneTwisterSource()]
    vara = MersenneTwisterSource()
    print(vara.getName())

    resultatsDesSources = {}
    #for source in listeDeSources:
    #    resultatsDesSources[source().getName()] = source.getRandomSequence(624)


if __name__ == "__main__":
    process() 