from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session, sessionmaker
from src.models.user_models import UsuarioModel
from src.database import pegar_sessao
from jose import JWTError, jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_schema = OAuth2PasswordBearer(tokenUrl="user/login_doc")

def verificar_token(token: str = Depends(oauth2_schema), sessao: Session = Depends(pegar_sessao)):
    try:
        informacoes = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id = int(informacoes.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    usuario = sessao.query(UsuarioModel).filter(UsuarioModel.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Acesso negado")
    return usuario
    