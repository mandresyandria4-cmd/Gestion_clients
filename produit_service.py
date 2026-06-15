from typing import List
from models import Produit
from repository import ProduitRepository

class ProduitService:
    def __init__(self):
        self.repository = ProduitRepository()

    def ajouter_produit(self, produit: Produit) -> Produit:
        if not produit.nom or produit.nom.strip() == "":
            raise ValueError("Le nom du produit est obligatoire.")
        if produit.prix < 0:
            raise ValueError("Le prix ne peut pas être négatif.")
        return self.repository.ajouter(produit)

    def lister_produits(self) -> List[Produit]:
        return self.repository.lister()
