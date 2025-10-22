from fastapi import APIRouter

from api.v1.endpoints import personagem

api_router = APIRouter()
api_router.include_router(personagem.router, prefix='/personagens',
                          tags=["personagens"])

#/api/v1/endpoints é o nosso endpoint completo junto com o prefixo