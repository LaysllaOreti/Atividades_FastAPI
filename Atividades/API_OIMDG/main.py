from fastapi import FastAPI, HTTPException, status, Response, Depends
from models import PersonagensOIncrivelMundoDeGumball
from typing import Any

app = FastAPI(
    title="API - O Incrível Mundo de Gumball",
    version="0.0.1",
    description="Uma API feita com os personagens principais da série animada 'O incrível mundo de Gumball'."
)

def fake_db():
    try:
        print("Connecting to the bank")
    finally:
        print("Closing the bank")

# Base de dados fake (mock)
personagens = {
    1: {
        "nome": "Gumball Watterson",
        "idade": "12",
        "trabalho": "Estudante da Elmore Junior High",
        "frase": "Isso é tão estúpido que pode funcionar!",
        "foto": "https://i.pinimg.com/1200x/01/fe/32/01fe323cf325749617e32e36a57d84af.jpg"
    },
    2: {
        "nome": "Darwin Watterson",
        "idade": "10",
        "trabalho": "Estudante / Melhor amigo e irmão adotivo do Gumball",
        "frase": "Eu acredito em você, Gumball!",
        "foto": "https://i.pinimg.com/736x/78/f3/a5/78f3a5e14c45fba5797a23c94a4629de.jpg"
    },
    3: {
        "nome": "Anais Watterson",
        "idade": "4",
        "trabalho": "Estudante prodígio da Elmore Junior High",
        "frase": "Vocês são todos idiotas.",
        "foto": "https://www.clipartmax.com/png/middle/225-2253265_anais-watterson-holding-toy-amazing-world-of-gumball-sister.png"
    },
    4: {
        "nome": "Nicole Watterson",
        "idade": "38",
        "trabalho": "Funcionária de fábrica (Rainbow Factory)",
        "frase": "Ninguém mexe com minha família!",
        "foto": "https://i.pinimg.com/736x/4a/23/42/4a23421ece48ea9996764a4fa6b6b46a.jpg"
    },
    5: {
        "nome": "Ricardo Watterson",
        "idade": "39",
        "trabalho": "Desempregado (pai em tempo integral)",
        "frase": "Trabalho é para os fracos.",
        "foto": "https://static.wikia.nocookie.net/oncrivelmundodegumball/images/5/5a/Season_3_Richard.png/revision/latest?cb=20161202111000&path-prefix=pt"
    },
    6: {
        "nome": "Banana Joe",
        "idade": "12",
        "trabalho": "Estudante da Elmore Junior High",
        "frase": "É banana time!",
        "foto": "https://thumbnail.imgbin.com/15/19/24/imgbin-gumball-watterson-banana-youtube-cartoon-network-formula-cartoon-all-stars-banana-mGYP6jdS9zpqX4bJFHftzsUzJ_t.jpg"
    },
    7: {
        "nome": "Sr. Gaylord Robinson",
        "idade": "50",
        "trabalho": "Aposentado",
        "frase": "Eu odeio os Watterson!",
        "foto": "https://static.wikia.nocookie.net/oncrivelmundodegumball/images/8/87/Gaylord_Robinson.webp/revision/latest?cb=20230513114044&path-prefix=pt"
    },
    8: {
        "nome": "Carrie Krueger",
        "idade": "12",
        "trabalho": "Estudante da Elmore Junior High",
        "frase": "Eu sou apenas um espírito solitário...",
        "foto": "https://cdn.imgbin.com/2/17/23/imgbin-carrie-krueger-gumball-watterson-wikia-character-cary-pVw9kViH1JfcjMdBf9k1GURxZ.jpg"
    },
    9: {
        "nome": "Penny Fitzgerald",
        "idade": "12",
        "trabalho": "Estudante da Elmore Junior High",
        "frase": "Gumball, eu gosto de você do jeito que você é.",
        "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVa6kg5Cu8plD9e-zagIn8d6U12lYIWZZIwg&s"
    },
    10: {
        "nome": "Tina Rex",
        "idade": "14",
        "trabalho": "Estudante da Elmore Junior High",
        "frase": "Quem vai ser o próximo a apanhar?",
        "foto": "https://upload.wikimedia.org/wikipedia/commons/1/19/Tina_Rex.png"
    }
}


# Rotas

@app.get("/")
async def raiz():
    return {"mensagem": "API - O Incrível Mundo de Gumball"}

@app.get("/personagens")
async def get_personagens(db: Any = Depends(fake_db)):
    return personagens

@app.get("/personagens/{personagem_id}", description="Retorna um personagem com um ID específico")
async def get_personagem(personagem_id: int):
    try:
        return personagens[personagem_id]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Esse personagem não foi encontrado."
        )

@app.post("/personagens", status_code=status.HTTP_201_CREATED, description="Criação de um novo personagem")
async def post_personagem(personagem: PersonagensOIncrivelMundoDeGumball):
    next_id = len(personagens) + 1
    personagens[next_id] = personagem.dict()
    return personagens[next_id]

@app.put("/personagens/{personagem_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_personagem(personagem_id: int, personagem: PersonagensOIncrivelMundoDeGumball):
    if personagem_id in personagens:
        personagens[personagem_id] = personagem.dict()
        return personagens[personagem_id]
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Esse personagem não foi encontrado."
        )

@app.delete("/personagens/{personagem_id}")
async def delete_personagem(personagem_id: int):
    if personagem_id in personagens:
        del personagens[personagem_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Personagem não encontrado"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
