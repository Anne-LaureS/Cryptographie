def dechiffrer_vigenere(message: str, cle: str) -> str:
    """
    Déchiffre un message chiffré avec le chiffre de Vigenère.

    Args:
        message: Le message chiffré à traiter.
        cle: La clé de chiffrement utilisée (même clé que pour chiffrer).

    Returns:
        Le message déchiffré.
    """
    message_dechiffre = ""
    index_cle = 0

    if not cle:
        return message

    for char_message in message:
        # On ne déchiffre que les lettres de l'alphabet (a-z, A-Z)
        if 'a' <= char_message.lower() <= 'z':
            char_cle = cle[index_cle % len(cle)]

            base = ord('A') if char_message.isupper() else ord('a')

            offset_message = ord(char_message) - base
            offset_cle = ord(char_cle.lower()) - ord('a')

            # Déchiffrement = opération inverse du chiffrement : on soustrait
            # le décalage de la clé au lieu de l'ajouter.
            nouveau_offset = (offset_message - offset_cle) % 26
            nouveau_char = chr(base + nouveau_offset)

            message_dechiffre += nouveau_char
            index_cle += 1
        else:
            message_dechiffre += char_message

    return message_dechiffre


if __name__ == "__main__":
    from Chiffrement import chiffrer_vigenere

    message_clair = "Bonjour les copains"
    cle = "toto"

    message_chiffre = chiffrer_vigenere(message_clair, cle)
    message_dechiffre = dechiffrer_vigenere(message_chiffre, cle)

    print(f"Message original : {message_clair}")
    print(f"Clé              : {cle}")
    print(f"Message chiffré  : {message_chiffre}")
    print(f"Message déchiffré: {message_dechiffre}")
