import sys

def chiffrement_cesar(texte, decalage):
    resultat = ""

    for caractere in texte:
        # Chiffrement des lettres minuscules
        if 'a' <= caractere <= 'z':
            resultat += chr((ord(caractere) - ord('a') + decalage) % 26 + ord('a'))

        # Chiffrement des lettres majuscules
        elif 'A' <= caractere <= 'Z':
            resultat += chr((ord(caractere) - ord('A') + decalage) % 26 + ord('A'))

        # Autres caractères (espaces, ponctuation…) inchangés
        else:
            resultat += caractere

    return resultat


def lire_fichier(chemin):
    with open(chemin, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def ecrire_fichier(chemin, contenu):
    with open(chemin, "w", encoding="utf-8", errors="ignore") as f:
        f.write(contenu)


def main():
    # Vérification du nombre d'arguments
    if len(sys.argv) != 3:
        print("Usage : python3 programmeDecalage.py fichier.txt decalage")
        sys.exit(1)

    chemin_fichier = sys.argv[1]
    decalage = int(sys.argv[2])

    # Lecture du fichier
    contenu = lire_fichier(chemin_fichier)

    # Chiffrement
    contenu_chiffre = chiffrement_cesar(contenu, decalage)

    # Réécriture dans le fichier
    ecrire_fichier(chemin_fichier, contenu_chiffre)

    print(f"Fichier '{chemin_fichier}' chiffré avec un décalage de {decalage}.")


if __name__ == "__main__":
    main()