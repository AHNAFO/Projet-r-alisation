import subprocess
import json
from Source import Source

class MCSSSource(Source):
    def __init__(self):
        super().__init__("MWCSS", "tab")
        

    def generateNumberSequence(self, lengthTab):
        # Définir le code JavaScript dans une chaîne
        lengthTab = 100 if lengthTab > 100 else lengthTab
        code_js = "console.log(Array.from(Array({lengthTab}), Math.random));".format(lengthTab=lengthTab)

        # Exécuter le code JavaScript avec Node.js et stocker le résultat dans une variable Python
        resultat = subprocess.check_output(["node", "-e", code_js])

        # Afficher le résultat
        self.setNumberSequence(json.loads(resultat.decode().strip()))
