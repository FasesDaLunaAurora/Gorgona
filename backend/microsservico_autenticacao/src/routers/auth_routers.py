from fastapi import APIRouter, Depends
from src.database import pegar_sessao
from src.models.auth_models import Usuario as UsuarioModel
from src.services.auth_services import UsuarioService


auth_router = APIRouter(prefix="/auth", tags=["Autenticação"])

@auth_router.post("/criar_usuario")
async def criar_usuario(email: str, nome: str, senha: str, sessao= Depends(pegar_sessao)):
    '''
    Rota de criação de usuário
    '''
    usuario = sessao.query(UsuarioModel).filter(UsuarioModel.email == email).first()
    if usuario:
        return {"erro": "Usuário já existe"}
    else:
        novo_usuario = UsuarioService.criar_usuario(sessao, nome, email, senha)
        return {"mensagem": f"Usuário {novo_usuario.nome} criado com sucesso"}