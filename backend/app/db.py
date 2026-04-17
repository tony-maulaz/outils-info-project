import os

import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.logger import logger

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@db:5432/app_db",
)

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())


def init_db() -> None:
    from app.models.user import Base, User

    logger.info("Suppression et recréation des tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    logger.info("Insertion des données de test...")
    with SessionLocal() as session:
        users = [
            User(
                last_name="Admin",
                first_name="Super",
                email="admin@example.com",
                hashed_password=hash_password("password123"),
            ),
            User(
                last_name="Dupont",
                first_name="Alice",
                email="alice@example.com",
                hashed_password=hash_password("password123"),
            ),
            User(
                last_name="Martin",
                first_name="Bob",
                email="bob@example.com",
                hashed_password=hash_password("password123"),
            ),
            User(
                last_name="Durand",
                first_name="Claire",
                email="claire@example.com",
                hashed_password=hash_password("password123"),
            ),
            User(
                last_name="Bernard",
                first_name="David",
                email="david@example.com",
                hashed_password=hash_password("password123"),
            ),
        ]
        session.add_all(users)
        session.commit()

    logger.info("Base de données initialisée avec succès.")

    # TODO: Ajouter ici l'initialisation de vos autres tables
