from sqlalchemy.orm import Session
from src.models.user_models import Usuario as UsuarioModel
from src.utils import criptografar_senha

class UsuarioService:

    @staticmethod
    def criar_usuario(sessao: Session, nome: str, email: str, senha: str, ativo: bool = True, admin: bool = False):
        
        senha_criptografada = criptografar_senha(senha)
        novo_usuario = UsuarioModel(nome=nome, email=email, senha=senha_criptografada, ativo=ativo, admin=admin)
        sessao.add(novo_usuario)
        sessao.commit()
        sessao.refresh(novo_usuario)
        return novo_usuario