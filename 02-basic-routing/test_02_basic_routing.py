# test_hello.py
from main import app

def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'hi everybody!'

def test_about():
    response = app.test_client().get('/about')
    assert response.status_code == 200
    assert response.data == b'i am very smart'

def test_double():
    response = app.test_client().get('/double/6')
    assert response.status_code == 200
    assert response.data == b'12'

def test_add():
    response = app.test_client().get('/add/42/102')
    assert response.status_code == 200
    assert response.data == b'144'