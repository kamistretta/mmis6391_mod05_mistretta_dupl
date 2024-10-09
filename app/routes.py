from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pet_info')
def pet_info():
    return render_template('pet_info.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/introduction')
def introduction():
    return render_template('introduction.html')

@app.route('/products')
def products():
    return render_template('products.html')


if __name__ == '__main__':
    app.run(debug=True)