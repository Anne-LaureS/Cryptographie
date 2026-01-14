def chiffrement_dechiffrement_xor(message: str, cle: str) -> str:
    """
    Chiffre ou déchiffre un message en utilisant un chiffrement XOR.
    L'opération est symétrique : appliquer la fonction une deuxième fois
    avec la même clé redonne le message original.

    Args:
        message: Le message à traiter (clair ou chiffré).
        cle: La clé de chiffrement/déchiffrement.

    Returns:
        Le message traité (chiffré ou déchiffré).
    """
    if not cle:
        return message

    # On parcourt chaque caractère du message et on applique l'opération XOR
    # avec le caractère correspondant de la clé (répétée si nécessaire).
    # La conversion ord() / chr() permet de travailler sur les valeurs numériques des caractères.
    return "".join(chr(ord(char_message) ^ ord(cle[i % len(cle)])) for i, char_message in enumerate(message))


if __name__ == "__main__":
    message_clair = "Bonjour les copains"
    cle = "toto"

    # La même fonction est utilisée pour chiffrer...
    message_chiffre = chiffrement_dechiffrement_xor(message_clair, cle)
    # ...et pour déchiffrer.
    message_dechiffre = chiffrement_dechiffrement_xor(message_chiffre, cle)

    print(f"Message original : {message_clair}")
    print(f"Clé              : {cle}")
    print(f"Message chiffré  : {message_chiffre}")
    print(f"Message déchiffré: {message_dechiffre}")