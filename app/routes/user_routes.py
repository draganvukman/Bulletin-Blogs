from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import ContactForm
from app.models import Message, db

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        message = Message(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(message)
        db.session.commit()
        flash('Message sent successfully!', 'success')
        return redirect(url_for('user_routes.contact'))
    return render_template('contact.html', form=form)
