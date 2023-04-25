# - source
from MersenneTwisterSource import MersenneTwisterSource
from HumanSource import HumanSource
from LCGSource import LCGSource
from LFSRSource import LFSRSource
from RandomOrgSource import RandomOrgDecimalSource, RandomOrgBinaireSource
from MSMSource import MSMSource

# - oracle
from MersenneTwisterOracle import MersenneTwisterOracle
from  RandomOrgOracle import RandomOrgOracle
from MSMOracle import MSMOracle

# - autre

def process():
    listeDeSources = [LCGSource()]
    

    resultatsDesSources = {}
    for source in listeDeSources:
        source.generateNumberSequence(101)
        resultatsDesSources[source.getName()] = source.getNumberSequence()

    print(resultatsDesSources)


def testMT():
    source = MersenneTwisterSource()
    oracle = MersenneTwisterOracle()

    
    source.generateNumberSequence(626)

    oracle.setNumberSequence(source.getNumberSequence())
    oracle.predictNextNumber()

    print(source.getNextNumber(), '=', oracle.getNextNumberPredicted(), ':',
        f'{source.getNextNumber() == oracle.getNextNumberPredicted() }')
    
def testMSM():
    source = MSMSource()
    oracle = MSMOracle()

    
    source.generateNumberSequence(100)

    oracle.setNumberSequence(source.getNumberSequence())
    oracle.predictNextNumber()

    print(source.getNextNumber(), '=', oracle.getNextNumberPredicted(), ':',
        f'{source.getNextNumber() == oracle.getNextNumberPredicted()}')


if __name__ == "__main__":
    # process() 
    # testMT()
    testMSM()