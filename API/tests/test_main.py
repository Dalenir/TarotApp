from collections import namedtuple

import pytest as pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    jsn = response.json()
    assert 'message' in jsn
    assert jsn['message']
