# 🤖 Mathik

![Logo Mathik](./assets/logo_mathik-850-200.png)

---
## Contexte

Mathik est un robot Discord qui traduit les notions mathématiques du BTS SIO en algorithme Python. Ce projet est développé par Louis MEDO, un étudiant en BTS SIO autodidacte et passionné par l'informatique. Avec ce projet, son objectif est de s'assurer d'une bonne compréhension des concepts mathématiques ainsi que de la capacité à les utiliser concrètement.

---
## Organisation du dépôt

````plaintext
bts-sio_mathik/
├── assets/          # Ressources graphiques (logo, images)
├── cogs/            # Modules Discord (commandes et fonctionnalités du bot)
├── mathik/          # Environnement virtuel Python
├── main.py          # Point d'entrée du bot Discord
├── requirements.txt # Dépendances Python du projet
└── readme.md        # Documentation du projet
````

**Structure :**

- `assets/` : Contient les fichiers graphiques et ressources visuelles
- `cogs/` : Modules de commandes Discord organisés par thématique (arithmétique, etc.)
- `mathik/` : Environnement virtuel Python avec toutes les dépendances installées

---
## Utiliser le dépôt

1. **Clonner le dépôt sur votre ordinateur.**
````
git clone https://github.com/FireToak/bts-sio_mathik.git
````

2. **Ouvrir le dossier du projet.**
````
cd bts-sio_mathik
````

3. **Création de l'environnement virtuelle python.**
```
python -m venv mathik
```

4. **Activation de l'environnement virtuelle.**

*Windows*
```
.\mathik\Scripts\Activate
```

*MacOS & Linux*
```
source mathik/bin/activate
```

5. **Téléchargement des librairies du projet.**
```
pip install -r requirements.txt
```

---
## Auteur

**Louis MEDO** | [Linkedin](https://www.linkedin.com/in/louismedo/) | [Portfolio](https://louis.loutik.fr/) | [GitHub](https://github.com/FireToak)