from flask import Flask, render_template, request, redirect, url_for
import os
import csv
app = Flask(__name__)


@app.route('/')
def show_books():
    
    # step 1 - get the data
    books = []
    with open('books.csv', 'r', newline="\n") as fp:
        reader = csv.reader(fp, delimiter=",")
        
        # skip the header
        next(reader)

        for line in reader:
            books.append({
                'isbn': line[0],
                'title': line[1],
                'author': line[2]
            })

    print(books)
    return render_template('show_books.template.html', books=books)



    # step 2 - process the data (optional)

    # step 3 - send the data to a template


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)