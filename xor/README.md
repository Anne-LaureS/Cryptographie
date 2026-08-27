# 🔐 Méthode de Chiffrement XOR
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Fonctionnel-brightgreen)
![Projet](https://img.shields.io/badge/Projet-Pédagogique-orange)

Le chiffrement XOR est une méthode simple mais puissante lorsqu'elle est bien utilisée.
Il repose sur l'opérateur logique **XOR (OU exclusif)** appliqué entre chaque caractère du message et une clé.

---

## 🧠 Principe du chiffrement XOR

L'opération XOR possède une propriété essentielle :

```
A XOR B = C
C XOR B = A
```

Cela signifie que **la même opération permet de chiffrer et de déchiffrer**.

➡️ **XOR est réversible**, ce qui en fait un mécanisme très utilisé en cryptographie moderne (flux, OTP, masquage, etc.).

---

## 📁 Contenu du dossier

| Fichier | Description |
|--------|-------------|
| **Chiffrer_Fichier.py** | Chiffre `monfichier.txt` avec la clé codée en dur (`cleToto = "toto"`), écrase le fichier avec le résultat |
| **Dechiffrement.py** | Démonstration chiffrement + déchiffrement d'un message codé en dur (clé identique aux deux opérations) |
| **Cassage_XOR.py** | Retrouve une clé XOR inconnue — brute force 1 octet, texte clair connu, clé de longueur inconnue |
| **monfichier.txt** | Exemple de fichier à chiffrer |
| **README.md** | Documentation du dossier |

---

## ▶️ Utilisation

### 🔸 Chiffrement d'un fichier
```bash
python3 Chiffrer_Fichier.py
```
Chiffre `monfichier.txt` avec la clé `toto` et **écrase le fichier** avec le résultat chiffré —
pas de fichier de sortie séparé. Pour revenir en arrière, relance le même script une seconde
fois : XOR est symétrique, chiffrer deux fois avec la même clé redonne l'original.

### 🔸 Démo chiffrement/déchiffrement
```bash
python3 Dechiffrement.py
```
Message et clé codés en dur dans le script (`if __name__ == "__main__":`) — à modifier
directement pour tester d'autres valeurs.

### 🔓 Cassage (clé inconnue)

`Cassage_XOR.py` sert quand tu récupères un message XOR-é (ex: un flag TryHackMe) **sans**
connaître la clé, mais en devinant son format (ex: `THM{...}`, `flag{...}`).

**Marche à suivre :**

1. Ouvre `Cassage_XOR.py`, descends jusqu'au bloc `if __name__ == "__main__":` tout en bas.
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
5. Lance :
   ```bash
   python3 Cassage_XOR.py
   ```
6. Dans la liste de candidats affichée, repère la ligne dont le texte décodé est **lisible et
   cohérent** (les autres candidats donnent du charabia) — le `clé=` associé est la réponse.

**Exemple concret (room TryHackMe W1seGuy)** : le serveur envoie un flag factice XOR-é avec une
clé de 5 caractères alphanumériques aléatoires, en précisant que le vrai flag commence toujours
par `THM{`. Il suffit de changer `hex_recu` à chaque nouvelle connexion — `"THM{"` et
`longueur_cle = 5` restent valables pour toute cette room.

---

## ⚠️ Limites du chiffrement XOR
- Sécurisé uniquement si la clé est aléatoire, aussi longue que le message et jamais réutilisée (One‑Time Pad).
- Avec une clé courte ou répétée → facilement cassable (voir `Cassage_XOR.py` ci-dessus).
- Sensible aux attaques par analyse statistique si mal utilisé.

---

## 🔗 Liens vers les autres méthodes du projet
- Méthode de César → dossier ```cesar/```
- Méthode de Vigenère → dossier ```vigenere/```
