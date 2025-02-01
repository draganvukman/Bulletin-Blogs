import os

# Database Configuration
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = 'postgresql://blog_db_e8gl_user:1j4xYoqvb8I7L6BnDLtp19sbG8uMHxn8@dpg-ct87t652ng1s73adnce0-a/blog_db_e8gl'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
