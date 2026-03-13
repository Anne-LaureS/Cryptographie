cleToto = "toto"

def chiffrement_xor(message, cle):
    message_chiffre = ""
    for i in range(len(message)):
        message_chiffre += chr(ord(message[i]) ^ ord(cle[i % len(cle)]))
    return message_chiffre


def lire_fichier(chemin):
    with open(chemin, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def ecrire_fichier(chemin, contenu):
    with open(chemin, "w", encoding="utf-8", errors="ignore") as f:
        f.write(contenu)


def chiffrer_fichier(chemin, cle):
    contenu = lire_fichier(chemin)
    contenu_chiffre = chiffrement_xor(contenu, cle)
    ecrire_fichier(chemin, contenu_chiffre)
    print("Fichier chiffré et réécrit avec succès.")


# Expérimentation
chemin_fichier = "monFichier.txt"


chiffrer_fichier(chemin_fichier, cleToto)
