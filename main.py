from fastapi import FastAPI
from controller import router

app = FastAPI(
    title="API Gestion de Produit",
    description="API REST pour gérer des produits (ajouter, lister)",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API Gestion de Produit"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
