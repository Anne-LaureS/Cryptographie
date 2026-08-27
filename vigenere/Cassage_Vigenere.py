"""
Cassage du chiffrement de Vigenère sans connaître la clé — technique classique
en deux temps, plus difficile que le brute force de César (26 clés) puisque la
clé peut être n'importe quelle suite de lettres, de longueur inconnue :

1. Examen de Kasiski : on repère des séquences de 3+ lettres qui se répètent
   dans le texte chiffré. Le hasard veut que ça n'arrive presque jamais sauf si
   la même portion de clé retombe sur la même portion de texte clair — la
   distance entre deux répétitions est alors presque toujours un multiple de la
   longueur de la clé, ce qui permet de la deviner (via le PGCD des distances).

2. Analyse fréquentielle par colonne : une fois la longueur de clé supposée,
   chaque colonne (lettres chiffrées avec la même lettre de clé) est un simple
   décalage de César — on teste les 26 décalages et on garde celui dont la
   distribution de lettres ressemble le plus au français (indice du chi carré).
"""

import math
from collections import Counter

# Fréquences moyennes des lettres en français (%), pour comparer par chi carré.
FREQUENCES_FR = {
    'a': 7.64, 'b': 0.90, 'c': 3.26, 'd': 3.67, 'e': 14.72, 'f': 1.07,
    'g': 0.87, 'h': 0.74, 'i': 7.53, 'j': 0.54, 'k': 0.05, 'l': 5.46,
    'm': 2.97, 'n': 7.10, 'o': 5.38, 'p': 3.02, 'q': 1.36, 'r': 6.55,
    's': 7.95, 't': 7.24, 'u': 6.31, 'v': 1.84, 'w': 0.05, 'x': 0.45,
    'y': 0.30, 'z': 0.13,
}


def _lettres_seulement(texte: str) -> str:
    return "".join(c.lower() for c in texte if c.isalpha())


def trouver_longueurs_cle_candidates(texte_chiffre: str, taille_sequence: int = 3, max_longueur: int = 12) -> list[int]:
    """Étape 1 (Kasiski) : repère les séquences répétées et leurs distances,
    retourne les longueurs de clé candidates triées par vraisemblance
    (celles qui divisent le plus de distances observées en premier)."""
    lettres = _lettres_seulement(texte_chiffre)
    positions = {}
    distances = []

    for i in range(len(lettres) - taille_sequence + 1):
        sequence = lettres[i:i + taille_sequence]
        if sequence in positions:
            distances.append(i - positions[sequence])
        positions[sequence] = i

    if not distances:
        return []

    # Pour chaque longueur candidate, compte combien de distances observées
    # elle divise exactement — plus ce compte est élevé, plus la longueur est
    # probable. On exclut 1 : une longueur de 1 divise TOUTE distance par
    # définition, donc elle gagnerait systématiquement sans rien démontrer
    # (une clé Vigenère d'une seule lettre est de toute façon juste du César).
    scores = {}
    for longueur in range(2, max_longueur + 1):
        scores[longueur] = sum(1 for d in distances if d % longueur == 0)

    return sorted(scores, key=lambda l: scores[l], reverse=True)


def _meilleur_decalage_colonne(colonne: str) -> int:
    """Étape 2 : teste les 26 décalages sur une colonne et retourne celui dont
    la distribution de lettres est la plus proche du français (chi carré le
    plus faible)."""
    meilleur_decalage, meilleur_score = 0, math.inf

    for decalage in range(26):
        dechiffree = "".join(
            chr((ord(c) - ord('a') - decalage) % 26 + ord('a')) for c in colonne
        )
        occurrences = Counter(dechiffree)
        n = len(dechiffree)

        chi_carre = 0.0
        for lettre, freq_attendue in FREQUENCES_FR.items():
            observe = occurrences.get(lettre, 0)
            attendu = freq_attendue / 100 * n
            if attendu > 0:
                chi_carre += (observe - attendu) ** 2 / attendu

        if chi_carre < meilleur_score:
            meilleur_score, meilleur_decalage = chi_carre, decalage

    return meilleur_decalage


def deviner_cle(texte_chiffre: str, longueur_cle: int) -> str:
    """Reconstruit la clé complète : un décalage (donc une lettre de clé) par
    colonne, déduit indépendamment par analyse fréquentielle."""
    lettres = _lettres_seulement(texte_chiffre)
    cle = ""
    for position in range(longueur_cle):
        colonne = lettres[position::longueur_cle]
        decalage = _meilleur_decalage_colonne(colonne)
        cle += chr(ord('a') + decalage)
    return cle


if __name__ == "__main__":
    from Dechiffrement import dechiffrer_vigenere

    # Texte plus long que "Bonjour les copains" : l'analyse fréquentielle a
    # besoin d'assez de lettres par colonne pour être fiable (quelques mots ne
    # suffisent pas à dégager une vraie distribution de fréquences).
    from Chiffrement import chiffrer_vigenere

    message_clair = (
        "Le chiffrement de Vigenere utilise une cle repetee pour decaler "
        "chaque lettre du message de maniere differente selon sa position "
        "dans le texte ce qui rend inefficace une simple analyse frequentielle"
    )
    cle_secrete = "cle"
    texte_chiffre = chiffrer_vigenere(message_clair, cle_secrete)

    print(f"Texte chiffré (clé inconnue en pratique) : {texte_chiffre}\n")

    candidats = trouver_longueurs_cle_candidates(texte_chiffre)
    print(f"Longueurs de clé candidates (Kasiski, par vraisemblance) : {candidats[:5]}")

    longueur_supposee = candidats[0]
    cle_devinee = deviner_cle(texte_chiffre, longueur_supposee)
    print(f"Clé devinée (longueur {longueur_supposee}) : {cle_devinee!r}")

    print(f"\nMessage déchiffré avec la clé devinée :")
    print(dechiffrer_vigenere(texte_chiffre, cle_devinee))
