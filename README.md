## 🔐 **Chiffrement avec les méthodes XOR, Vigenère et César**

https://img.shields.io/badge/Python-3.x-blue?logo=python  
https://img.shields.io/badge/Projet-P%C3%A9dagogique-orange  
https://img.shields.io/badge/Status-Actif-brightgreen

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

---

## 🔤 Vigenère

Chiffrement par **décalage alphabétique** basé sur une clé répétée :

```(lettre_message + lettre_clé) mod 26```
Le déchiffrement s’effectue par soustraction.
Plus robuste que César sur le papier, mais cassable dès qu’on comprend les longueurs de clé (attaque **Kasiski**).

📁 Voir le dossier : ```vigenere/```

---

## 🏛️ César

Chiffrement par **décalage fixe de l’alphabet**.
Aucune clé réelle, une sécurité équivalente à un cadenas en plastique.

📁 Voir le dossier : ```cesar/```

---

## ⚠️ **Attention-Sécurité**
Ces méthodes sont **obsolètes et non sécurisées**.
Elles ne doivent **jamais** être utilisées en production ou pour protéger des données sensibles.

Elles servent uniquement à comprendre les **fondements historiques** du chiffrement symétrique avant de passer à des algorithmes modernes comme **AES, ChaCha20, RSA, ECC**, etc.

