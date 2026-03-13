## 🔐 **Chiffrement avec les méthodes XOR, Vigenère et César**

Ce dépôt illustre plusieurs méthodes de **chiffrement symétrique classiques** à des fins **strictement pédagogiques**.
L’objectif est de comprendre les principes fondamentaux du chiffrement avant d’aborder des algorithmes modernes réellement sécurisés.

---

## 🔁 XOR

Chiffrement par **OU exclusif bit à bit** :

* `message ⊕ clé = chiffré`
* `chiffré ⊕ clé = message`
  La même opération est utilisée pour le chiffrement et le déchiffrement.
  Simple, rapide… et totalement vulnérable si la clé est courte ou réutilisée (bonjour l’analyse fréquentielle).

---

## 🔤 Vigenère

Chiffrement par **décalage alphabétique** basé sur une clé répétée :

* `(lettre_message + lettre_clé) mod 26`
  Le déchiffrement s’effectue par soustraction.
  Plus robuste que César sur le papier, mais cassable dès qu’on comprend les longueurs de clé (merci Kasiski).

---

## 🏛️ César

Chiffrement par **décalage fixe de l’alphabet**.
Aucune clé réelle, une sécurité équivalente à un cadenas en plastique.

--- 

## ⚠️ **Attention**
Ces méthodes sont **obsolètes et non sécurisées**.
Elles ne doivent **jamais** être utilisées en production ou pour protéger des données sensibles.
Elles servent uniquement à **comprendre les bases** du chiffrement symétrique avant de passer à AES, RSA & co.

