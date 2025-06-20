 gestion des bibliotheques

Ce projet Python simple permet de gérer une collection de livres dans une bibliothèque, en suivant les emprunts et les retours.

 Fonctionnalités

- Ajouter un livre à la bibliothèque
- Emprunter un livre (avec date d'emprunt)
- Retourner un livre
- Afficher le statut d'un livre
- Lister les livres disponibles
- Lister les livres empruntés
 Utilisation

 Création d'un livre

```python
livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
Ajouter à la bibliothèque
python
biblio = Bibliotheque()
biblio.ajouter_livre(livre1)
Emprunter un livre
python
livre1.emprunter("Alice")
Retourner un livre
python
livre1.retourner()
Afficher le statut d'un livre
python
livre1.statut()
Lister tous les livres empruntés
python
biblio.lister_livres_empruntes()
Lister tous les livres disponibles
python
biblio.lister_livres_disponibles()
 Structure
Livre: classe représentant un livre individuel.

Bibliotheque: classe contenant une liste de livres et leurs statuts.

 Prérequis
Python 3.x
 Licence
Ce projet est open-source, n’hésite pas à le modifier ou à le réutiliser.