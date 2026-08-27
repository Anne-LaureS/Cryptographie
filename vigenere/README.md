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

`Cassage_Vigenere.py` sert quand tu as un texte chiffré en Vigenère **sans connaître ni la clé
ni sa longueur** — Kasiski pour deviner la longueur, analyse fréquentielle pour deviner chaque
lettre de la clé.

**Marche à suivre :**

1. Ouvre `Cassage_Vigenere.py`, descends jusqu'au bloc `if __name__ == "__main__":` tout en bas.
2. Remplace `message_clair`/`cle_secrete` par ton propre texte à tester — ou, si tu as déjà un
   texte chiffré réel (pas besoin de le générer toi-même), remplace directement la ligne
   `texte_chiffre = chiffrer_vigenere(...)` par :
   ```python
   texte_chiffre = "ton texte chiffré ici"
   ```
3. Lance :
   ```bash
   python3 Cassage_Vigenere.py
   ```
4. Le script affiche les longueurs de clé candidates (Kasiski), puis devine directement la clé
   pour la plus probable et déchiffre le texte avec.
5. Vérifie que le texte déchiffré est **lisible et cohérent**. Si ce n'est pas le cas, la
   longueur de clé la plus probable était la mauvaise — reprends `candidats[1]`, `candidats[2]`,
   etc. (2ème, 3ème longueur la plus probable) à la place de `candidats[0]` dans l'appel à
   `deviner_cle()`, et relance.

⚠️ Il faut un texte d'au moins quelques phrases pour que ça marche : l'analyse fréquentielle par
colonne a besoin d'assez de lettres pour être fiable, quelques mots ne suffisent pas.

---

## ⚠️ Limites du chiffrement de Vigenère
- Plus robuste que César, mais cassable si la clé est courte
- Vulnérable à l’attaque de Kasiski
- Ne protège pas contre les attaques modernes

---

## 🔗 Liens vers les autres méthodes du projet
- Méthode de César → dossier ```cesar/```
- Méthode XOR → dossier ```xor/```

