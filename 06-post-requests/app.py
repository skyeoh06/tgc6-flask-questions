from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


# your code here!
@app.route("/")
def hello():
    return render_template("index.template.html")


# @app.route("/", methods=['POST'])
# def processHello():
#     first_name = request.form.get('first-name')
#     last_name = request.form.get('last-name')
#     return render_template('process-hello.template.html',
#                            fn=first_name,
#                            ln=last_name)


@app.route("/", methods=['POST'])
def processHello():
    return render_template('process-hello.template.html',
                           fn=request.form.get('first-name'),
                           ln=request.form.get('last-name'))


@app.route('/calculate')
def calculate():
    return render_template('calculate.template.html')


@app.route('/calculate', methods=['POST'])
def process_calculate():
    print(request.form)
    number1 = int(request.form.get('number1'))
    number2 = int(request.form.get('number2'))
    total = number1 + number2
    return render_template('answer.template.html', total=total)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)