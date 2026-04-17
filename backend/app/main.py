import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.users import router as users_router
from app.logger import logger

APP_ENV = os.getenv("APP_ENV", "dev")
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:5173")
INIT_DB = os.getenv("INIT_DB", "false").lower() == "true"

app = FastAPI(
    title="Project Base API",
    description="Template de projet - cours WEB HEIG-VD",
    version="0.1.0",
)

# CORS
origins = [o.strip() for o in CORS_ORIGINS.split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    if INIT_DB:
        logger.info("INIT_DB=true → initialisation de la base de données...")
        from app.db import init_db
        init_db()
    else:
        # En prod, on crée juste les tables si elles n'existent pas
        from app.db import engine
        from app.models.user import Base
        Base.metadata.create_all(bind=engine)


@app.get("/api/health")
def health():
    """Route de santé pour vérifier que l'API tourne."""
    return {"status": "ok", "env": APP_ENV}


# Inclure les routes
app.include_router(users_router)

# TODO: Inclure vos autres routers ici
# Exemple: app.include_router(items_router)
