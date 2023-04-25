# - source
from MersenneTwisterSource import MersenneTwisterSource
from MersenneTwisterOracle import MersenneTwisterOracle
from HumanSource import HumanSource
from LCGSource import LCGSource
from LCGOracle import LCGOracle
from LFSRSource import LFSRSource
from RandomOrgSource import RandomOrgDecimalSource
from MWCSSSource import MCSSSource
from MWCSSOracle import MWCSSOracle
from MSMSource_web import MSMSource_web
from MSMSource_local import MSMSource_local
from MSMOracle import MSMOracle

# - oracle
from MersenneTwisterOracle import MersenneTwisterOracle
from MSMOracle import MSMOracle

# - autre


def process():
    dictSourcesOracle = [
        (LCGSource(), LCGOracle),
        (MersenneTwisterSource(), MersenneTwisterOracle),
        (RandomOrgDecimalSource(), None),
        (MCSSSource(), MWCSSOracle),
        (MSMSource_local(), MSMOracle),
        (HumanSource(), None),
    ]

    resultatsDesSources = {}
    for (source, oracle) in dictSourcesOracle:
        source.generateNumberSequence(1000)
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
    source = MSMSource_local()
    oracle = MSMOracle()

    source.generateNumberSequence(100)

    oracle.setNumberSequence(source.getNumberSequence())
    oracle.predictNextNumber()

    print(source.getNextNumber(), '=', oracle.getNextNumberPredicted(), ':',
          f'{source.getNextNumber() == oracle.getNextNumberPredicted()}')


if __name__ == "__main__":
    process()
    # testMT()
    # testMSM()
