from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db

genre_info = Blueprint('genre_info', __name__)

@genre_info.route('/genres', methods=['GET', 'POST'])
def genres():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new genre
    if request.method == 'POST':
        genre = request.form['genre']

        # Insert the new genre into the database
        cursor.execute('INSERT INTO genre_info (genre) VALUES (%s)', (genre,))
        db.commit()

        flash('New genre added successfully!', 'success')
        return redirect(url_for('genre_info.genres'))

    # Handle GET request to display all genres
    cursor.execute('SELECT * FROM genre_info')
    all_genres = cursor.fetchall()
    return render_template('genres.html', all_genres=all_genres)  # Ensure this matches your file name

@genre_info.route('/update_genre/<int:genre_id>', methods=['GET', 'POST'])
def update_genre(genre_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        # Update the genre's details
        genre = request.form['genre']

        cursor.execute('UPDATE genre_info SET genre = %s WHERE genre_id = %s', (genre, genre_id))
        db.commit()

        flash('Genre updated successfully!', 'success')
        return redirect(url_for('genre_info.genres'))

    # GET method: fetch genre's current data for pre-populating the form
    cursor.execute('SELECT * FROM genre_info WHERE genre_id = %s', (genre_id,))
    current_genre_info = cursor.fetchone()
    return render_template('genre_update.html', current_genre_info=current_genre_info)

@genre_info.route('/delete_genre/<int:genre_id>', methods=['POST'])
def delete_genre(genre_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the genre
    cursor.execute('DELETE FROM genre_info WHERE genre_id = %s', (genre_id,))
    db.commit()

    flash('Genre deleted successfully!', 'danger')
    return redirect(url_for('genre_info.genres'))
