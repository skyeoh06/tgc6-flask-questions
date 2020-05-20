from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# your code here
@app.route('/')
def home():
    return "hi everybody!"


@app.route('/about')
def about_us():
    return "i am very smart"


@app.route('/double/<int:number>')
def double(number):
    number = number * 2
    return str(number)


@app.route('/add/<int:n1>/<int:n2>')
def add_two(n1, n2):
    return str(n1 + n2)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
