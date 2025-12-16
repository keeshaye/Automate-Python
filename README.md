# Automate-Python

Ce projet a pour objectif d’implémenter en Python une structure complète permettant de manipuler des automates finis et d’appliquer les principales opérations classiques de la théorie des langages formels.
Il a été réalisé dans le cadre du module LU2IN005 – Mathématique discrètes.

Le projet comprend plusieurs fonctionnalités essentielles :

🔹 Manipulation d’automates

- Création d’états et de transitions
- Construction d’automates à partir de fichiers
- Visualisation graphique des automates
- Tests de transitions et manipulation de l’ensemble des états

🔹 Opérations fondamentales

- Successeur et acceptation de mots
- Test de déterminisme
- Test de complétude
- Complétion d’un automate
- Déterminisation

🔹 Opérations sur les langages

- Complémentaire
- Intersection
- Union
- Concaténation
- Étoile de Kleene

🔹 Application : extraction de nombres décimaux

Le projet se conclut par une application pratique :
extraction dans un fichier texte de nombres décimaux complets (comme 123,456) grâce à un automate spécifiquement construit.
Cette partie remplace l’utilisation de regex par un analyseur purement automatisé.

🔹 Contenu du dépôt

- projet_etudiant.ipynb : notebook Python permettant de tester et manipuler les automates, avec création d’automates à partir de fichiers, affichage, et vérification d’égalité d’états.

- automateBase.py : classes et outils de base pour la construction et la manipulation d’automates.

- myparse.py : définit un parser (MyParser) permettant de lire un fichier texte décrivant un automate et d’en extraire les états, transitions et ensembles initiaux/finals.

- rename_files.py : renomme tous les fichiers d’un répertoire en conservant uniquement la partie avant le premier underscore, en changeant leur extension en .py.

- sp.py : bibliothèque Python pour créer des analyseurs syntaxiques (parsers) récursifs, offrant des parsers pour séquences, alternatives, répétitions, constantes, positions et transformations, avec gestion d'espaces et d'erreurs.

- state.py : définit la classe State représentant un état d'automate avec identifiant, indicateurs initiaux et finaux, label, et méthodes pour comparaison, hachage, préfixage et tests d'appartenance dans un ensemble.

- test.py : script modifiable qui crée un automate à partir d'un fichier, affiche sa représentation graphique, et teste l'égalité de deux états.

- transition.py : définit la classe Transition représentant une transition d'automate avec étiquette, état source et état destination, et surcharge les méthodes __repr__, __eq__ et __hash__.

- fichiers .txt utilisés pour créer des automates de test

🔹 Objectifs pédagogiques

- Comprendre en profondeur la logique des automates finis
- Implémenter proprement des algorithmes théoriques
- Apprendre à concevoir une application simple basée sur les automates
