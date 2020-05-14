# test_hello.py
from app import app
from bs4 import BeautifulSoup

def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 200
    soup = BeautifulSoup(response.data, features='html.parser')
    assert soup.find_all('h1')[0].string == 'hello world'
    assert soup.find_all('a')[0]['href'].split('/')[1] == 'gallery'
    assert soup.find_all('link')[0]['href'] == 'static/styles.css'

def test_can_display_image():
    response = app.test_client().get('/gallery')
    assert response.status_code == 200

    soup = BeautifulSoup(response.data, features='html.parser')
    print(soup.find_all('img')[0])
    assert soup.find_all('img')[0]['src'] == 'static/puppy.jpg'
    