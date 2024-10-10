# Jeu de Triominos en Python avec Tkinter

## Description

Ce projet implémente un jeu de Triominos en utilisant Python et Tkinter pour l'interface graphique. Le jeu propose deux modes : jouer à deux joueurs (en local) ou jouer contre une Intelligence Artificielle (IA). Le jeu utilise une interface conviviale, permettant aux utilisateurs de faire pivoter les pièces et de les placer sur le plateau, avec des scores mis à jour automatiquement.

## Fonctionnalités

- **Modes de Jeu** :
  - Jouer à deux joueurs en local.
  - Jouer contre une Intelligence Artificielle.
- **Gestion des Scores** : Les scores des joueurs sont calculés en fonction des pièces posées et des actions réalisées.
- **Rotation des Pièces** : Les joueurs peuvent faire pivoter les pièces avant de les placer sur le plateau.
- **Interface Graphique** : Développée avec Tkinter, l'interface permet une interaction intuitive et visuelle avec le jeu.

## Prérequis

- Python 3.x
- Bibliothèque Tkinter (incluse par défaut avec Python)

## Installation et Lancement

1. Clonez ce dépôt sur votre machine locale :
   ```sh
   git clone <URL-du-dépôt>
   ```
2. Accédez au dossier du jeu :
   ```sh
   cd chemin/vers/Jeu_Triominos
   ```

### Lancer le Jeu

- Pour accéder à l'écran d'accueil et choisir un mode de jeu, exécutez :
  ```sh
  python Jeu_Triominos.py
  ```
- Pour jouer uniquement à deux joueurs en local, exécutez :
  ```sh
  python Triominos.py
  ```
- Pour jouer contre l'IA, exécutez :
  ```sh
  python Triominos_IA.py
  ```

## Structure du Projet

- **Classes.py** : Contient les classes principales du jeu, y compris `Pion`, `Player` et `Game`.
- **Jeu_Triominos.py** : Fichier principal pour lancer le jeu avec écran d'accueil et choix des modes de jeu.
- **Triominos.py** : Fichier pour jouer à deux joueurs en local.
- **Triominos_IA.py** : Fichier pour jouer contre l'Intelligence Artificielle.

## Contrôles du Jeu

- **Clic gauche sur un Triomino** : Sélectionner la pièce.
- **Double clic sur un Triomino** : Faire pivoter la pièce (pas de rotation possible au début du jeu).
- **Bouton "Piocher"** : Permet de piocher une nouvelle pièce si nécessaire.
- **Bouton "Quitter"** : Ferme le jeu et retourne à l'écran d'accueil.
- **Bouton "Recommencer"** : Relance une nouvelle partie.

## Collaborateurs

- Arafat Feical Idriss
- Ismael Sow

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

