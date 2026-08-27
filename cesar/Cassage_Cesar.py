"""
Cassage du chiffrement de César — le plus simple des trois du dépôt à casser :
seulement 26 décalages possibles (l'alphabet latin), donc un brute force complet
est instantané. Contrairement à XOR ou Vigenère, pas besoin de scoring
automatique : on affiche les 26 résultats et l'œil humain repère immédiatement
lequel est du texte lisible.
"""


def dechiffrer_cesar(texte: str, decalage: int) -> str:
    """Déchiffre un texte César avec un décalage donné (opération inverse du
    chiffrement : on retranche le décalage au lieu de l'ajouter)."""
    resultat = ""
    for caractere in texte:
        if 'a' <= caractere <= 'z':
            resultat += chr((ord(caractere) - ord('a') - decalage) % 26 + ord('a'))
        elif 'A' <= caractere <= 'Z':
            resultat += chr((ord(caractere) - ord('A') - decalage) % 26 + ord('A'))
        else:
            resultat += caractere
    return resultat


def casser_cesar(texte_chiffre: str) -> list[tuple[int, str]]:
    """Teste les 26 décalages possibles et retourne tous les résultats —
    à l'utilisateur de repérer celui qui est lisible."""
    return [(decalage, dechiffrer_cesar(texte_chiffre, decalage)) for decalage in range(26)]


if __name__ == "__main__":
    # Exemple : "Bonjour les copains" chiffré avec un décalage de 3, sans
    # connaître ce décalage à l'avance.
    texte_chiffre = "Erqmrxu ohv frsdlqv"

    print(f"Texte chiffré : {texte_chiffre}\n")
    print("Les 26 décalages possibles :")
    for decalage, resultat in casser_cesar(texte_chiffre):
        print(f"  décalage {decalage:>2} : {resultat}")
