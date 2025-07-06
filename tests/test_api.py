import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app

from app.main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}

def test_post_and_get_notes(client):
    note = {"title": "Note 1", "content": "This is a secure note."}
    post_res = client.post("/notes", json=note)
    assert post_res.status_code == 201
    get_res = client.get("/notes")
    assert get_res.status_code == 200
    assert any(n["title"] == "Note 1" for n in get_res.get_json())
