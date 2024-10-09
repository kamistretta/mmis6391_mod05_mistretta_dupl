from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book_info')
def book_info():
    return render_template('book_info.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/upcoming')
def upcoming():
    return render_template('upcoming.html')

if __name__ == '__main__':
    app.run(debug=True)