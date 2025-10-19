from sqlalchemy.orm import Session
from src.models.user_models import UsuarioModel
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES= os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UsuarioService:

    @staticmethod
    def criar_usuario(sessao: Session, nome: str, email: str, senha: str, ativo: bool = True, admin: bool = False):
        
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = UsuarioModel(nome=nome, email=email, senha=senha_criptografada, ativo=ativo, admin=admin)
        sessao.add(novo_usuario)
        sessao.commit()
        sessao.refresh(novo_usuario)
        return novo_usuario
    
    @staticmethod
    def buscar_usuario_email(sessao: Session, email: str):
        usuario = sessao.query(UsuarioModel).filter(UsuarioModel.email == email).first()
        if not usuario:
            return False
        return usuario
    
    @staticmethod
    def autenticar_usuario(sessao: Session, email: str, senha: str):
        usuario = sessao.query(UsuarioModel).filter(UsuarioModel.email == email).first()
        if not usuario:
            return False
        elif not bcrypt_context.verify(senha, usuario.senha):
            return False
        return usuario
    
    @staticmethod
    def gerar_token(user_id: int, duracao = timedelta(minutes= int(ACCESS_TOKEN_EXPIRE_MINUTES))):
        data_expiracao = datetime.now(timezone.utc) + duracao
        jwt_codificado = {
            "sub": str(user_id),
            "exp": data_expiracao
        }
        token = jwt.encode(jwt_codificado, SECRET_KEY, algorithm=ALGORITHM)
        return token