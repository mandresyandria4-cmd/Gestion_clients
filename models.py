from pydantic import BaseModel
from typing import Optional

class Produit(BaseModel):
    id: Optional[int] = None
    nom: str
    prix: float
    description: Optional[str] = None
