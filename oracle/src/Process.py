# - source
from MersenneTwisterSource import MersenneTwisterSource
from MersenneTwisterOracle import MersenneTwisterOracle
from HumanSource import HumanSource
from LCGSource import LCGSource
from LFSRSource import LFSRSource
from RandomOrgSource import RandomOrgSource

# - oracle

# - autre

def process():
    listeDeSources = [MersenneTwisterSource(), RandomOrgSource()]
    

    resultatsDesSources = {}
    for source in listeDeSources:
        source.generateNumberSequence(624)
        resultatsDesSources[source.getName()] = source.getNumberSequence()

    print(resultatsDesSources)


if __name__ == "__main__":
    process() 