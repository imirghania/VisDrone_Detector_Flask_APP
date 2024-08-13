import os
from dotenv import load_dotenv
load_dotenv()

# BASEDIR = os.path.abspath(os.path.dirname(__file__))
# SECRET_KEY = os.getenv('SECRET_KEY')

class Config:
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.getenv('SECRET_KEY')
    MODEL_NAME = os.getenv('MODEL_NAME')


config = Config()