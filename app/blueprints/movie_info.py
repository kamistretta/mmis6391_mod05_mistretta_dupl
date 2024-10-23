from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db

movie_info = Blueprint('movie_info', __name__)

@movie_info.route('/movies', methods=['GET', 'POST'])
def movies():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new movie
    if request.method == 'POST':
        title = request.form['title']
        director = request.form['director']
        release_year = request.form['release_year']

        # Insert the new movie info into the database
        cursor.execute('INSERT INTO movie_info (title, director, release_year) VALUES (%s, %s, %s)',
                       (title, director, release_year))
        db.commit()

        flash('New movie information added successfully!', 'success')
        return redirect(url_for('movie_info.movies'))

    # Handle GET request to display all movies
    cursor.execute('SELECT * FROM movie_info')
    all_movies = cursor.fetchall()
    return render_template('movie_add.html', all_movies=all_movies)  # Ensure this matches your file name

@movie_info.route('/update_movie/<int:movie_id>', methods=['GET', 'POST'])
def update_movie(movie_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        # Update the movie's details
        title = request.form['title']
        director = request.form['director']
        release_year = request.form['release_year']

        cursor.execute('UPDATE movie_info SET title = %s, director = %s, release_year = %s WHERE movie_id = %s',
                       (title, director, release_year, movie_id))
        db.commit()

        flash('Movie updated successfully!', 'success')
        return redirect(url_for('movie_info.movies'))

    # GET method: fetch movie's current data for pre-populating the form
    cursor.execute('SELECT * FROM movie_info WHERE movie_id = %s', (movie_id,))
    current_movie_info = cursor.fetchone()
    return render_template('update_movie.html', current_movie_info=current_movie_info)

@movie_info.route('/delete_movie/<int:movie_id>', methods=['POST'])
def delete_movie(movie_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the movie
    cursor.execute('DELETE FROM movie_info WHERE movie_id = %s', (movie_id,))
    db.commit()

    flash('Movie deleted successfully!', 'danger')
    return redirect(url_for('movie_info.movies'))
