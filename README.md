# # BiblioPy

## 1. Présentation du Projet

**BiblioPy** est un gestionnaire de bibliothèque en ligne de commande permettant de gérer un catalogue de livres. Cet outil permet d’ajouter, rechercher, trier et gérer les emprunts de livres depuis une interface textuelle simple. Les données sont stockées dans des fichiers persistants (CSV ou JSON).

---

## 2. Fonctionnalités

- **Ajouter, supprimer et modifier** les livres du catalogue.
- **Rechercher** des livres par titre, auteur ou ISBN (avec différents algorithmes de recherche).
- **Afficher** la liste des livres triée par différents critères (titre, auteur, année).
- **Marquer** les livres comme empruntés ou retournés.
- **Lister** les livres actuellement empruntés ou disponibles.
- **Interface utilisateur** en ligne de commande claire et interactive.
- **Rapport simple** : total de livres, livres empruntés, liste par statut.

---

## 3. Architecture et Modules

Le projet est structuré en 5 modules principaux pour assurer modularité et clarté :

### 3.1 Module 1 : Gestion des Données (`data_manager.py`)
- Lecture/écriture des données de livres depuis/vers un fichier (CSV/JSON).
- Ajout, suppression, modification des livres dans la structure en mémoire (liste de dictionnaires).
- Gestion des identifiants uniques pour chaque livre.

### 3.2 Module 2 : Algorithmes de Recherche (`search_engine.py`)
- Recherche séquentielle.
- Recherche dichotomique (sur données triées).
- Recherche par titre, auteur, ISBN.
- Comparaison des performances et gestion des recherches multi-critères simples.

### 3.3 Module 3 : Algorithmes de Tri (`sort_engine.py`)
- Implémentation d’au moins deux tris : tri à bulles, tri par sélection, tri par insertion, etc.
- (Optionnel) Tri récursif : tri fusion, tri rapide.
- Tri par titre, auteur, année de publication.

### 3.4 Module 4 : Gestion des Emprunts (`loan_manager.py`)
- Marquer un livre comme "emprunté" (avec date, nom de l’emprunteur possible).
- Marquer comme "retourné".
- Lister tous les livres empruntés ou disponibles.

### 3.5 Module 5 : Interface Utilisateur & Rapports (`cli_interface.py`)
- Menu principal en ligne de commande.
- Gestion des interactions utilisateur et affichage formaté.
- Génération d’un rapport synthétique sur les livres.

---

## 4. Schéma d’Interaction

```
+-------------------------+
|   Interface CLI         |
| (cli_interface.py)      |
+-----------+-------------+
            |
            v
+-------------------------+
|   Modules Métiers       |
+-------------------------+
| - data_manager.py       |
| - search_engine.py      |
| - sort_engine.py        |
| - loan_manager.py       |
+-------------------------+
            |
            v
+-------------------------+
|   Fichier de Données    |
|  (CSV ou JSON)          |
+-------------------------+
```

---

## 5. Choix Techniques

- **Langage** : Python 3.x
- **Structures de données** : listes et dictionnaires pour une gestion souple et efficace des livres.
- **Persistance** : fichiers JSON ou CSV pour la sauvegarde des données.

---

## 6. Installation et Utilisation

1. **Clonez le dépôt :**
   ```bash
   git clone https://github.com/DANIELLA-py/BIBLIO.py.git
   cd BIBLIO.py
   ```
2. **Lancez l’application :**
   ```bash
   python cli_interface.py
   ```
3. **(Optionnel) Dépendances :**
   - Standard Python modules seulement (csv, json, os, etc.).

---

## 7. Exemples de Commandes

- Ajouter un livre
- Rechercher un livre par titre
- Trier les livres par auteur
- Marquer un livre comme emprunté
- Générer un rapport

---

## 8. Tests

- Divers scénarios de tests pour chaque fonctionnalité majeure.
- Vérification manuelle de la cohérence des données après chaque opération.
- Exemples de résultats inclus dans le rapport final.

---

## 9. Difficultés Rencontrées

- Gestion de la cohérence des données lors d’opérations concurrentes.
- Optimisation des algorithmes de recherche et de tri sur de grands volumes de données.
- Validation robuste des entrées utilisateur.

---

## 10. Perspectives d’Amélioration

- Interface graphique (GUI).
- Gestion multi-utilisateurs et authentification.
- Export/Import avancé (PDF, Excel).
- Statistiques plus détaillées sur les emprunts et les livres.

---

## 11. Auteurs

- Projet réalisé par 5 étudiants dans le cadre du module d’algorithmique et de programmation Python.

---

## 12. Licence

Ce projet est sous licence MIT.

---
