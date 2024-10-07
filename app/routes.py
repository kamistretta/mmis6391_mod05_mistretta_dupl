from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/runners')
def runners():
    return render_template('runners.html')

@app.route('/story')
def story():
    return render_template('story.html')
