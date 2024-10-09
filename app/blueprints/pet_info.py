from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db

pet_info = Blueprint('pet_info', __name__)

@pet_info.route('/pets', methods=['GET', 'POST'])
def pets():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new pet
    if request.method == 'POST':
        pet_name = request.form['pet_name']
        pet_type = request.form['pet_type']
        price = request.form['price']

        # Insert the new pet info into the database
        cursor.execute('INSERT INTO pet_info (pet_name, pet_type, price) VALUES (%s, %s, %s)',
                       (pet_name, pet_type, price))
        db.commit()

        flash('New pet information added successfully!', 'success')
        return redirect(url_for('pet_info.pets'))

    # Handle GET request to display all pets
    cursor.execute('SELECT * FROM pet_info')
    all_pets = cursor.fetchall()
    return render_template('pet_info.html', all_pets=all_pets)

@pet_info.route('/update_pet/<int:pet_id>', methods=['GET', 'POST'])
def update_pet(pet_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        # Update the pet's details
        pet_name = request.form['pet_name']
        pet_type = request.form['pet_type']
        price = request.form['price']

        cursor.execute('UPDATE pet_info SET pet_name = %s, pet_type = %s, price = %s WHERE pet_id = %s',
                       (pet_name, pet_type, price, pet_id))
        db.commit()

        flash('Pet updated successfully!', 'success')
        return redirect(url_for('pet_info.pets'))

    # GET method: fetch pet's current data for pre-populating the form
    cursor.execute('SELECT * FROM pet_info WHERE pet_id = %s', (pet_id,))
    current_pet_info = cursor.fetchone()
    return render_template('update_pet.html', current_pet_info=current_pet_info)

@pet_info.route('/delete_pet/<int:pet_id>', methods=['POST'])
def delete_pet(pet_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the pet
    cursor.execute('DELETE FROM pet_info WHERE pet_id = %s', (pet_id,))
    db.commit()

    flash('Pet deleted successfully!', 'danger')
    return redirect(url_for('pet_info.pets'))
