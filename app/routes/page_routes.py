from flask import Blueprint, render_template
from app.models import Blog

page_routes = Blueprint('page_routes', __name__)

@page_routes.route('/')
def home():
    # Fetch blogs for each category
    business_blogs = Blog.query.filter_by(category='Business').all()
    health_blogs = Blog.query.filter_by(category='Health').all()
    technology_blogs = Blog.query.filter_by(category='Technology').all()

    return render_template('index.html', 
                           business_blogs=business_blogs,
                           health_blogs=health_blogs,
                           technology_blogs=technology_blogs)

@page_routes.route('/business')
def business():
    # Fetch blogs for business category
    business_blogs = Blog.query.filter_by(category='Business').all()
    return render_template('business.html', business_blogs=business_blogs)

@page_routes.route('/technology')
def technology():
    # Fetch blogs for technology category
    technology_blogs = Blog.query.filter_by(category='Technology').all()
    return render_template('technology.html', technology_blogs=technology_blogs)

@page_routes.route('/health')
def health():
    # Fetch blogs for health category
    health_blogs = Blog.query.filter_by(category='Health').all()
    return render_template('health.html', health_blogs=health_blogs)

@page_routes.route('/authors')
def authors():
    return render_template('authors.html')

@page_routes.route('/contact')
def contact():
    return render_template('contact-us.html')
