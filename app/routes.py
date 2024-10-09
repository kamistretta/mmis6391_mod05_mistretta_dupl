from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/introduction')
def introduction():
    return render_template('introduction.html')

