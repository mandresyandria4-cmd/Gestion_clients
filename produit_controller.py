from fastapi import APIRouter, HTTPException
from typing import List
from models import Produit
from service import ProduitService

router = APIRouter(prefix="/produits", tags=["Produits"])
service = ProduitService()

@router.post("/", response_model=Produit, status_code=201)
def ajouter_produit(produit: Produit):
    """Ajouter un nouveau produit."""
    try:
        return service.ajouter_produit(produit)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[Produit])
def lister_produits():
    """Lister tous les produits."""
    return service.lister_produits()
