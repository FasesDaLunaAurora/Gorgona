from fastapi import APIRouter
from src.database import pegar_sessao

auth_router = APIRouter(prefix="/auth", tags=["Autenticação"])

@auth_router.get("/")
async def autenticar():
    '''
    Rota de autenticação
    '''
    return {"mensagem": "Rota de autenticação"}