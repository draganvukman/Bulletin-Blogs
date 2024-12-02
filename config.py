import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1103@localhost/blog_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
