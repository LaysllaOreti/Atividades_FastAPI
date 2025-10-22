from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.personagem_model import PersonagemModel
from schemas.personagem_schema import PersonagemSchema
from core.deps import get_session

# Criando os endpoints da API
router = APIRouter()

# ==============================
# MÉTODO POST
# ==============================
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PersonagemSchema)
async def post_personagem(personagem: PersonagemSchema, db: AsyncSession = Depends(get_session)):
    novo_personagem = PersonagemModel(
        nome=personagem.nome,
        apelido=personagem.apelido,
        idade=personagem.idade,
        ocupacao=personagem.ocupacao
    )

    db.add(novo_personagem)
    await db.commit()
    await db.refresh(novo_personagem)

    return novo_personagem


# ==============================
# MÉTODO GET (todos)
# ==============================
@router.get("/", response_model=List[PersonagemSchema])
async def get_personagens(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PersonagemModel)
        result = await session.execute(query)
        personagens: List[PersonagemModel] = result.scalars().all()

        return personagens


# ==============================
# MÉTODO GET (por ID)
# ==============================
@router.get("/{personagem_id}", response_model=PersonagemSchema, status_code=status.HTTP_200_OK)
async def get_personagem(personagem_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PersonagemModel).filter(PersonagemModel.id == personagem_id)
        result = await session.execute(query)
        personagem = result.scalar_one_or_none()

        if personagem:
            return personagem
        else:
            raise HTTPException(
                detail="Personagem não encontrado",
                status_code=status.HTTP_404_NOT_FOUND
            )


# ==============================
# MÉTODO PUT
# ==============================
@router.put("/{personagem_id}", response_model=PersonagemSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_personagem(personagem_id: int, personagem: PersonagemSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PersonagemModel).filter(PersonagemModel.id == personagem_id)
        result = await session.execute(query)
        personagem_up = result.scalar_one_or_none()

        if personagem_up:
            personagem_up.nome = personagem.nome
            personagem_up.apelido = personagem.apelido
            personagem_up.idade = personagem.idade
            personagem_up.ocupacao = personagem.ocupacao

            await session.commit()
            await session.refresh(personagem_up)

            return personagem_up
        else:
            raise HTTPException(
                detail="Personagem não encontrado",
                status_code=status.HTTP_404_NOT_FOUND
            )
        
# ==============================
# MÉTODO DELETE
# ==============================
@router.delete("/{personagem_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_personagem(personagem_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PersonagemModel).filter(PersonagemModel.id == personagem_id)
        result = await session.execute(query)
        curso_del = result.scalar_one_or_none()

        if curso_del:
            await session.delete(curso_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(
                detail="Curso não encontrado.",
                status_code=status.HTTP_404_NOT_FOUND
            )
