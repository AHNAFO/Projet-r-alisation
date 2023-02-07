# - source
from MersenneTwisterSource import MersenneTwisterSource
from MersenneTwisterOracle import MersenneTwisterOracle
from HumanSource import HumanSource
from LCGSource import LCGSource
from LFSRSource import LFSRSource
from RandomOrgSource import RandomOrgDecimalSource, RandomOrgBinaireSource

# - oracle
from  RandomOrgOracle import RandomOrgOracle

# - autre

def process():
    listeDeSources = [MersenneTwisterSource(), RandomOrgDecimalSource(), RandomOrgBinaireSource()]
    

    resultatsDesSources = {}
    for source in listeDeSources:
        source.generateNumberSequence()
        resultatsDesSources[source.getName()] = source.getNumberSequence()

    print(resultatsDesSources)


if __name__ == "__main__":
    process() 