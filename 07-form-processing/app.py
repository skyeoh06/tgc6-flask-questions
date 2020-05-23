from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.template.html')


@app.route('/book')
def add_book():
    return render_template('book.template.html')


@app.route('/process_booking', methods=['POST'])
def process_booking():
    customer_name = request.form.get('customer-name')
    seating_type = request.form.get('seating-type')
    time_period = request.form.get('time-period')
    services = request.form.getlist('services')
    hear_about = request.form.get('hear-about')
    return render_template('results.template.html',
                           customer_name=customer_name,
                           seating_type=seating_type,
                           time_period=time_period,
                           services=", ".join(services),
                           hear_about=hear_about
                           )


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)