# Module1 - Gestionnaire de livres

Ce module permet de gérer une collection de livres en utilisant des fichiers JSON et CSV pour la sauvegarde des données.

## Fonctionnalités

- Charger et sauvegarder les livres au format JSON et CSV
- Ajouter un livre
- Supprimer un livre
- Modifier un livre
- Afficher la liste des livres

## Utilisation

Exemple d'utilisation :

```python
from data_manager import *

livres = charger_livres_json()
ajouter_livre(livres, "Le Petit Prince", "Antoine de Saint-Exupéry")
supprimer_livre(livres, 1)
modifier_livre(livres, 2, titre="Le Petit Prince Modifié", auteur="Antoine de Saint-Exupéry Modifié")
afficher_livres()