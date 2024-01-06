import os
from dotenv import load_dotenv

class Config:

    load_dotenv()
  
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ['DB_CONNECTION_STRING'] or 'sqlite:///' + os.path.join(basedir, 'app.db')
    #SQLALCHEMY_DATABASE_URI = os.environ['DB_CONNECTION_STRING']