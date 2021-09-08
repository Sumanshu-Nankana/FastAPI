from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from utils import OAuth2PasswordBearerWithCookie
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from database import get_db
from models import User
from hashing import Hasher
from jose import jwt
from config import settings

oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/login/token")


router = APIRouter()


@router.post("/login/token")
def retrieve_token_for_authenticated_user(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username"
        )
    if not Hasher.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Password"
        )
    data = {"sub": form_data.username}
    jwt_token = jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    response.set_cookie(key="access_token", value=f"Bearer {jwt_token}", httponly=True)
    return {"access_token": jwt_token, "token_type": "bearer"}
