from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

# configuração do SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# importação dos modelos e schemas
from models.personagens_model import PersonagensModel, PersonagensSchemaPatch
from schemas.personagens_schema import PersonagensSchema

from core.deps import get_session

router = APIRouter()

# MÉTODO POST
# cria um novo personagem no banco de dados.
# o ID é gerado automaticamente pelo banco.
# o endpoint recebe e retorna dados no formato JSON conforme o PersonagensSchema.
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PersonagensSchema)
async def post_personagens(personagem: PersonagensSchema, db: AsyncSession = Depends(get_session)):
    # cria uma nova instância do personagem com os dados recebidos na requisição
    novo_personagem = PersonagensModel(
        nome=personagem.nome,
        idade=personagem.idade,
        ocupacao=personagem.ocupacao
    )
    
    db.add(novo_personagem)
    await db.commit()
    await db.refresh(novo_personagem)
    return novo_personagem

# MÉTODO GET (TODOS)
# retorna uma lista com todos os personagens cadastrados.
@router.get("/", response_model=List[PersonagensSchema])
async def get_personagens(db: AsyncSession = Depends(get_session)):
    query = select(PersonagensModel)
    result = await db.execute(query)
    personagens: List[PersonagensModel] = result.scalars().all()
    return personagens

# MÉTODO GET (POR ID)
# busca um personagem específico pelo ID.
@router.get("/{personagem_id}", response_model=PersonagensSchema, status_code=status.HTTP_200_OK)
async def get_personagem(personagem_id: int, db: AsyncSession = Depends(get_session)):
    query = select(PersonagensModel).filter(PersonagensModel.id == personagem_id)
    result = await db.execute(query)
    personagem = result.scalar_one_or_none()

    if personagem:
        return personagem
    else:
        raise HTTPException(
            detail="Personagem de BrBa não encontrado.",
            status_code=status.HTTP_404_NOT_FOUND
        )

# MÉTODO PUT
# atualiza todos os dados de um personagem existente.
# requer que todos os campos do PersonagensSchema sejam enviados.
@router.put("/{personagem_id}", response_model=PersonagensSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_personagem(personagem_id: int, personagem: PersonagensSchema, db: AsyncSession = Depends(get_session)):
    query = select(PersonagensModel).filter(PersonagensModel.id == personagem_id)
    result = await db.execute(query)
    personagem_up = result.scalar_one_or_none()

    if personagem_up:
        # atualiza os campos do personagem
        personagem_up.nome = personagem.nome
        personagem_up.idade = personagem.idade
        personagem_up.grupo = personagem.grupo

        await db.commit()
        await db.refresh(personagem_up)
        return personagem_up
    else:
        raise HTTPException(
            detail="Personagem não foi encontrado no banco de dados.",
            status_code=status.HTTP_404_NOT_FOUND
        )

# MÉTODO DELETE
# exclui um personagem do banco de dados com base no ID.
@router.delete("/{personagem_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_personagem(personagem_id: int, db: AsyncSession = Depends(get_session)):
    query = select(PersonagensModel).filter(PersonagensModel.id == personagem_id)
    result = await db.execute(query)
    personagem_del = result.scalar_one_or_none()

    if personagem_del:
        await db.delete(personagem_del)
        await db.commit()
        # retorna uma resposta sem conteúdo (204)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            detail="Personagem não encontrado.",
            status_code=status.HTTP_404_NOT_FOUND
        )


# MÉTODO PATCH
# atualiza parcialmente um personagem existente.
# apenas os campos enviados na requisição serão alterados.
@router.patch("/{personagem_id}", response_model=PersonagensSchema, status_code=status.HTTP_202_ACCEPTED)
async def patch_personagem(personagem_id: int, personagem_payload: PersonagensSchemaPatch, db: AsyncSession = Depends(get_session)):
    query = select(PersonagensModel).filter(PersonagensModel.id == personagem_id)
    result = await db.execute(query)
    personagem_no_banco = result.scalar_one_or_none()

    if not personagem_no_banco:
        raise HTTPException(
            detail="Personagem não foi encontrado no banco de dados.",
            status_code=status.HTTP_404_NOT_FOUND
        )

    # Atualiza apenas os campos informados (exclude_unset=True)
    update_data = personagem_payload.model_dump(exclude_unset=True)

    # Aplica as alterações no objeto existente
    for key, value in update_data.items():
        setattr(personagem_no_banco, key, value)

    await db.commit()
    await db.refresh(personagem_no_banco)

    return personagem_no_banco
