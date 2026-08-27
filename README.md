## 🔐 **Chiffrement avec les méthodes XOR, Vigenère et César**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Projet](https://img.shields.io/badge/Projet-P%C3%A9dagogique-orange)
![Status](https://img.shields.io/badge/Status-Actif-brightgreen)

Ce dépôt illustre plusieurs méthodes de **chiffrement symétrique classiques** à des fins **strictement pédagogiques**.
L’objectif est de comprendre les principes fondamentaux du chiffrement avant d’aborder des algorithmes modernes réellement sécurisés.

---

## 🔁 XOR

Chiffrement par **OU exclusif bit à bit** :

* ```message ⊕ clé = chiffré```
* ```chiffré ⊕ clé = message```
La même opération est utilisée pour le chiffrement et le déchiffrement.
Simple, rapide… et **totalement vulnérable** si la clé est courte ou réutilisée.

📁 Voir le dossier : ```xor/```

### 🔓 Casser une clé XOR inconnue (CTF)

`xor/Cassage_XOR.py` — utile quand on récupère un message XOR-é (ex: un flag TryHackMe) sans
connaître la clé, mais en devinant son format (ex: `THM{...}`, `flag{...}`).

**Marche à suivre :**

1. Ouvre `xor/Cassage_XOR.py`, descends jusqu'au bloc `if __name__ == "__main__":` tout en bas.
2. Remplace `hex_recu` par le hex reçu dans ton challenge :
   ```python
   hex_recu = "ton_nouveau_hex_ici"
   ```
3. Remplace `"THM{"` (dans l'appel à `casser_par_texte_connu`) par le début de texte que tu
   devines pour CE challenge (ex: `"flag{"`, `"CTF{"`) :
   ```python
   cle_partielle = bytearray(casser_par_texte_connu(chiffre, "THM{", longueur_cle))
   ```
4. Si tu connais la longueur de la clé, ajuste `longueur_cle = 5` en conséquence (sinon essaie
   plusieurs valeurs, ou utilise directement `casser_cle_repetee_longueur_inconnue(chiffre)` à
   la place des étapes 3/4 si tu n'as ni format de texte connu ni longueur de clé).
5. Lance depuis le dossier `xor/` :
   ```powershell
   python Cassage_XOR.py
   ```
6. Dans la liste de candidats affichée, repère la ligne dont le texte décodé est **lisible et
   cohérent** (les autres candidats donnent du charabia) — le `clé=` associé est la réponse.

**Exemple concret (room TryHackMe W1seGuy)** : le serveur envoie un flag factice XOR-é avec une
clé de 5 caractères alphanumériques aléatoires, en précisant que le vrai flag commence toujours
par `THM{`. Il suffit de changer `hex_recu` à chaque nouvelle connexion — `"THM{"` et
`longueur_cle = 5` restent valables pour toute cette room.

---

## 🔤 Vigenère

Chiffrement par **décalage alphabétique** basé sur une clé répétée :

```(lettre_message + lettre_clé) mod 26```
Le déchiffrement s’effectue par soustraction.
Plus robuste que César sur le papier, mais cassable dès qu’on comprend les longueurs de clé (attaque **Kasiski**).

📁 Voir le dossier : ```vigenere/```
🔓 Casser une clé inconnue : `vigenere/Cassage_Vigenere.py` (Kasiski + analyse fréquentielle —
détail dans le README du dossier).

---

## 🏛️ César

Chiffrement par **décalage fixe de l’alphabet**.
Aucune clé réelle, une sécurité équivalente à un cadenas en plastique.

📁 Voir le dossier : ```cesar/```
🔓 Casser un décalage inconnu : `cesar/Cassage_Cesar.py` (brute force des 26 décalages possibles
— détail dans le README du dossier).

---

## ⚠️ **Attention-Sécurité**
Ces méthodes sont **obsolètes et non sécurisées**.
Elles ne doivent **jamais** être utilisées en production ou pour protéger des données sensibles.

Elles servent uniquement à comprendre les **fondements historiques** du chiffrement symétrique avant de passer à des algorithmes modernes comme **AES, ChaCha20, RSA, ECC**, etc.

