Huffman Compressor

Un compresseur de fichiers basé sur l'algorithme de compression de Huffman.

Fonctionnalités

- Analyse des fréquences d'un fichier binaire.
- Construction d’un arbre de Huffman.
- Compression des données avec génération d’un encodage binaire.
- Écriture du fichier compressé incluant un en-tête avec les métadonnées nécessaires à la décompression.

Algorithme

L'algorithme de Huffman compresse les données en attribuant des codes binaires plus courts aux symboles fréquents et des codes plus longs aux symboles rares. Il repose sur un arbre binaire construit à partir des fréquences d'apparition des octets du fichier.

Structure du projet


Utilisation
project/
│
├── compressor.py # Contient la fonction compress()
├── huffman_tree.py # Construction de l’arbre et génération des codes
├── frequency_analyzer.py # Analyse des fréquences et file de priorité
├── decompressor.py # (Optionnel) pour décompresser les fichiers
├── example.txt # Exemple de fichier à compresser
└── README.md # Ce fichier
Compression

python
from compressor import compress

compress("example.txt", "example.huff")

from decompressor import decompress

decompress("example.huff", "example_decompressed.txt")

Ce projet utilise uniquement les modules standards de Python (aucune bibliothèque externe requise).

Python ≥ 3.9 (utilise l'opérateur := de l’instruction while (byte := f.read(1)))
Avant compression
Contenu de example.txt :
"Bonjour bonjour bonjour"
Taille : 24 octets
Après compression
Contenu de example.huff :
Taille : ~12–16 octets (selon la répétition des caractères)
