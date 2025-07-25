import os
from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file

from models import *
from config.settings import create_app
from instance.database import db

config_name = os.getenv("FLASK_CONFIG", "config.local")
app = create_app(config_name)
