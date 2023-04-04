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

        data = [5, 6, 4, 9, 5, 8, 0, 8, 10, 5, 1, 8, 4, 8, 0, 5, 8, 10, 10, 10, 8, 2, 3, 5, 10, 8, 1, 2, 6, 7, 5, 5, 6, 1, 5, 2, 4, 8, 5, 0, 8, 9, 3, 5, 2, 5, 9, 6, 5, 1, 6, 2, 4, 8, 8, 0, 2, 1, 8, 10, 6, 2, 1, 2, 0, 0, 1, 1, 9, 1, 7, 7, 6, 2, 9, 6, 3, 0, 8, 3, 5, 0, 1, 10, 5, 1, 6, 9, 9, 7, 1, 7, 5, 3]
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