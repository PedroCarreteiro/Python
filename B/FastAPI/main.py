from fastapi import FastAPI, HTTPException, status, Response
from models import PersonagensOnePiece

app = FastAPI()

personagens = {
    1: {
        "nome": "Monkey D. Luffy",
        "fruta": "Gomu Gomu no Mi",
        "recompensa": 3000000000,
        "funcao": "Capitão",
        "foto": "https://i.pinimg.com/736x/14/fe/b6/14feb6e3b404459ca7f62dfe5d60b4d6.jpg"
    },
    2: {
        "nome": "Trafalgar D. Water Law",
        "fruta": "Ope Ope no Mi",
        "recompensa": 3000000000,
        "funcao": "Capitão",
        "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwqkhBwpSnZ_lNQD52uhzDQbaw4rDZ9LLfFQ&s"
    }
}


@app.get("/")
def teste():
    return {"Mensagem": "Deu certo"}

@app.get("/personagens")
async def get_personagens():
    return personagens

@app.get("/personagens/{personagem_id}")
async def get_personagem(personagem_id: int):
    try:
        personagem = personagens[personagem_id]
        return personagem
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Personagem não encontrado")
    
@app.post("/personagens", status_code=status.HTTP_201_CREATED)
async def post_personagem(personagem: PersonagensOnePiece):
    next_id = len(personagens) + 1

    personagens[next_id] = personagem

    del personagem.id

    return personagem

@app.put("/personagens/{personagem_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_personagem(personagem_id: int, personagem: PersonagensOnePiece):
    if personagem_id in personagens:
        personagens[personagem_id] = personagem
        personagem.id = personagem_id
        del personagem.id
        return personagem
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Personagem não encontrado")
    
@app.delete("/personagens/{personagem_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_personagem(personagem_id: int):
    if personagem_id in personagens:
        del personagens[personagem_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Personagem não encontrado")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, 
                log_level="info", reload=True)
