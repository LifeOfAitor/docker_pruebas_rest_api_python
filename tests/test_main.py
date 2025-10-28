from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "mensaje" in data
    assert data["mensaje"] == "¡API funcionando!"
    assert "tutorial" in data

def test_listar_items_vacio():
    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data == []

def test_crear_item():
    nuevo_item = {
        "id": 1,
        "nombre": "Lapiz",
        "descripcion": "Lapiz HB"
    }
    response = client.post("/items", json=nuevo_item)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == nuevo_item["id"]
    assert data["nombre"] == nuevo_item["nombre"]

def test_listar_items_con_uno():
    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["nombre"] == "Lapiz"

def test_obtener_item_existente():
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["nombre"] == "Lapiz"

def test_obtener_item_no_existente():
    response = client.get("/items/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Item no encontrado"
