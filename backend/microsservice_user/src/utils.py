from passlib.context import CryptContext
import os

SECRET_KEY = os.getenv("SECRET_KEY")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def criptografar_senha(senha: str):
    return bcrypt_context.hash(senha)

def verificar_senha(senha: str):
    return bcrypt_context.verify(senha, SECRET_KEY)