# Projet-réalisation

### 2022-2023 ISEN AP4

Ahmed Aboelnaga, Michelle Martin, Adam Ouali, Charles Chaudron, Ulysse Dahiez

# ORACLE

_Réponse qu'une divinité donnait à ceux qui la consultaient._

Ce nom est inspiré des oracles de la Grèce antique, qui étaient considérés comme des canaux de communication entre les dieux et les mortels, capables de fournir des conseils et des prédictions divines

# Dépendances

## Installation des dépendances Python

Le projet étant réalisé à 100% en Python, il vous faudra avoir Python sur votre station de travail.
Pour installer toutes les dépendances Python nécessaires au projet, lancez la commande suivante dans votre terminal en veillant à être à la racine du projet :

```bash
py -m pip install -r requirements.txt
```

Alternative en remplaçant <V> par votre version de Python :

```bash
pip<V> install -r requirements.txt
```

## Installation des dépendances Node

Node est nécessaire pour simuler la fonction d'aléat utilisé par JavaScript (algorithme MWC1616).
Vous pouvez télécharger [node ici](https://nodejs.org/en/download).

# Installation

1. Cloner le dépôt le répertoire souhaité :

```bash
git clone https://github.com/AHNAFO/Projet-realisation.git
```

2. Suivez la section "Dépendances" ci-dessus avant de continuer

3. Aller dans la partie source du projet :

```bash
cd ./oracle/src/
```

4. Lancer le fichier "interface.py" à l'aide de votre version :

```bash
python3 ./interface.py
```

# Ajout de source / Ajout de prédicteur

Grâce à l'architecture orientée objet du projet, il est facilement possible d'ajouter des sources ou des prédicteurs de PRNG.

Il suffit de créer de nouvelles classes dans un nouveau fichier ExempleOracle.py ou ExempleSource.py et de faire hériter ces classes de la classe Predictor ou Source.

Ensuite il faut surcharger certaines méthodes pour que les classes soient fonctionnelles.

Les classes à surcharger sont generateNumberSequence pour les sources et predictNextNumber pour les prédicteurs.

Il faut ensuite ajouter la source et son prédicteur dans le tableau dictSourcesOracle dans le fichier process.py pour controller le fonctionnement.
