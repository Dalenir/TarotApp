from collections import namedtuple

import pytest as pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


NameParams = namedtuple('NameParams', ['return_code', 'name', 'response_dict'])


@pytest.fixture(scope="function", params=[NameParams(404, '', {'detail': 'Not Found'}),
                                          NameParams(200, 'String', {'message': 'Hello String'}),
                                          NameParams(422, '$%WN',
                                                     {'detail': 'string does not match regex "^[a-zA-Z0-9_]*$"'}),
                                          NameParams(200, 'A'*100, {'message': f'Hello {"A"*100}'})],
                ids=['Empty string', 'Valid string', "Numbers and symbols", 'Large string'])
def name_data(request):
    return request.param


def test_root_hello_name(name_data: NameParams):
    response = client.get(f"/hello/{name_data.name}")
    assert response.status_code == name_data.return_code
    assert response.json() == name_data.response_dict
