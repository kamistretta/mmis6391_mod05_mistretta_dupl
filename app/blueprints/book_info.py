from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db

book_info = Blueprint('book_info', __name__)


@book_info.route('/book', methods=['GET', 'POST'])
def book():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new book
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        price = request.form['price']
        pub_date = request.form['pub_date']

        # Insert the new book info into the database
        cursor.execute('INSERT INTO book_info (title, author, genre, price, pub_date) VALUES (%s, %s, %s, %s, %s)',
                       (title, author, genre, price, pub_date))
        db.commit()

        flash('New book information added successfully!', 'success')
        return redirect(url_for('book_info.book'))

    # Handle GET request to display all books
    cursor.execute('SELECT * FROM book_info')
    all_books = cursor.fetchall()
    return render_template('book_info.html', all_books=all_books)


@book_info.route('/update_book/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        # Update the book's details
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        price = request.form['price']
        pub_date = request.form['pub_date']

        cursor.execute('UPDATE book_info SET title = %s, author = %s, genre = %s, price = %s, pub_date = %s WHERE book_id = %s',
                       (title, author, genre, price, pub_date, book_id))
        db.commit()

        flash('Book updated successfully!', 'success')
        return redirect(url_for('book_info.book'))

    # GET method: fetch book's current data for pre-populating the form
    cursor.execute('SELECT * FROM book_info WHERE book_id = %s', (book_id,))
    current_book_info = cursor.fetchone()
    return render_template('update_book.html', current_book_info=current_book_info)


@book_info.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the book
    cursor.execute('DELETE FROM book_info WHERE book_id = %s', (book_id,))
    db.commit()

    flash('Book deleted successfully!', 'danger')
    return redirect(url_for('book_info.book'))
