from fastapi import FastAPI, HTTPException, status, Response, Depends, requests
from models import PersonagensToyStory
from typing import Optional, Any
from routes import curso_router, user_router

app = FastAPI(title="API - Persoangens de Toy Story", version='0.0.1', description="Uma API feita com a DS 18 para aprender FastAPI")

app.include_router(curso_router.router, tags=["Cursos"]) #Solicitar uma rota que já existe e trabalhar em cima dela
app.include_router(user_router.router, tags=["Usuários"])

@app.get("/pokemon/{name}")
def get_pokemon(name: str):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    if response.status.code == 200:
        return response.json()
    return {"Message: Pokemon not found"}

def fake_db():
    try:
        print("Conectando com o banco")
    finally:
        print("Fechando o banco")
#decorator (@) indica que a função que está abaixo dela terá outra função que vai ser criada
# url:youtube.com.br/algumcoisa (algumacoisa é o endpoint)

personagens = {
    1: {
        "nome": "Woody",
        "dono": "Andy",
        "tamanho": "Pequeno",
        "foto": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dentrodahistoria.com.br%2Fblog%2Fentretenimento-e-diversao%2Fdesenhos-filmes-youtube%2Fconheca-personagens-de-toy-story%2F&psig=AOvVaw24VdHzUP4rwJvx_aw54yZG&ust=1755776299101000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCICWlcmmmY8DFQAAAAAdAAAAABAL"
    },
    2: {
        "nome": "Jessie",
        "dono": "Emily",
        "tamanho": "Pequeno",
        "foto": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dentrodahistoria.com.br%2Fblog%2Fentretenimento-e-diversao%2Fdesenhos-filmes-youtube%2Fconheca-personagens-de-toy-story%2F&psig=AOvVaw24VdHzUP4rwJvx_aw54yZG&ust=1755776299101000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCICWlcmmmY8DFQAAAAAdAAAAABAV"
    }
}

@app.get("/")
async def raiz():
    return{"Hello DS18!"}

@app.get("/personagens")
async def get_personagens(db: Any = Depends(fake_db)):
    return personagens

@app.get("/personagens/{personagem_id}", description="Retorna um personagem com um ID específico")
async def get_personagem(personagem_id: int):
    try:
        personagem = personagens[personagem_id]
        return personagem
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")
    
@app.post("/personagens", status_code=status.HTTP_201_CREATED)
async def post_personagem(personagem: Optional[PersonagensToyStory] = None):

    next_id = len(personagens) + 1
    personagens[next_id] = personagem
    del personagem.id
    return personagem

@app.put("/personagens/{personagem_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_personagem(personagem_id:int, personagem: PersonagensToyStory):
    if personagem_id in personagens:
        personagens[personagem_id] = personagem
        personagem.id = personagem_id
        del personagem.id
        return personagem
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")

@app.delete("/personagens/{personagem_id}")
async def delete_personagem(personagem_id: int):
    if personagem_id in personagens:
        del personagens[personagem_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")  

@app.get("/calcular")
async def calcular(a: int, b: int):

    soma = a + b
    return {soma}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8002, log_level="info", reload=True)
