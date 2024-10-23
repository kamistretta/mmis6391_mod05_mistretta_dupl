from flask import render_template, request, redirect, url_for, flash
from . import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/movie_list')   # Ensure this matches the file name in the templates folder
def movie_list():
    return render_template('movie_list.html')
