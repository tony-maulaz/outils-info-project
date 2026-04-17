# Cahier des charges — Projet WEB

## 1. Contexte et objectif

Le projet consiste à développer une **application web complète** en utilisant les technologies vues en cours :

- **Base de données** : PostgreSQL
- **Backend** : Python avec FastAPI et SQLAlchemy (ORM)
- **Frontend** : Vue.js 3

Le projet est **libre** : les groupes choisissent eux-mêmes le sujet de leur application.

---

## 2. Groupes et dates

| Groupe | Membres | Date de présentation |
|--------|---------|----------------------|
| 1      |         | XXX                  |
| 2      |         | XXX                  |
| 3      |         | XXX                  |

---

## 3. Contraintes techniques

### 3.1 Base de données

- Au moins **6 tables** dont **une table de jointure** (many-to-many)
- Chaque table doit contenir **au moins 20 entrées** de données (fake data)
- Obligatoirement une table **`user`** avec au minimum un utilisateur `admin` et un utilisateur normal
- Les mots de passe des utilisateurs doivent être **hashés** (ex: bcrypt)
- Le mot de passe ne doit **jamais** être renvoyé par l'API
- La base de données doit être protégée par les **contraintes de base** : `NOT NULL`, `UNIQUE`, `FOREIGN KEY`, longueurs maximales (`VARCHAR`)

### 3.2 Backend (FastAPI + SQLAlchemy)

- Les requêtes SQL doivent être **minimisées** : ne charger que les données nécessaires (pas de `SELECT *` inutile, pas de relations chargées si elles ne sont pas utilisées dans la réponse)


L'API doit exposer **au minimum** les routes suivantes :

| Méthode | Route | Description |
|---------|-------|-------------|
| `GET`   | `/api/health` | Vérifier que l'API tourne |
| `GET`   | `/api/users` | Récupérer tous les utilisateurs |
| `GET`   | `/api/users/{id}` | Récupérer un utilisateur |
| `POST`  | `/api/login` | Authentifier un utilisateur |
| `GET`   | `/api/me` | Retourner l'utilisateur connecté |
| `GET`   | `/api/<ressource>` | Liste d'une ressource |
| `GET`   | `/api/<ressource>/{id}` | Détail d'une ressource (avec jointure) |
| `POST`  | `/api/<ressource>` | Créer un élément |
| `POST`  | `/api/<ressource>` | Créer un élément (avec table de jointure) |
| `PUT`   | `/api/<ressource>/{id}` | Modifier un élément |
| `DELETE`| `/api/<ressource>/{id}` | Supprimer un élément (avec table de jointure) |
| `DELETE`| `/api/<ressource>/{id}` | Supprimer un élément |


### 3.3 Frontend (Vue.js 3)

- **Page de login** : formulaire simple (email + mot de passe)
- Après connexion, afficher le **nom de l'utilisateur** connecté sur la page d'accueil
- Le **rôle** de l'utilisateur doit être visible d'une façon ou d'une autre (texte, badge coloré, icône, etc.)
- Les données du formulaire doivent être **validées côté frontend**
- Un **visuel clair** doit indiquer les erreurs de saisie ou **les erreurs retournées par le backend** (ex: 404, 500, erreur métier...)
- Utiliser **Vue Router** avec navigation guard (`router.beforeEach`) pour protéger les routes
- Utiliser **Pinia** pour la gestion de l'état (utilisateur connecté, etc.)
- L'application doit comporter **plusieurs pages** (vues distinctes) et naviguer entre elles via Vue Router
- Chaque page doit avoir un **titre pertinent** (`<title>` de l'onglet navigateur)
- Une **favicon** personnalisée doit être définie (pas l'icône par défaut du navigateur)

### 3.4 Infrastructure

- **Docker Compose** avec deux environnements : `dev` et `prod`
- Environnement `dev` : hot-reload backend et frontend, init DB automatique
- Environnement `prod` : build optimisé, pas d'init DB automatique
- Un **Makefile** pour démarrer/arrêter les environnements
- Fichiers `.env.dev` et `.env.prod` pour les variables d'environnement

---

## 4. Démarrage du projet

### Environnement de développement

```bash
# Démarrer (hot-reload + init DB automatique)
make dev-up

# Arrêter et supprimer les volumes
make dev-down

# Voir les logs
make dev-logs

# Réinitialiser la base de données manuellement
make dev-db
```

**URLs :**
- Frontend : http://localhost:5173
- Backend / API docs : http://localhost:8000/docs

### Environnement de production

```bash
make prod-up
make prod-down
make prod-logs
```

---

## 5. Structure du projet

```
project-base/
├── Makefile
├── compose.yml            # Base commune (DB)
├── compose.dev.yml        # Surcharge dev (hot-reload)
├── compose.prod.yml       # Surcharge prod
├── .env.dev               # Variables d'env dev (non committé)
├── .env.dev.example       # Template dev
├── .env.prod              # Variables d'env prod (non committé)
├── .env.prod.example      # Template prod
├── backend/
│   ├── Dockerfile
│   ├── pyproject.toml     # Dépendances Python (uv)
│   └── app/
│       ├── main.py        # Point d'entrée FastAPI
│       ├── db.py          # Engine, session, init_db()
│       ├── auth.py        # JWT : create_token(), get_current_user()
│       ├── logger.py
│       ├── models/
│       │   └── user.py    # Modèle SQLAlchemy User (base à compléter)
│       ├── schemas/
│       │   └── user.py    # Schémas Pydantic (UserOut, LoginRequest, TokenOut)
│       └── api/
│           └── users.py   # Routes /api/users, /api/login
└── frontend/
    ├── Dockerfile          # Build prod (nginx)
    ├── nginx.conf
    ├── package.json
    ├── vite.config.js
    └── src/
        ├── main.js
        ├── api.js          # Instance axios centralisée + interceptor JWT
        ├── App.vue
        ├── assets/
        │   └── main.css   # Styles globaux partagés (card, btn, form, alert...)
        ├── router/
        │   └── index.js   # Routes + beforeEach guard (à compléter)
        ├── stores/
        │   └── app.js     # Store Pinia (currentUser, token)
        └── views/
            ├── HomeView.vue
            └── LoginView.vue
```

---

## 6. Comptes de test (dev)

| Email | Mot de passe |
|-------|-------------|
| admin@example.com | password123 |
| alice@example.com | password123 |
| bob@example.com | password123 |
| claire@example.com | password123 |
| david@example.com | password123 |
