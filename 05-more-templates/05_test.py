# test_hello.py
from app import app
from bs4 import BeautifulSoup

def test_index_route_task_1():
    response = app.test_client().get('/')
    assert response.status_code == 200
    
    soup = BeautifulSoup(response.data, features='html.parser')
    assert soup.find('h1').string == 'About Us'
    assert soup.find('p').string.strip() == 'We have the best friend chicken ever!'

def test_index_route_task_2():
    response = app.test_client().get('/')
    assert response.status_code == 200
    
    soup = BeautifulSoup(response.data, features='html.parser')
    assert soup.find('a')['href'].split('/')[1] == 'products'

def test_index_route_task_3():
    response = app.test_client().get('/')
    assert response.status_code == 200
    
    soup = BeautifulSoup(response.data, features='html.parser')
    assert soup.find('link')['href'] == 'static/styles.css'

def test_products_route():
    response = app.test_client().get('/products')
    assert response.status_code == 200
    
    soup = BeautifulSoup(response.data, features='html.parser')
    assert soup.find('h1').string == 'Products'
    assert len(soup.find_all('li')) == 3
    assert soup.find('img')['src'] == 'static/friedchicken.jpg'



