from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session

from app.db import get_session
from app.models.user import User
from app.schemas.user import LoginRequest, UserOut

router = APIRouter(prefix="/api", tags=["users"])


@router.get("/users", response_model=list[UserOut])
def get_users(session: Session = Depends(get_session)):
    """Récupère la liste de tous les utilisateurs."""
    users = session.query(User).all()
    return users


@router.post("/login", response_model=UserOut)
def login(body: LoginRequest, session: Session = Depends(get_session)):
    """Authentifie un utilisateur et retourne ses informations."""
    user = session.query(User).filter(User.email == body.email).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Email ou mot de passe incorrect")
    return user
