 Moteur de Recherche de Livres en Python

Ce projet Python fournit un ensemble de fonctions pour effectuer des recherches efficaces dans une liste de livres, selon différents critères (titre, auteur, ISBN). Il permet également de comparer les performances entre recherche séquentielle et dichotomique.

 Fonctionnalités

- Recherche par **titre**, **auteur** ou **ISBN**
- Recherche par **plusieurs critères** (titre et/ou auteur)
- Comparaison des performances entre :
  -  **Recherche séquentielle** : complexité O(n)
  -  **Recherche dichotomique** : complexité O(log n) (avec tri préalable)
  
 Structure des données

Les livres sont stockés dans une liste de dictionnaires avec les clés suivantes :
- `titre`
- `auteur`
- `ISBN`

 Fonctions principales

- `recherche_sequentielle(liste, cle, valeur)`
- `recherche_dichotomique(liste, cle, valeur)`
- `recherche_par_titre(titre, methode="sequentielle")`
- `rechercher_par_auteur(auteur, methode="sequentielle")`
- `recherche_par_ISBN(ISBN)`
- `recherche_multi_critere(titre=None, auteur=None)`
- `comparaison_performances(cle, valeur)`


```python
resultat = recherche_par_titre("Deep learning")
print(resultat)
