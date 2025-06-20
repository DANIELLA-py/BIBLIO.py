import os
from Module1.data_manager import (
    initialiser_gestionnaire,
    ajouter_livre,
    supprimer_livre,
    modifier_livre,
    afficher_livres,
    sauvegarder_livres_json
)
from Module2.search_engine import (
    recherche_par_titre,
    rechercher_par_auteur,
    recherche_par_ISBN
)
from Module3.sort_engine import trier_livres, compare_sorts
from Module4.loan_manager import Livre, Bibliotheque

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def afficher_menu():
    print("=== BiblioPy - Système de gestion de livres ===")
    print("1. Afficher tous les livres")
    print("2. Ajouter un livre")
    print("3. Supprimer un livre")
    print("4. Modifier un livre")
    print("5. Rechercher un livre")
    print("6. Trier les livres")
    print("7. Emprunter un livre")
    print("8. Retourner un livre")
    print("9. Livres empruntés")
    print("10. Livres disponibles")
    print("11. Générer un rapport")
    print("12. Comparer les performances des tris")
    print("0. Quitter")
    print("===============================================")

def input_book_data():
    return {
        "titre": input("Titre: "),
        "auteur": input("Auteur: "),
        "annee": input("Année de publication: "),
        "isbn": input("ISBN: "),
        "emprunte": False
    }

def generate_report(livres):
    total = len(livres)
    empruntes = len([l for l in livres if l.get("emprunte", False)])
    disponibles = total - empruntes

    print("\n=== Rapport Bibliothèque ===")
    print(f"Total de livres      : {total}")
    print(f"Livres empruntés     : {empruntes}")
    print(f"Livres disponibles   : {disponibles}")
    print("======================================\n")

def main():
    livres_data = initialiser_gestionnaire("json")
    biblio = Bibliotheque()

    for l in livres_data:
        livre = Livre(l['titre'], l['auteur'])
        if l.get("emprunte", False):
            livre.emprunter(l.get("emprunteur", "Inconnu"))
        biblio.ajouter_livre(livre)

    while True:
        clear_console()
        afficher_menu()
        choix = input("Entrez votre choix: ")

        if choix == "1":
            afficher_livres(livres_data)

        elif choix == "2":
            data = input_book_data()
            ajouter_livre(livres_data, data["titre"], data["auteur"], data["annee"], data["isbn"])

        elif choix == "3":
            id_livre = input("Entrez l'ID du livre à supprimer : ")
            supprimer_livre(livres_data, id_livre)

        elif choix == "4":
            id_livre = input("Entrez l'ID du livre à modifier : ")
            print("Laissez vide pour ne pas modifier un champ.")
            titre = input("Nouveau titre : ")
            auteur = input("Nouvel auteur : ")
            annee = input("Nouvelle année : ")
            isbn = input("Nouveau ISBN : ")
            modifier_livre(
                livres_data,
                id_livre,
                titre if titre else None,
                auteur if auteur else None,
                annee if annee else None,
                isbn if isbn else None
            )

        elif choix == "5":
            critere = input("Rechercher par (titre/auteur/isbn): ").lower()
            valeur = input("Entrez la valeur de recherche: ")

            if critere == "titre":
                resultats = [recherche_par_titre(valeur)]
            elif critere == "auteur":
                resultats = [rechercher_par_auteur(valeur)]
            elif critere == "isbn":
                resultats = [recherche_par_ISBN(valeur)]
            else:
                print("Critère invalide.")
                continue

            resultats = [r for r in resultats if r]
            if resultats:
                afficher_livres(resultats)
            else:
                print("Aucun résultat trouvé.")

        elif choix == "6":
            cle = input("Trier par (titre/auteur/annee): ").lower()
            methode = input("Méthode de tri (bubble/insertion/merge): ").lower()
            livres_data = trier_livres(livres_data, cle, methode)
            afficher_livres(livres_data)

        elif choix == "7":
            titre = input("Titre du livre à emprunter: ")
            nom = input("Nom de l'emprunteur: ")
            for livre in biblio.livres:
                if livre.titre.lower() == titre.lower():
                    livre.emprunter(nom)
                    break
            else:
                print("Livre non trouvé.")

        elif choix == "8":
            titre = input("Titre du livre à retourner: ")
            for livre in biblio.livres:
                if livre.titre.lower() == titre.lower():
                    livre.retourner()
                    break
            else:
                print("Livre non trouvé.")

        elif choix == "9":
            biblio.lister_livres_empruntes()

        elif choix == "10":
            biblio.lister_livres_disponibles()

        elif choix == "11":
            generate_report([
                {
                    "titre": l.titre,
                    "auteur": l.auteur,
                    "emprunte": l.emprunteur is not None
                } for l in biblio.livres
            ])

        elif choix == "12":
            cle = input("Comparer les tris par quelle clé (titre/auteur/annee): ").lower()
            print("\nComparaison des performances :\n")
            resultats = compare_sorts(livres_data, cle)
            for nom, info in resultats.items():
                print(f"{nom}: {info['temps']} secondes")
            print("\nTri effectué, résultats non modifiés dans la liste.")

        elif choix == "0":
            print("Fermeture de BiblioPy...")
            # Sauvegarde de l’état final des livres
            sauvegarder_livres_json([
                {
                    "titre": l.titre,
                    "auteur": l.auteur,
                    "emprunte": l.emprunteur is not None,
                    "emprunteur": l.emprunteur,
                    "date_emprunt": l.date_emprunt
                } for l in biblio.livres
            ])
            break

        else:
            print("Choix invalide, veuillez réessayer.")

        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
