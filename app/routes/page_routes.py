from flask import Blueprint, render_template

page_routes = Blueprint('page_routes', __name__)

@page_routes.route('/')
def home():
    return render_template('index.html')

@page_routes.route('/business')
def business():
    return render_template('business.html')

@page_routes.route('/technology')
def technology():
    return render_template('technology.html')

@page_routes.route('/health')
def health():
    return render_template('health.html')

@page_routes.route('/authors')
def authors():
    return render_template('authors.html')

@page_routes.route('/contact')
def contact():
    return render_template('contact-us.html')