from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth import create_token, get_current_user
from app.db import get_session
from app.models.user import User
from app.schemas.user import LoginRequest, TokenOut, UserOut

router = APIRouter(prefix="/api", tags=["users"])


@router.get("/users", response_model=list[UserOut])
def get_users(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """Récupère la liste de tous les utilisateurs (authentification requise)."""
    users = session.query(User).all()
    return users


@router.post("/login", response_model=TokenOut)
def login(body: LoginRequest, session: Session = Depends(get_session)):
    """Authentifie un utilisateur et retourne un token JWT."""
    user = session.query(User).filter(User.email == body.email).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Email ou mot de passe incorrect")

    token = create_token(user.id)
    return TokenOut(access_token=token, user=UserOut.model_validate(user))
