# test_hello.py
from app import app
from bs4 import BeautifulSoup

def test_ask_name_route():
    response = app.test_client().post('/', data={
        'first-name':'Ah Kow',
        'last-name':'Tan'
    })
    assert response.status_code == 200
    
    soup = BeautifulSoup(response.data, features='html.parser')
    assert soup.find('p').string.strip() == 'Hi Ah Kow Tan!'


def test_calculate_route():
    response = app.test_client().post('/calculate', data={
        'number1':3,
        'number2':4
    })

    assert response.status_code == 200
    
    soup = BeautifulSoup(response.data, features='html.parser')
    assert soup.find('div').string.strip() == '7'

