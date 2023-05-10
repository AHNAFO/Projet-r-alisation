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
    for button in button_select :
        print(button['image'])
        match(button['image']):
            #PREDICT
            case "pyimage8":
                print("MERSENNE TWISTER")
                
            case "pyimage22":
                print("MVSM")
            
            case "pyimage6":
                print("MSM")
            
            case "pyimage4":
                print("LCG")
                
            case "pyimage2":
                print("MWCSS")
            
            case "pyimage18":
                print("KNN")
                
            # SOURCES
            case "pyimage10":
                print("MCSS")
            
            case "pyimage12":
                print("MERSENNE TWISTER")
            
            case "pyimage14":
                print("MSM")
                
            case "pyimage16":
                print("LCG")
                
            case "pyimage20":
                print("RANDOM.ORG")
        

    
def change_color_button(button,image,image_select):
    
    global check_source
    global check_predicteur
        
    source_select = ['pyimage16','pyimage14','pyimage12','pyimage10','pyimage20']
    source_deselect = ['pyimage15','pyimage13','pyimage11','pyimage9','pyimage19']
    predicteur_select = ['pyimage8','pyimage6','pyimage4','pyimage2','pyimage22','pyimage18']
    predicteur_deselect = ['pyimage7','pyimage5','pyimage3','pyimage1','pyimage21','pyimage17']
    
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
    


