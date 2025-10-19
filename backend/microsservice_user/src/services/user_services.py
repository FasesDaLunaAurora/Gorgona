from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.user_models import UsuarioModel
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES= os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
TESTE= os.getenv("TESTE")


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UsuarioService:

    @staticmethod
    def criar_usuario(sessao: Session, nome: str, email: str, senha: str, ativo: bool = True, admin: bool = False):
        print(f"Variável TESTE em user_services.py: {TESTE}")
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = UsuarioModel(nome=nome, email=email, senha=senha_criptografada, ativo=ativo, admin=admin)
        sessao.add(novo_usuario)
        sessao.commit()
        sessao.refresh(novo_usuario)
        return novo_usuario
    
    @staticmethod
    def buscar_usuario_email(email: str, sessao: Session):
        usuario = sessao.query(UsuarioModel).filter(UsuarioModel.email == email).first()
        if not usuario:
            return False
        return usuario
    
    @staticmethod
    def autenticar_usuario(email: str, senha: str, sessao: Session):
        usuario = sessao.query(UsuarioModel).filter(UsuarioModel.email == email).first()
        if not usuario:
            return False
        elif not bcrypt_context.verify(senha, usuario.senha):
            return False
        return usuario
    
class LoginService:

    @staticmethod
    def gerar_token(usuario_id: int, duracao = timedelta(minutes= int(ACCESS_TOKEN_EXPIRE_MINUTES))):
        data_expiracao = datetime.now(timezone.utc) + duracao
        informacoes = {
            "sub": str(usuario_id),
            "exp": data_expiracao
        }
        token_codificado = jwt.encode(informacoes, SECRET_KEY, algorithm=ALGORITHM)
        return token_codificado
    
    
