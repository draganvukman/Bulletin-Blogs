import os

# Database Configuration
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = 'postgresql://blog_db_osau_user:BsJaD6lftS02sXDAAVJxzOXqW7W6ie60@dpg-cuf860ogph6c7381h7m0-a/blog_db_osau'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
