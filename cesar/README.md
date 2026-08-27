# 🔐 Méthode de Chiffrement de César  
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Fonctionnel-brightgreen)

Ce dossier contient une implémentation complète du chiffrement de César, un des plus anciens algorithmes de cryptographie par substitution.  
Il repose sur un décalage fixe appliqué à chaque lettre du message.

---

## 🧠 Principe du chiffrement

Le chiffrement de César consiste à décaler chaque lettre de l’alphabet d’un nombre fixe de positions.  
Exemple avec un décalage de **3** :

- A → D  
- B → E  
- C → F  
- …  
- X → A  
- Y → B  
- Z → C  

Ce chiffrement est simple mais illustre les bases de la cryptographie classique.

---

## 📁 Contenu du dossier

| Fichier | Rôle |
|--------|------|
| **ProgrammeDecalage.py** | Chiffre un fichier texte avec un décalage donné (déchiffrement = même script avec un décalage négatif) |
| **Cassage_Cesar.py** | Casse le chiffrement sans connaître le décalage — brute force des 26 possibilités |
| **FichierAChiffrer.txt** | Exemple de fichier texte à chiffrer |
| **README.md** | Documentation du dossier |

---

## ▶️ Utilisation

### Chiffrement d'un fichier
```bash
python3 ProgrammeDecalage.py FichierAChiffrer.txt 3
```
Réécrit le fichier avec son contenu chiffré (décalage de 3 lettres).

### Déchiffrement
Même script, avec le décalage négatif :
```bash
python3 ProgrammeDecalage.py FichierAChiffrer.txt -3
```

### 🔓 Cassage (décalage inconnu)

`Cassage_Cesar.py` sert quand tu as un texte chiffré en César sans connaître le décalage — pas
besoin d'algorithme compliqué, seulement 26 décalages possibles.

**Marche à suivre :**

1. Ouvre `Cassage_Cesar.py`, descends jusqu'au bloc `if __name__ == "__main__":` tout en bas.
2. Remplace `texte_chiffre` par ton propre texte chiffré :
   ```python
   texte_chiffre = "ton texte chiffré ici"
   ```
3. Lance :
   ```bash
   python3 Cassage_Cesar.py
   ```
4. Les 26 décalages possibles s'affichent d'un coup — parcours-les et repère celui qui donne du
   texte **lisible et cohérent**, les 25 autres seront du charabia. Pas de scoring automatique
   nécessaire ici : avec seulement 26 possibilités, l'œil humain repère la bonne immédiatement.

---

## ⚠️ Limites du chiffrement de César
- Très faible sécurité
- Vulnérable à l’analyse fréquentielle
- Seulement 26 clés possibles (pour l’alphabet latin)

---

## 🔗 Liens vers les autres méthodes du projet

- Méthode de Vigenère → dossier ```vigenere/```
- Méthode XOR → dossier ```xor/```

Chaque dossier contient son propre code et sa propre documentation.
