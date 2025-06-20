 Module 3 – Algorithmes de Tri (sort_engine.py)

Objectif

Ce module permet d’implémenter et de comparer différents algorithmes de tri appliqués à une liste de livres. Les tris peuvent être effectués selon plusieurs critères : titre, auteur ou année de publication.
 Fonctions principales
 Algorithmes de tri implémentés :
- **Tri à bulles (bubble_sort)**
- **Tri par insertion (insertion_sort)**
- **Tri fusion (récursif) (merge_sort)** (optionnel mais recommandé)

Chaque algorithme peut trier une liste de dictionnaires (livres) selon une clé (titre, auteur, annee).

Comparaison des performances

Fonction : compare_sorts(livres, key)

- Compare le temps d'exécution de chaque algorithme pour un même jeu de données.
- Retourne les résultats triés et le temps d'exécution pour chaque méthode.


Structure attendue des livres

Chaque livre est un dictionnaire au format suivant :

python
{
    "titre": "1984",
    "auteur": "George Orwell",
    "annee": 1949
}


Fonctions utilitaires


Exemple d'utilisation

from sort_engine import trier_par_titre, compare_sorts

livres = [
    {"titre": "Zola", "auteur": "Emile Zola", "annee": 1885},
    {"titre": "L'Étranger", "auteur": "Albert Camus", "annee": 1942},
    {"titre": "1984", "auteur": "George Orwell", "annee": 1949},
]

Tri simple
print(trier_par_titre(livres))

Comparaison des tris
resultats = compare_sorts(livres, key='annee')
for nom_algo, data in resultats.items():
    print(f"{nom_algo}: {data['temps']}s")


Objectifs d’auto-apprentissage

Comprendre les différences de complexité entre les algorithmes (O(n²) vs O(n log n)).

Utiliser la récursivité pour des tris plus performants.

Appliquer le tri sur des objets complexes avec des clés multiple
