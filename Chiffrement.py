def chiffrer_vigenere(message: str, cle: str) -> str:
    """
    Chiffre un message en utilisant le chiffre de Vigenère.

    Args:
        message: Le message en clair à chiffrer.
        cle: La clé de chiffrement.

    Returns:
        Le message chiffré.
    """
    message_chiffre = ""
    index_cle = 0

    # Pour s'assurer que la clé n'est pas vide pour éviter les erreurs
    if not cle:
        return message

    for char_message in message:
        # On ne chiffre que les lettres de l'alphabet (a-z, A-Z)
        if 'a' <= char_message.lower() <= 'z':
            # On récupère le caractère correspondant dans la clé, en la répétant si besoin
            char_cle = cle[index_cle % len(cle)]

            # On détermine si la lettre du message est majuscule ou minuscule
            # pour conserver la casse d'origine.
            base = ord('A') if char_message.isupper() else ord('a')

            # --- Le cœur du chiffrement ---
            # 1. On calcule la position (0-25) de la lettre du message
            offset_message = ord(char_message) - base
            # 2. On calcule la position (0-25) de la lettre de la clé (en la mettant en minuscule)
            offset_cle = ord(char_cle.lower()) - ord('a')

            # 3. On additionne les deux positions et on utilise le modulo 26
            #    pour "boucler" si on dépasse la lettre Z.
            nouveau_offset = (offset_message + offset_cle) % 26

            # 4. On reconvertit le nouvel offset en caractère
            nouveau_char = chr(base + nouveau_offset)
            
            message_chiffre += nouveau_char

            # On incrémente l'index de la clé uniquement pour les lettres chiffrées
            index_cle += 1
        else:
            # Si le caractère n'est pas une lettre (espace, ponctuation...), on l'ajoute tel quel.
            message_chiffre += char_message
            
    return message_chiffre

# --- Programme principal ---
if __name__ == "__main__":
    message_clair = "Bonjour les copains"
    cle = "toto"

    message_chiffre = chiffrer_vigenere(message_clair, cle)

    print(f"Message original : {message_clair}")
    print(f"Clé              : {cle}")
    print(f"Message chiffré  : {message_chiffre}")