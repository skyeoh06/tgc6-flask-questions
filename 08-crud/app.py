from flask import Flask, render_template, request, redirect, url_for
import os
import csv
app = Flask(__name__)


@app.route('/')
def show_books():

    # step 1 - get the data
    books = get_all_books_from_file()

    print(books)
    # step 3 - send the data to a template
    return render_template('show_books.template.html', books=books)


@app.route('/search')
def show_search_form():
    return render_template('show_search_form.template.html')


# @app.route('/search', methods=['POST'])
# def process_search_form():
#     matches = []   #accumulator - will at the end have all the books that matches the search term
#     search_terms = request.form.get('search-terms')
#     with open('books.csv', 'r', newline="\n") as fp:
#         reader = csv.reader(fp, delimiter=",")
#         for line in reader:
#             if line[1] == search_terms:
#                 matches.append({
#                     'isbn': line[0],
#                     'title': line[1],
#                     'author': line[2]
#                 })

#     return render_template('show_books.template.html', books=matches)

@app.route('/search', methods=["POST"])
def process_search_form():
    all_books = get_all_books_from_file()
    matches = []
    for book in all_books:
        if book['title'] == request.form.get('search-terms'):
            matches.append(book)

    return render_template('show_books.template.html', books=matches)


def get_all_books_from_file():
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
    return books


@app.route('/add')
def display_add_form():
    return render_template('add_book.template.html')


@app.route('/add', methods=["POST"])
def process_add():

    # step 1 - get the data
    print(request.form)

    # step 2 - process the data

    # step 3 - render a template or redirect to a view function

    return "data recieved"


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
