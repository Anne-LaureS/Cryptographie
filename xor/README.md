# 🔐 Méthode de Chiffrement XOR  
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Fonctionnel-brightgreen)
![Projet](https://img.shields.io/badge/Projet-Pédagogique-orange)

Le chiffrement XOR est une méthode simple mais puissante lorsqu’elle est bien utilisée.  
Il repose sur l’opérateur logique **XOR (OU exclusif)** appliqué entre chaque caractère du message et une clé.

---

## 🧠 Principe du chiffrement XOR

L’opération XOR possède une propriété essentielle :

```
A XOR B = C
C XOR B = A
```

Cela signifie que **la même opération permet de chiffrer et de déchiffrer**.

Exemple simple :

| Caractère | Code | Clé | Résultat |
|-----------|------|-----|----------|
| A | 65 | 42 | 107 |
| 107 XOR 42 | → | 65 (A) |

➡️ **XOR est réversible**, ce qui en fait un mécanisme très utilisé en cryptographie moderne (flux, OTP, masquage, etc.).

---

## 📁 Contenu du dossier

| Fichier | Description |
|--------|-------------|
| **xor.py** *(ou nom équivalent)* | Script principal de chiffrement/déchiffrement XOR |
| **README.md** | Documentation du dossier |
| **fichiers d’exemple** | Selon ton projet (texte à chiffrer, sortie, etc.) |

> Si les noms exacts diffèrent, tu peux les ajuster — la structure reste la même.

---

## ▶️ Utilisation

### 🔸 Chiffrement
```bash
python3 xor.py --input monfichier.txt --key 42 --output fichier_chiffre.txt
```

### 🔸 Déchiffrement
```bash
python3 xor.py --input fichier_chiffre.txt --key 42 --output fichier_dechiffre.txt
```

### 🔸 Propriété importante
Le même programme sert aux deux opérations.
Il suffit de réutiliser la même clé.

---

## ⚠️ Limites du chiffrement XOR
- Sécurisé uniquement si la clé est aléatoire, aussi longue que le message et jamais réutilisée (One‑Time Pad).
- Avec une clé courte ou répétée → facilement cassable.
- Sensible aux attaques par analyse statistique si mal utilisé.

---

## 🔗 Liens vers les autres méthodes du projet
- Méthode de César → dossier ```cesar/```
- Méthode de Vigenère → dossier ```vigenere/```
  
