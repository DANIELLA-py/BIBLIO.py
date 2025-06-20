import json
import csv
import os

# Fichiers de stockage
JSON_FILE = "livres.json"
CSV_FILE = "livres.csv"

# =========================
# Chargement et sauvegarde
# =========================

def charger_livres_json():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r", encoding='utf-8') as f:
            return json.load(f)
    return []

def sauvegarder_livres_json(livres):
    with open(JSON_FILE, "w", encoding='utf-8') as f:
        json.dump(livres, f, ensure_ascii=False, indent=2)

def charger_livres_csv():
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def sauvegarder_livres_csv(livres):
    if not livres:
        return
    with open(CSV_FILE, "w", newline="", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=livres[0].keys())
        writer.writeheader()
        writer.writerows(livres)

# =========================
# Opérations CRUD
# =========================

def generer_id(livres):
    if livres:
        return max(int(livre['id']) for livre in livres) + 1
    return 1

def ajouter_livre(livres, titre, auteur, annee="", isbn=""):
    livre = {
        "id": str(generer_id(livres)),
        "titre": titre,
        "auteur": auteur,
        "annee": annee,
        "isbn": isbn,
        "emprunte": False
    }
    livres.append(livre)
    sauvegarder_livres_json(livres)
    sauvegarder_livres_csv(livres)

def supprimer_livre(livres, id_livre):
    livres[:] = [livre for livre in livres if livre['id'] != str(id_livre)]
    sauvegarder_livres_json(livres)
    sauvegarder_livres_csv(livres)

def modifier_livre(livres, id_livre, titre=None, auteur=None, annee=None, isbn=None):
    for livre in livres:
        if livre['id'] == str(id_livre):
            if titre is not None:
                livre['titre'] = titre
            if auteur is not None:
                livre['auteur'] = auteur
            if annee is not None:
                livre['annee'] = annee
            if isbn is not None:
                livre['isbn'] = isbn
            break
    sauvegarder_livres_json(livres)
    sauvegarder_livres_csv(livres)

def afficher_livres(livres):
    if not livres:
        print("Aucun livre à afficher.")
    for l in livres:
        statut = "Emprunté" if l.get("emprunte", False) else "Disponible"
        print(f"ID: {l['id']}, Titre: {l['titre']}, Auteur: {l['auteur']}, Année: {l.get('annee', 'N/A')}, ISBN: {l.get('isbn', 'N/A')}, Statut: {statut}")

# =========================
# Initialisation du gestionnaire
# =========================

def initialiser_gestionnaire(format="json"):
    if format == "csv":
        return charger_livres_csv()
    else:
        return charger_livres_json()

# =========================
# Exemple de test
# =========================

if __name__ == "__main__":
    livres = initialiser_gestionnaire("json")

    ajouter_livre(livres, "Le Petit Prince", "Antoine de Saint-Exupéry", "1943", "978-0156013987")
    ajouter_livre(livres, "1984", "George Orwell", "1949", "978-0451524935")

    afficher_livres(livres)

    modifier_livre(livres, 1, titre="Le Petit Prince (Édition spéciale)")
    supprimer_livre(livres, 2)

    print("\nAprès modification :")
    afficher_livres(livres)
