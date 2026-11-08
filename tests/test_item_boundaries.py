import pytest


@pytest.mark.parametrize(
    ("payload", "expected_status"),
    [
        ({"name": "x" * 80, "quantity": 1}, 201),
        ({"name": "x" * 81, "quantity": 1}, 422),
        ({"name": "valid item", "quantity": 1000}, 201),
        ({"name": "valid item", "quantity": 1001}, 422),
        ({"name": "", "quantity": 1}, 422),
    ],
)
def test_item_field_boundaries(client, payload, expected_status):
    response = client.post("/items", json=payload)
    assert response.status_code == expected_status
