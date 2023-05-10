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

def variableGlobale():
    global check_source
    global check_predicteur
    
    check_source = False
    check_predicteur = False
    print("pass")
    

def calculate_begin(tab):
    button_select = []
    for button in tab:
        if(button['text'] == 1):
            button_select.append(button)

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
                sequenceLength = 625
            
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
                print("MERSENNE TWISTER")
                predictors.append(MersenneTwisterOracle())
                
            case "pyimage22":
                print("MVSM")
                predictors.append(MvsMOracle())

            
            case "pyimage6":
                print("MSM")
                predictors.append(MSMOracle())

            
            case "pyimage4":
                print("LCG")
                predictors.append(LCGOracle())

                
            case "pyimage2":
                print("MWCSS")
                predictors.append(MWCSSOracle())

            
            case "pyimage18":
                print("KNN")
                predictors.append(RandomOrgOracle())
    
    for predictor in predictors:
        predictor.setNumberSequence(numberSequence[:-1])
        try :
            predictor.predictNextNumber()
        except:
            predictor.setNextNumberPredicted(0)

        print(predictor.getName(), numberSequence[-1], ' -> ', predictor.getNextNumberPredicted())
    


    
def change_color_button(button,image,image_select):
    
    global check_source
    global check_predicteur
        
    source_deselect = ['pyimage15','pyimage14','pyimage12','pyimage10','pyimage20']
    source_select = ['pyimage16','pyimage13','pyimage11','pyimage9','pyimage19']
    predicteur_deselect = ['pyimage8','pyimage6','pyimage4','pyimage2','pyimage22','pyimage18']
    predicteur_select = ['pyimage7','pyimage5','pyimage3','pyimage1','pyimage21','pyimage17']
    
    print(button['image'])
    
    #Change couleur -------------
    if(button['text'] == True):
        button['image'] = image
        button['text'] = False
    else:
        button['image'] = image_select
        button['text'] = True
    # -------------

    #Retiens bouton ----------------- 
    if(button['image'] in source_select):
        check_source = True
    elif(button['image'] in source_deselect):
        check_source = False
    
    if(button['image'] in predicteur_select):
        check_predicteur = True
    elif(button['image'] in predicteur_deselect):
        check_predicteur = False
    
    if((check_source == True) and (check_predicteur == True)):
        print("DOUBLE")
        
    
    print("Source : ",check_source)
    print("Predicteur : ",check_predicteur)
    


