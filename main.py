from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de datos
class Item(BaseModel):
    id: int
    nombre: str
    descripcion: str = None

# Base de datos temporal (en memoria)
items_db = []

# Ruta raíz
@app.get("/")
def leer_root():
    tutorial = {
        "mensaje": "¡API funcionando! version 2",
        "tutorial": {
            "GET /items": "Lista todos los items. Puedes filtrar por nombre con el parámetro 'nombre'.",
            "GET /items/{item_id}": "Obtiene un item específico por su ID.",
            "POST /items": "Crea un nuevo item. Debes enviar JSON con 'id', 'nombre' y opcionalmente 'descripcion'.",
            "PUT /items/{item_id}": "Actualiza un item existente. Debes enviar JSON completo con el mismo 'id'.",
            "DELETE /items/{item_id}": "Elimina un item por su ID.",
            "nota": "Recuerda que el campo 'id' debe ser único para cada item."
        },
        "ejemplo_post": {
            "curl": "curl -X POST http://localhost:8000/items -H 'Content-Type: application/json' -d '{\"id\":1, \"nombre\":\"Lapiz\", \"descripcion\":\"Lapiz HB\"}'"
        }
    }
    return tutorial


# Obtener todos los items
@app.get("/items", response_model=List[Item])
def listar_items():
    return items_db

# Obtener un item por ID
@app.get("/items/{item_id}", response_model=Item)
def obtener_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item no encontrado")

# Crear un nuevo item
@app.post("/items", response_model=Item)
def crear_item(item: Item):
    items_db.append(item)
    return item
