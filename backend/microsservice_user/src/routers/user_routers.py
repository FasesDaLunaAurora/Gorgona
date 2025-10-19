from fastapi import APIRouter, Depends, HTTPException
from src.database import pegar_sessao
from sqlalchemy.orm import Session
from src.schemas.user_schemas import UsuarioSchema, LoginSchema
from src.services.user_services import UsuarioService
from datetime import timedelta


user_router = APIRouter(prefix="/user", tags=["user"])

@user_router.post("/criar_usuario")
async def criar_usuario(schema: UsuarioSchema, sessao: Session = Depends(pegar_sessao)):
    '''
    Rota de criação de usuário
    '''
    usuario = UsuarioService.buscar_usuario_email(sessao, schema.email, schema.senha)
    if usuario:
        raise HTTPException(status_code=409, detail="Email já cadastrado")
    else:
        novo_usuario = UsuarioService.criar_usuario(sessao, schema.nome, schema.email, schema.senha, schema.ativo, schema.admin)
        return {"mensagem": f"Usuário {novo_usuario.nome} criado com sucesso"}
    
@user_router.post("/login")
async def login(schema: LoginSchema, sessao: Session = Depends(pegar_sessao)):
    '''
    Rota de login de usuário
    '''
    usuario = UsuarioService.autenticar_usuario(sessao, schema.email, schema.senha)
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário ou credenciais inválidas")
    else: 
        access_token = UsuarioService.gerar_token(usuario.id)
        refresh_token = UsuarioService.gerar_token(usuario.id, duracao=timedelta(days=7))
        return {
            "access_token": access_token, 
            "refresh_token": refresh_token,
            "token_type": "Bearer"
            }