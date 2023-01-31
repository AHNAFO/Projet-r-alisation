# - source
from MersenneTwisterSource import MersenneTwisterSource
from BlumBlumShubSource import BlumBlumShubSource
from HumanSource import HumanSource
from LCGSource import LCGSource
from LFSRSource import LFSRSource
from RandomOrgSource import RandomOrgSource

# - oracle

# - autre

def process():
    listeDeSources = [MersenneTwisterSource()]
    

    resultatsDesSources = {}
    for source in listeDeSources:
        resultatsDesSources[source.getName()] = source.getRandomSequence(624)
    print(resultatsDesSources)


if __name__ == "__main__":
    process() 