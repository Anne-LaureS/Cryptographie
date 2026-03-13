# 🔐 Chiffrement de César

Ce dossier contient une implémentation complète du chiffrement de César, un des plus anciens algorithmes de cryptographie par substitution.  
Il repose sur un décalage fixe appliqué à chaque lettre du message.

---

## 📌 Principe du chiffrement

Le chiffrement de César consiste à décaler chaque lettre de l’alphabet d’un nombre fixe de positions.  
Exemple avec un décalage de 3 :

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
| **Chiffrement.py** | Script permettant de chiffrer un message avec un décalage donné |
| **Dechiffrement.py** | Script permettant de déchiffrer un message chiffré |
| **ProgrammeDecalage.py** | Programme interactif pour tester différents décalages |
| **FichierAChiffrer.txt** | Exemple de fichier texte à chiffrer |
| **README.md** | Documentation du dossier |

---

## ▶️ Exemple d’utilisation

### Chiffrement
```bash
python3 Chiffrement.py "MESSAGE" 3
```

---

## Déchiffrement

```
python3 Dechiffrement.py "PHHPDJH" 3
```

---

## Limites du chiffrement de César
- Très faible sécurité
- Vulnérable à l’analyse fréquentielle
- Seulement 26 clés possibles (pour l’alphabet latin)

