import subprocess
import json

class MCSSSource(Source):
    def __init__(self):
        super().__init__("MWCSS", "tab")
        

    def generateNumberSequence(self, lengthTab):
        # Définir le code JavaScript dans une chaîne
        code_js = """console.log(Array.from(Array(6), Math.random));"""

        # Exécuter le code JavaScript avec Node.js et stocker le résultat dans une variable Python
        resultat = subprocess.check_output(["node", "-e", code_js])

        # Afficher le résultat
        print(resultat.decode().strip())
        return json.loads(resultat.decode().strip())
    
    