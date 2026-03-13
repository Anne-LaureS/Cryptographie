# 🔐 Méthode de Chiffrement de Vigenère  
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Fonctionnel-brightgreen)
![Projet](https://img.shields.io/badge/Projet-Pédagogique-orange)

Le chiffrement de Vigenère est une amélioration du chiffrement de César.  
Il utilise une **clé composée de plusieurs lettres**, ce qui permet d’appliquer plusieurs décalages successifs et rend l’analyse fréquentielle beaucoup plus difficile.

---

## 🧠 Principe du chiffrement

Le chiffrement de Vigenère repose sur une **clé** (ex : `CLE`) appliquée en boucle sur le message.

Chaque lettre de la clé correspond à un décalage :

| Lettre clé | Décalage |
|------------|----------|
| A | +0 |
| B | +1 |
| C | +2 |
| … | … |
| Z | +25 |

Exemple :  
Message : `BONJOUR`  
Clé : `CLE` → répétée : `CLECLEC`

Chaque lettre du message est décalée selon la lettre correspondante de la clé.

---

## 📁 Contenu du dossier

| Fichier | Description |
|--------|-------------|
| **Chiffrer_Fichier.py** | Chiffre un fichier texte avec une clé |
| **Dechiffrement.py** | Déchiffre un texte chiffré avec la même clé |
| **monfichier.txt** | Exemple de fichier à chiffrer |
| **README.md** | Documentation du dossier |

---

## ▶️ Utilisation

### 🔸 Chiffrement d’un fichier
```bash
python3 Chiffrer_Fichier.py monfichier.txt CLE
```

### 🔸 Déchiffrement d’un fichier
```bash
python3 Dechiffrement.py fichier_chiffre.txt CLE
```

---

## ⚠️ Limites du chiffrement de Vigenère
- Plus robuste que César, mais cassable si la clé est courte
- Vulnérable à l’attaque de Kasiski
- Ne protège pas contre les attaques modernes

---

## 🔗 Liens vers les autres méthodes du projet
- Méthode de César → dossier ```cesar/```
- Méthode XOR → dossier ```xor/```

