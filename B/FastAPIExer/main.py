from fastapi import FastAPI
from routes import carro_router

app = FastAPI(title="API", 
            version="0.0.1", 
            description="API de carro de corrida") 

app.include_router(carro_router.router, tags=["Carro"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, 
                log_level="info", reload=True)
