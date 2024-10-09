from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db

products = Blueprint('products', __name__)

@products.route('/products', methods=['GET', 'POST'])
def products_list():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new product
    if request.method == 'POST':
        product_name = request.form['product_name']
        category = request.form['category']
        price = request.form['price']
        stock = request.form['stock']

        # Insert the new product info into the database
        cursor.execute('INSERT INTO product_info (product_name, category, price, stock) VALUES (%s, %s, %s, %s)',
                       (product_name, category, price, stock))
        db.commit()

        flash('New product information added successfully!', 'success')
        return redirect(url_for('products.products_list'))

    # Handle GET request to display all products
    cursor.execute('SELECT * FROM product_info')
    all_products = cursor.fetchall()
    return render_template('product_info.html', all_products=all_products)

@products.route('/update_product/<int:product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        # Update the product's details
        product_name = request.form['product_name']
        category = request.form['category']
        price = request.form['price']
        stock = request.form['stock']

        cursor.execute('UPDATE product_info SET product_name = %s, category = %s, price = %s, stock = %s WHERE product_id = %s',
                       (product_name, category, price, stock, product_id))
        db.commit()

        flash('Product updated successfully!', 'success')
        return redirect(url_for('products.products_list'))

    # GET method: fetch product's current data for pre-populating the form
    cursor.execute('SELECT * FROM product_info WHERE product_id = %s', (product_id,))
    current_product_info = cursor.fetchone()
    return render_template('update_product.html', current_product_info=current_product_info)

@products.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the product
    cursor.execute('DELETE FROM product_info WHERE product_id = %s', (product_id,))
    db.commit()

    flash('Product deleted successfully!', 'danger')
    return redirect(url_for('products.products_list'))
