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
    isbn = request.form.get('isbn')
    title = request.form.get('book-title')
    author = request.form.get('author')

    # step 2 - process the data

    # step 2.1 : open the file
    with open('books.csv', 'a', newline="\n") as fp:
        # step 2.2: add in new row in

        # step 2.3 create the csv writer
        writer = csv.writer(fp, delimiter=",")

        # step 2.4 append the row in using the csv writer
        writer.writerow([isbn, title, author])

    # step 3 - render a template or redirect to a view function
    return redirect(url_for('show_books'))


@app.route('/edit_book/<isbn>')
def edit_book(isbn):
    # step 1: get the book specified by the isbn
    book = None
    all_books = get_all_books_from_file()
    for b in all_books:
        if b['isbn'] == isbn:
            book = b
            break

    return render_template('edit_book.template.html', book=book)


@app.route('/edit_book/<isbn>', methods=["POST"])
def process_edit_book(isbn):
    # step 1: read in all the books
    books = get_all_books_from_file()

    # step 2: find the book to be updated by its isbn
    for i in range(len(books)):
        # step 3: update the book in the list directly
        if books[i]['isbn'] == isbn:
            books[i]['isbn'] = request.form.get('isbn')
            books[i]['title'] = request.form.get('book-title')
            books[i]['author'] = request.form.get('author')
            break

    # step 4: write all books into data.csv
    # overwriting the csv file with the modified book information
    with open('books.csv', 'w', newline="\n") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(['isbn', 'title', 'author'])
        for b in books:
            writer.writerow([
                b['isbn'],
                b['title'],
                b['author']
            ])

    return redirect(url_for('show_books'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
