from .huffman_tree import build_tree, generate_codes
from .frequency_analyzer import calculate_frequencies, create_priority_queue

def compress(input_file, output_file):
    # Calculer les fréquences
    frequencies = calculate_frequencies(input_file)
    priority_queue = create_priority_queue(frequencies)
    
    # Construire l'arbre et les codes
    root = build_tree(priority_queue)
    codes = generate_codes(root) if root else {}
    
    # Préparer les données compressées
    bit_string = ""
    with open(input_file, 'rb') as f:
        while (byte := f.read(1)):
            # byte est de type bytes (longueur 1), donc byte[0] donne l'entier (0–255)
            bit_string += codes[byte[0]]
            
    # Gérer le padding
    padding = (8 - len(bit_string) % 8) % 8
    bit_string += '0' * padding
    
    # Convertir en octets
    data_bytes = bytearray()
    for i in range(0, len(bit_string), 8):
        data_bytes.append(int(bit_string[i:i+8], 2))
        
    # Écrire le fichier compressé
    with open(output_file, 'wb') as f:
        # Écrire l'en-tête : nombre d'entrées de fréquence
        f.write(len(frequencies).to_bytes(2, 'little'))  # 2 octets pour gérer jusqu'à 65535 symboles
        
        for byte_value, freq in frequencies.items():
            f.write(bytes([byte_value]))                  # 1 octet : le caractère
            f.write(freq.to_bytes(8, 'little'))           # 8 octets : la fréquence
        
        # Écrire le padding suivi des données compressées
        f.write(bytes([padding]))                         # 1 octet : padding
        f.write(data_bytes)
