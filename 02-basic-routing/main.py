from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# your code here
@app.route('/')
def home():
    return "hi everybody!"

@app.route('/about')
def about_me():
    return "i am very smart"

@app.route('/double/<number>')
def double(number):
    return str(int(number) * 2)

@app.route('/add/<n1>/<n2>')
def add(n1, n2):
    return str(int(n1)+int(n2))

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)