def chiffrer_vigenere(message: str, cle: str) -> str:
    message_chiffre = ""
    index_cle = 0
def chiffrement_dechiffrement_xor(message: str, cle: str) -> str:
    """
    Chiffre ou déchiffre un message en utilisant un chiffrement XOR.
    L'opération est symétrique : appliquer la fonction une deuxième fois
    avec la même clé redonne le message original.

    if not cle:
        return message
    Args:
        message: Le message à traiter (clair ou chiffré).
        cle: La clé de chiffrement/déchiffrement.

    for char_message in message:
        if 'a' <= char_message.lower() <= 'z':
            char_cle = cle[index_cle % len(cle)]
            base = ord('A') if char_message.isupper() else ord('a')

            offset_message = ord(char_message) - base
            offset_cle = ord(char_cle.lower()) - ord('a')

            nouveau_offset = (offset_message + offset_cle) % 26
            nouveau_char = chr(base + nouveau_offset)

            message_chiffre += nouveau_char
            index_cle += 1
        else:
            message_chiffre += char_message

    return message_chiffre


def dechiffrer_vigenere(message: str, cle: str) -> str:
    message_dechiffre = ""
    index_cle = 0

    Returns:
        Le message traité (chiffré ou déchiffré).
    """
    if not cle:
        return message

    for char_message in message:
        if 'a' <= char_message.lower() <= 'z':
            char_cle = cle[index_cle % len(cle)]
            base = ord('A') if char_message.isupper() else ord('a')
    # On parcourt chaque caractère du message et on applique l'opération XOR
    # avec le caractère correspondant de la clé (répétée si nécessaire).
    # La conversion ord() / chr() permet de travailler sur les valeurs numériques des caractères.
    return "".join(chr(ord(char_message) ^ ord(cle[i % len(cle)])) for i, char_message in enumerate(message))

            offset_message = ord(char_message) - base
            offset_cle = ord(char_cle.lower()) - ord('a')

            nouveau_offset = (offset_message - offset_cle) % 26
            nouveau_char = chr(base + nouveau_offset)

            message_dechiffre += nouveau_char
            index_cle += 1
        else:
            message_dechiffre += char_message

    return message_dechiffre


if __name__ == "__main__":
    message_clair = "Bonjour les copains"
    cle = "toto"

    message_chiffre = chiffrer_vigenere(message_clair, cle)
    message_dechiffre = dechiffrer_vigenere(message_chiffre, cle)
    # La même fonction est utilisée pour chiffrer...
    message_chiffre = chiffrement_dechiffrement_xor(message_clair, cle)
    # ...et pour déchiffrer.
    message_dechiffre = chiffrement_dechiffrement_xor(message_chiffre, cle)

    print(f"Message original : {message_clair}")
    print(f"Clé              : {cle}")
    print(f"Message chiffré  : {message_chiffre}")
    print(f"Message déchiffré: {message_dechiffre}")