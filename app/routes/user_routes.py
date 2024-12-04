from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import ContactForm
from app.models import Message, db

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Extract data from the form submission
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Create a new Message object
        new_message = Message(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        # Save the new message to the database
        db.session.add(new_message)
        db.session.commit()

        # Provide feedback to the user
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('user_routes.contact'))

    # Render the contact page
    return render_template('contact-us.html')
