from fastapi import APIRouter, Depends, HTTPException
from src.database import pegar_sessao
from sqlalchemy.orm import Session
from backend.microsservice_user.src.schemas.user_schemas import Usuario as UsuarioSchema
from src.models.user_models import Usuario as UsuarioModel
from backend.microsservice_user.src.services.user_services import UsuarioService


user_router = APIRouter(prefix="/user", tags=["user"])

@user_router.post("/criar_usuario")
async def criar_usuario(schema: UsuarioSchema, sessao: Session = Depends(pegar_sessao)):
    '''
    Rota de criação de usuário
    '''
    usuario = sessao.query(UsuarioModel).filter(UsuarioModel.email == schema.email).first()
    if usuario:
        raise HTTPException(status_code=409, detail="Email já cadastrado")
    else:
        novo_usuario = UsuarioService.criar_usuario(sessao, schema.nome, schema.email, schema.senha, schema.ativo, schema.admin)
        return {"mensagem": f"Usuário {novo_usuario.nome} criado com sucesso"}