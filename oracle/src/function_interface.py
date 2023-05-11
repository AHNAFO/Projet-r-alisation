from MersenneTwisterSource import MersenneTwisterSource
from MersenneTwisterOracle import MersenneTwisterOracle
from HumanSource import HumanSource
from LCGSource import LCGSource
from LCGOracle import LCGOracle
from RandomOrgOracle import RandomOrgOracle

from RandomOrgSource import RandomOrgBinaireSource
from MWCSSSource import MCSSSource
from MWCSSOracle import MWCSSOracle

from MSMSource_local import MSMSource_local
from MSMOracle import MSMOracle

from MvsMOracle import MvsMOracle


def calculate_begin(tab, human):
    button_select = []
    
    for button in tab:
            if(button['text'] == 1):
                button_select.append(button)
    
    ##Verif si chaine de caractere rentree
    if(human != ""):
        source = HumanSource()
        source.generateNumberSequence(human)
    else:
        numberSequence = []
        sequenceLength = 0
        for button in button_select :
            match(button['image']):
                case "pyimage20":
                    print("MCSS")
                    source = MCSSSource()
                    sequenceLength = 6
                
                case "pyimage16":
                    print("MERSENNE TWISTER")
                    source = MersenneTwisterSource()
                    sequenceLength = 626
                
                case "pyimage14":
                    print("MSM")
                    source = MSMSource_local()
                    sequenceLength = 10
                    
                case "pyimage12":
                    print("LCG")
                    source = LCGSource()
                    sequenceLength = 5
                    
                case "pyimage10":
                    print("RANDOM.ORG")
                    source = RandomOrgBinaireSource()
                    sequenceLength = 50

        source.generateNumberSequence(sequenceLength) if source else numberSequence
        
    numberSequence = source.getNumberSequence()
    
    predictors = []
    for button in button_select :
        match(button['image']):
            #PREDICT
            case "pyimage8":
                #print("MERSENNE TWISTER")
                predictors.append(MersenneTwisterOracle())
                
            case "pyimage22":
                #print("MVSM")
                predictors.append(MvsMOracle())

            
            case "pyimage6":
                #print("MSM")
                predictors.append(MSMOracle())

            case "pyimage4":
                #print("LCG")
                predictors.append(LCGOracle())

            case "pyimage2":
                #print("MWCSS")
                predictors.append(MWCSSOracle())

            case "pyimage18":
                #print("KNN")
                predictors.append(RandomOrgOracle())
    
    # TODO: ici set le attendu genre setAttendu(numberSequence[-1])
    to_render = []
    for predictor in predictors:
        predictor.setNumberSequence(numberSequence[:-1])
        predictor.setLastNumberSequence(numberSequence[-1])
        #Premiere valeur envoyee est l'attendu
        to_render.append(predictor)
        try :
            predictor.predictNextNumber()
        except:
            predictor.setNextNumberPredicted(0)
        
        #Enregistre le reste dans le tab
        to_render.append(predictor)      
        # TODO: ici set le point d'interrogation genre setMachin(predictor.getName(), predictor.getNextNumberPredicted())
        
        print(predictor.getName(), numberSequence[-1], ' -> ', predictor.getNextNumberPredicted())
    return to_render


    
def change_color_button(button,image,image_select):
            
    #Change couleur -------------
    if(button['text'] == True):
        button['image'] = image
        button['text'] = False
    else:
        button['image'] = image_select
        button['text'] = True
    # -------------
