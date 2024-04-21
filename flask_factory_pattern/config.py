import os
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine


basedir = os.path.dirname(os.path.abspath(__file__))

class Config:
    SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_recycle': 280,
    'pool_pre_ping': True
    }
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=URL.create(
        os.environ.get('DRIVER'), 
        username=os.environ.get('USERNAME'),
        password=os.environ.get('PASSWORD'),
        host=os.environ.get('HOST'),
        port=os.environ.get('PORT'),
        database=os.environ.get('DATABASE')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTPLUS_MASK_SWAGGER = False



