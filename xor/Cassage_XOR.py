"""
Cassage de chiffrement XOR — techniques offensives, à l'opposé de Chiffrer_Fichier.py
et Dechiffrement.py qui supposent une clé déjà connue.

Trois techniques, de la plus simple à la plus générale :
1. Brute force clé à 1 octet (256 possibilités)
2. Attaque en texte clair connu ("crib") : on connaît (ou on devine) le début du
   message en clair, ce qui suffit à déduire les octets de la clé correspondants
3. Clé répétée de longueur inconnue : analyse colonne par colonne

Utile en CTF quand on récupère un message XOR-é sans connaître la clé (ex: TryHackMe
W1seGuy, où le format du flag est connu à l'avance : "THM{...}").
"""

import itertools
import string


def est_imprimable(donnees: bytes) -> bool:
    """Un décodage correct donne du texte ASCII imprimable ; un mauvais donne des
    octets aléatoires en dehors de cette plage. Sert de filtre pour éliminer les
    mauvaises clés sans avoir à les lire une par une."""
    return all(32 <= b < 127 for b in donnees)


def casser_cle_1_octet(chiffre: bytes) -> list[tuple[int, bytes]]:
    """Teste les 256 clés à 1 octet possibles, ne garde que celles qui donnent du
    texte entièrement imprimable. Rapide, mais ne fonctionne que si la vraie clé
    fait bien 1 octet."""
    candidats = []
    for cle in range(256):
        dechiffre = bytes(b ^ cle for b in chiffre)
        if est_imprimable(dechiffre):
            candidats.append((cle, dechiffre))
    return candidats


def casser_par_texte_connu(chiffre: bytes, debut_connu: str, longueur_cle: int) -> bytes:
    """Si on connaît (ou devine, ex: un format de flag "THM{") le début du message
    en clair, on peut en déduire directement les octets de la clé à cette position :
    clé[i] = chiffré[i] XOR clair[i]. Ne donne que les octets de clé couverts par
    debut_connu — complète le reste par brute force si besoin (voir
    casser_cle_repetee_longueur_connue)."""
    cle = bytearray(longueur_cle)
    connu = [False] * longueur_cle
    for i, caractere in enumerate(debut_connu):
        pos = i % longueur_cle
        octet_cle = chiffre[i] ^ ord(caractere)
        if connu[pos] and cle[pos] != octet_cle:
            raise ValueError(
                f"Incohérence à la position {pos} de la clé : le texte connu ne "
                "correspond pas à une clé répétée de cette longueur."
            )
        cle[pos] = octet_cle
        connu[pos] = True
    return bytes(cle)


def completer_cle_par_brute_force(
    chiffre: bytes,
    cle_partielle: bytes,
    positions_inconnues: list[int],
    longueur_cle: int,
    alphabet: str = string.ascii_letters + string.digits,
) -> list[tuple[str, bytes]]:
    """Une fois une partie de la clé déduite par texte connu (casser_par_texte_connu),
    complète les octets restants par brute force — nettement plus rapide que de
    bruteforcer la clé entière, puisqu'on ne bruteforce que ce qu'on ignore encore."""
    candidats = []
    for combo in itertools.product(alphabet, repeat=len(positions_inconnues)):
        cle = bytearray(cle_partielle)
        for pos, caractere in zip(positions_inconnues, combo):
            cle[pos] = ord(caractere)
        dechiffre = bytes(chiffre[i] ^ cle[i % longueur_cle] for i in range(len(chiffre)))
        if est_imprimable(dechiffre):
            candidats.append((cle.decode(), dechiffre))
    return candidats


def casser_cle_repetee_longueur_inconnue(
    chiffre: bytes, longueur_max: int = 12, alphabet: str = string.ascii_letters + string.digits
) -> dict[int, list[bytes]]:
    """Sans aucun texte connu : pour chaque longueur de clé possible, découpe le
    chiffré en colonnes (une colonne = tous les octets chiffrés avec le même octet
    de clé), et ne garde que les octets de clé qui rendent TOUTE la colonne
    imprimable. Beaucoup plus rapide qu'un brute force naïf sur la clé entière,
    car chaque colonne réduit l'espace de recherche indépendamment des autres."""
    resultats = {}
    for longueur_cle in range(1, longueur_max + 1):
        candidats_par_colonne = []
        for position in range(longueur_cle):
            colonne = chiffre[position::longueur_cle]
            survivants = [
                ord(c) for c in alphabet
                if all(32 <= (octet ^ ord(c)) < 127 for octet in colonne)
            ]
            if not survivants:
                candidats_par_colonne = None
                break
            candidats_par_colonne.append(survivants)

        if not candidats_par_colonne:
            continue

        cles_valides = []
        for combo in itertools.product(*candidats_par_colonne):
            cle = bytes(combo)
            dechiffre = bytes(chiffre[i] ^ cle[i % longueur_cle] for i in range(len(chiffre)))
            cles_valides.append(dechiffre)

        if cles_valides:
            resultats[longueur_cle] = cles_valides
    return resultats


if __name__ == "__main__":
    # Reproduction du cas réel rencontré sur TryHackMe (room W1seGuy) : un serveur
    # envoie un texte XOR-é dont on sait qu'il commence par "THM{" (format de flag),
    # avec une clé de 5 caractères alphanumériques générée aléatoirement.
    hex_recu = "05121e1909603b3f0c0d142227230d256e30091a10342151183d162a0a2c232e2a520c23221c1004"
    chiffre = bytes.fromhex(hex_recu)
    longueur_cle = 5

    # Étape 1 : déduire les 4 premiers octets de la clé à partir du "THM{" connu
    cle_partielle = bytearray(casser_par_texte_connu(chiffre, "THM{", longueur_cle))
    print(f"Octets de clé déduits du texte connu : {cle_partielle.decode()}...")

    # Étape 2 : bruteforcer le seul octet restant (position 4)
    candidats = completer_cle_par_brute_force(
        chiffre, bytes(cle_partielle), positions_inconnues=[4], longueur_cle=longueur_cle
    )

    print(f"\n{len(candidats)} clé(s) candidate(s) donnant un texte imprimable :")
    for cle, dechiffre in candidats:
        print(f"  clé={cle!r} -> {dechiffre.decode()!r}")
