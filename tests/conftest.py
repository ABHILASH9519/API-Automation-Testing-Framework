import pytest
import demo_api.main as api_module
from fastapi.testclient import TestClient

@pytest.fixture()
def client():
    api_module._items.clear()
    api_module._next_id = 1
    return TestClient(api_module.app)