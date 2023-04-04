from Predictor import Predictor

import numpy as np

'''
cette methode utilise KNN,, c'est à dire les plus proches voisins.
Les valeurs etant réélement aléatoire, elles ne peuvent être prédictible.



c'est pour ça que ça ne fonctionne pas.

'''

class RandomOrgOracle(Predictor):

    def __init__(self):
        super().__init__("RandomOrg", "tab")

    def predictNextNumber(self):

        data = self.getNumberSequence()
        
         # Longueur de la fenêtre de prédiction
        window_size = 5

        # Valeurs précédentes à utiliser pour la prédiction
        X = []

        # Valeurs suivantes à prédire
        y = []

        for i in range(window_size, len(data)):
            X.append(data[i-window_size:i])
            y.append(data[i])

        # Convertir en tableaux numpy
        X = np.array(X)
        y = np.array(y)

        # Entrée à prédire
        x_pred = [0,0,0,0,0]

        # Nombre de voisins à considérer
        k = 3

        # Calculer la distance entre l'entrée à prédire et toutes les autres entrées
        distances = np.sqrt(np.sum((X - x_pred)**2, axis=1))

        # Trier les distances par ordre croissant
        idx = np.argsort(distances)

        # Prendre les k plus proches voisins et calculer la moyenne de leurs sorties
        output = np.mean(y[idx[:k]])
        return output
RO = RandomOrgOracle()
print(RO.predictNextNumber())