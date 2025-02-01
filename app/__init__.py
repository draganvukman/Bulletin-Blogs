from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from .routes.page_routes import page_routes
    from .routes.user_routes import user_routes

    app.register_blueprint(page_routes, url_prefix='/')
    app.register_blueprint(user_routes, url_prefix='/user')

    with app.app_context():
        from .models import Blog, Message
        db.create_all()

    return app
