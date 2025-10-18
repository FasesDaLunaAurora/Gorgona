from sqlalchemy.orm import Session
from src.models.auth_models import Usuario as UsuarioModel
from src.utils import criptografar_senha

class UsuarioService:

    @staticmethod
    def criar_usuario(sessao: Session, nome: str, email: str, senha: str):
        
        senha_criptografada = criptografar_senha(senha)
        novo_usuario = UsuarioModel(nome=nome, email=email, senha=senha_criptografada)
        sessao.add(novo_usuario)
        sessao.commit()
        sessao.refresh(novo_usuario)
        return novo_usuario