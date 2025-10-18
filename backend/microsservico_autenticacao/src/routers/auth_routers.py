from fastapi import APIRouter, Depends, HTTPException
from src.database import pegar_sessao
from sqlalchemy.orm import Session
from src.schemas.auth_schemas import Usuario as UsuarioSchema
from src.models.auth_models import Usuario as UsuarioModel
from src.services.auth_services import UsuarioService


auth_router = APIRouter(prefix="/auth", tags=["Autenticação"])

@auth_router.post("/criar_usuario")
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