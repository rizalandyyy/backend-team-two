from models import *
from config.settings import create_app
from instance.database import db

app = create_app("config.local")
