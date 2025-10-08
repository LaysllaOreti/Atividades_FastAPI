from fastapi import APIRouter

from api.v1.endpoints import filme

api_router = APIRouter()

api_router.include_router(filme.router, prefix='/filmes', tags=["filmes"])

# /api/v1/filmes -> esse será nosso endpoint completo junto ao prefixo!
