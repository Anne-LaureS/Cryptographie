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
🔓 Casser une clé inconnue (utile en CTF) : `xor/Cassage_XOR.py` — brute force 1 octet, texte
clair connu, clé de longueur inconnue. Marche à suivre détaillée dans `xor/README.md`.

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

