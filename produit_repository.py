from typing import List, Optional
from models import Produit

class ProduitRepository:
    def __init__(self):
        self._produits: List[Produit] = []
        self._next_id = 1

    def ajouter(self, produit: Produit) -> Produit:
        produit.id = self._next_id
        self._next_id += 1
        self._produits.append(produit)
        return produit

    def lister(self) -> List[Produit]:
        return self._produits

    def trouver_par_id(self, produit_id: int) -> Optional[Produit]:
        for p in self._produits:
            if p.id == produit_id:
                return p
        return None
