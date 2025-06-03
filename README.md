# Statistiques de Planification (FastAPI + React)

Ce projet permet de suivre les heures planifiées et effectuées via Rentman, avec visualisations, alertes et gestion des paramètres de majoration.

---

## 📦 Contenu

- `stat-planning-api/` → Backend FastAPI (connexion Rentman, stats, quotas, alertes)
- `stat-planning-frontend/` → Interface React (tableau de bord avec graphiques, filtres, auth)

---

## 🚀 Déploiement Render + GitHub

### 1. Backend (API FastAPI)

#### a. Upload sur GitHub :
```bash
cd stat-planning-api
git init
git remote add origin https://github.com/votre-utilisateur/stat-planning-api.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

#### b. Déploiement Render :
1. Aller sur https://render.com
2. Créer un nouveau **Web Service**
3. Connecter le repo GitHub
4. Ajouter la variable d’environnement `RENTMAN_TOKEN`
5. Le fichier `render.yaml` s’occupe du reste (build + lancement)

---

### 2. Frontend (React)

#### a. Upload GitHub :
```bash
cd stat-planning-frontend
git init
git remote add origin https://github.com/votre-utilisateur/stat-planning-frontend.git
git add .
git commit -m "Frontend init"
git push -u origin main
```

#### b. Déploiement Render OU Vercel :
- Render : même méthode que pour le backend
- Vercel : https://vercel.com/import → connecter GitHub → build automatique

---

## 🔑 Identifiants de connexion (frontend)

- Login : n'importe quel identifiant
- Mot de passe : `admin123`

---

## 🛠️ Lancement local (dev)

### Backend :
```bash
cd stat-planning-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend :
```bash
cd stat-planning-frontend
npm install
npm run dev
```

---

## ✅ Routes principales de l’API :

| Route | Description |
|-------|-------------|
| `/membres` | Liste des membres Rentman |
| `/heures/planifiees` | Heures planifiées enrichies |
| `/heures/effectuees` | Heures réellement effectuées |
| `/stats` | Statistiques par mois et employé |
| `/alertes` | Alertes dépassement quota |
| `/parametres` | Gestion des règles de majoration |

---