# Exercice 1 — API Gestion de Produit (FastAPI)

## Structure
```
exercice1_gestion_produit/
├── main.py                        ← Point d'entrée
├── models.py                      ← Modèle Produit (Pydantic)
├── controller/
│   └── produit_controller.py      ← Routes HTTP (Controller)
├── service/
│   └── produit_service.py         ← Logique métier (Service)
└── repository/
    └── produit_repository.py      ← Accès aux données (Repository)
```

## Lancer le serveur
```bash
pip install fastapi uvicorn
python main.py
```
Ou directement :
```bash
uvicorn main:app --reload
```

## Endpoints
| Méthode | URL          | Description         |
|---------|--------------|---------------------|
| GET     | /            | Message de bienvenue |
| POST    | /produits/   | Ajouter un produit  |
| GET     | /produits/   | Lister les produits |

## Exemple d'utilisation
```bash
# Ajouter un produit
curl -X POST http://localhost:8000/produits/ \
  -H "Content-Type: application/json" \
  -d '{"nom": "Laptop", "prix": 999.99, "description": "PC portable"}'

# Lister les produits
curl http://localhost:8000/produits/
```

## Documentation auto
Swagger UI : http://localhost:8000/docs
