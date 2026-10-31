def test_health_contract(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_and_fetch_item(client):
    created = client.post("/items", json={"name": "keyboard", "quantity": 2})
    assert created.status_code == 201
    body = created.json()
    assert body == {"id": 1, "name": "keyboard", "quantity": 2}
    fetched = client.get(f"/items/{body['id']}")
    assert fetched.status_code == 200
    assert fetched.json() == body

def test_rejects_invalid_quantity(client):
    response = client.post("/items", json={"name": "mouse", "quantity": 0})
    assert response.status_code == 422

def test_unknown_item_returns_404(client):
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "item not found"

def test_missing_required_field_returns_422(client):
    response = client.post("/items", json={"name": "monitor"})
    assert response.status_code == 422

def test_list_items_starts_empty(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {"items": []}