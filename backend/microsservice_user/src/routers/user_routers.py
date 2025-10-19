from fastapi import APIRouter, Depends, HTTPException
from src.schemas.user_schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session
from src.database import pegar_sessao
from src.utils import verificar_token
from src.models.user_models import UsuarioModel
from src.services.user_services import UsuarioService, LoginService
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm


user_router = APIRouter(prefix="/user", tags=["user"])

@user_router.post("/criar")
async def criar_usuario(schema: UsuarioSchema, sessao: Session = Depends(pegar_sessao)):
    '''
    Rota de criação de usuário
    '''
    usuario = UsuarioService.buscar_usuario_email(schema.email, sessao)
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
    usuario = UsuarioService.autenticar_usuario(schema.email, schema.senha, sessao)
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário ou credenciais inválidas")
    else: 
        access_token = LoginService.gerar_token(usuario.id)
        refresh_token = LoginService.gerar_token(usuario.id, duracao=timedelta(days=7))
        return {
            "access_token": access_token, 
            "refresh_token": refresh_token,
            "token_type": "Bearer"
            }
    
@user_router.post("/login_doc")
async def login_doc(request_form: OAuth2PasswordRequestForm = Depends(), sessao: Session = Depends(pegar_sessao)):
    '''
    Rota de login de usuário pelo formulário do OAuth2 na documentação
    '''
    usuario = UsuarioService.autenticar_usuario(request_form.username, request_form.password, sessao)
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário ou credenciais inválidas")
    else: 
        access_token = LoginService.gerar_token(usuario.id)
        return {
            "access_token": access_token, 
            "token_type": "Bearer"
            }
    
@user_router.get("/refresh")
async def refresh_token(usuario: UsuarioModel = Depends(verificar_token)):
    '''
    Rota para refresh de token
    '''
    acess_token = LoginService.gerar_token(usuario.id)
    return {
        "access_token": acess_token, 
        "token_type": "Bearer"
        }