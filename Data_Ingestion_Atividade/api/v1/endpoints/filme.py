from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.filme_model import FilmeModel
from schemas.filme_schema import FilmeSchema

from core.deps import get_session

router = APIRouter()

# método POST
# Vou responder um FilmeSchema e também receber um FilmeSchema!
# API envia JSON e espera receber JSON

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FilmeSchema)
async def post_filme(filme: FilmeSchema, db: AsyncSession = Depends(get_session)):
    novo_filme = FilmeModel(
        titulo=filme.titulo,
        produtora=filme.produtora,
        atores_principais=filme.atores_principais,
        horas_filme=filme.horas_filme
    )
    
    db.add(novo_filme)
    await db.commit()
    await db.refresh(novo_filme)  # para garantir que o novo objeto tenha os dados atualizados (como o id)

    return novo_filme

# método GET
@router.get('/', response_model=List[FilmeSchema])
async def get_filmes(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FilmeModel)
        result = await session.execute(query)
        filmes: List[FilmeModel] = result.scalars().all()

        return filmes

@router.get("/{filme_id}", response_model=FilmeSchema, status_code=status.HTTP_200_OK)
async def get_filme(filme_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FilmeModel).filter(FilmeModel.id == filme_id)
        result = await session.execute(query)
        filme = result.scalar_one_or_none()

        if filme:
            return filme
        else:
            raise HTTPException(
                detail="Filme não encontrado.",
                status_code=status.HTTP_404_NOT_FOUND
            )

# método PUT
@router.put("/{filme_id}", response_model=FilmeSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_filme(filme_id: int, filme: FilmeSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FilmeModel).filter(FilmeModel.id == filme_id)
        result = await session.execute(query)
        filme_up = result.scalar_one_or_none()

        if filme_up:
            filme_up.titulo = filme.titulo
            filme_up.produtora = filme.produtora
            filme_up.atores_principais = filme.atores_principais
            filme_up.horas_filme = filme.horas_filme

            await session.commit()
            await session.refresh(filme_up)  # Atualiza o objeto com dados do banco

            return filme_up
        else:
            raise HTTPException(
                detail="Filme não encontrado.",
                status_code=status.HTTP_404_NOT_FOUND
            )
        
# método DELETE
@router.delete("/{filme_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_filme(filme_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FilmeModel).filter(FilmeModel.id == filme_id)
        result = await session.execute(query)
        filme_del = result.scalar_one_or_none()

        if filme_del:
            await session.delete(filme_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(
                detail="Filme não encontrado.",
                status_code=status.HTTP_404_NOT_FOUND
            )