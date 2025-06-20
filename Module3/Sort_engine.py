import time
import copy

def bubble_sort(livres, key):
    n = len(livres)
    for i in range(n):
        for j in range(0, n - i - 1):
            if livres[j][key] > livres[j + 1][key]:
                livres[j], livres[j + 1] = livres[j + 1], livres[j]
    return livres

def insertion_sort(livres, key):
    for i in range(1, len(livres)):
        current = livres[i]
        j = i - 1
        while j >= 0 and livres[j][key] > current[key]:
            livres[j + 1] = livres[j]
            j -= 1
        livres[j + 1] = current
    return livres

def merge_sort(livres, key):
    if len(livres) <= 1:
        return livres
    mid = len(livres) // 2
    left = merge_sort(livres[:mid], key)
    right = merge_sort(livres[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def compare_sorts(livres, key):
    algos = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
    }
    results = {}
    for name, func in algos.items():
        copied = copy.deepcopy(livres)
        start = time.time()
        sorted_list = func(copied, key)
        end = time.time()
        results[name] = {
            "temps": round(end - start, 6),
            "résultat": sorted_list
        }
    return results

def trier_livres(livres, key, methode="bubble"):
    if methode == "bubble":
        return bubble_sort(livres, key)
    elif methode == "insertion":
        return insertion_sort(livres, key)
    elif methode == "merge":
        return merge_sort(livres, key)
    else:
        print("Méthode inconnue. Tri bubble utilisé par défaut.")
        return bubble_sort(livres, key)
