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
| **Chiffrement.py** | Chiffre un message (codé en dur dans le script) avec une clé |
| **Dechiffrement.py** | Déchiffre ce même message avec la même clé |
| **Cassage_Vigenere.py** | Retrouve la clé sans la connaître (Kasiski + analyse fréquentielle) |
| **README.md** | Documentation du dossier |

---

## ▶️ Utilisation

Les scripts sont des démonstrations autonomes : le message et la clé sont définis dans le bloc
`if __name__ == "__main__":` de chaque fichier, à modifier directement pour tester d'autres
valeurs — pas d'argument en ligne de commande.

### 🔸 Chiffrement
```bash
python3 Chiffrement.py
```

### 🔸 Déchiffrement (chiffre le message puis le déchiffre pour vérifier)
```bash
python3 Dechiffrement.py
```

### 🔓 Cassage (clé inconnue)
```bash
python3 Cassage_Vigenere.py
```
Édite `message_clair`/`cle_secrete` en bas du script pour tester avec ton propre texte. Prévois
un texte d'au moins quelques phrases : l'analyse fréquentielle par colonne a besoin d'assez de
lettres pour être fiable, quelques mots ne suffisent pas.

---

## ⚠️ Limites du chiffrement de Vigenère
- Plus robuste que César, mais cassable si la clé est courte
- Vulnérable à l’attaque de Kasiski
- Ne protège pas contre les attaques modernes

---

## 🔗 Liens vers les autres méthodes du projet
- Méthode de César → dossier ```cesar/```
- Méthode XOR → dossier ```xor/```

