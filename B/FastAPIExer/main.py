from fastapi import FastAPI, HTTPException, status, Response, Depends
from models import Carro, CarroPatch
from typing import Any
from routes import carro_router
import requests

app = FastAPI(title="API", 
            version="0.0.1", 
            description="API de carro de corrida")

#app.include_router(carro_router.router, tags=["Carro"])  


from fastapi import APIRouter

router = APIRouter()

@router.get("/api/v1/carro")
async def get_cursos():
    return {"info": "API está funcionando"}

def fake_db():
    try:
        print("Abrindo a conexão como banco de dados")
    finally:
        print("Conexão concluida, fechando conexão com o banco de dados")

carros = {
    1: {
        "equipe": "1St Phorm",
        "marca": "Porsche",
        "modelo": "GT3",
        "potencia": 400,
        "cambio": "Sequencial",
        "tracao": "Traseira",
        "pneus": "Macios",
        "combustivel": 100
    },
    2: {
        "equipe": "JOTA",
        "marca": "Cadillac",
        "modelo": "V-Series. R.",
        "potencia": 600,
        "cambio": "Sequencial",
        "tracao": "Traseira",
        "pneus": "Medios",
        "combustivel": 70
    },
    # 3: {
    #     "equipe": "Penske",
    #     "marca": "Porsche",
    #     "modelo": "919",
    #     "potencia": 600,
    #     "cambio": "Sequencial",
    #     "tracao": "Traseira",
    #     "pneus": "Duros",
    #     "combustivel": 30
    # }
}


@app.get("/")
def teste():
    return {"Mensagem": "Deu certo"}

@app.get("/carros")
async def get_carros(db: Any = Depends(fake_db)):
    return carros

@app.get("/carros/{carro_id}", description="Retorna 1 carro com um ID específico ou um erro 404",
         summary="Retorna um carro especifico")
async def get_carro(carro_id: int):
    try:
        carro = carros[carro_id]
        return carro
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Carro não encontrado")
    
@app.post("/carros", status_code=status.HTTP_201_CREATED)
async def post_carro(carro: Carro):
    next_id = len(carros) + 1

    carros[next_id] = carro

    del carro.id

    return carro

@app.put("/carros/{carro_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_carro(carro_id: int, carro: Carro):
    if carro_id in carros:
        carros[carro_id] = carro
        carro.id = carro_id
        del carro.id
        return carro
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Carro não encontrado")
    
@app.delete("/carros/{carro_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_carro(carro_id: int):
    if carro_id in carros:
        del carros[carro_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Carro não encontrado")
    
@app.patch("/carros/{carro_id}", status_code=status.HTTP_202_ACCEPTED)
async def patch_carro(carro_id: int, carro_patch: CarroPatch):
    if carro_id in carros:

        stored_carro_data = carros[carro_id]

        update_data = carro_patch.model_dump(exclude_unset=True) # Exclude fields not set in the request

        for key, value in update_data.items():
            stored_carro_data[key] = value
        
        carros[carro_id] = stored_carro_data

        return {"Patch Carro": carro_patch}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Carro não encontrado")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, 
                log_level="info", reload=True)
