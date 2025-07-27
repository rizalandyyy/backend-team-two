import os
from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file

from models import *
from config.settings import create_app
from instance.database import db

config_name = os.getenv("FLASK_CONFIG", "config.local")
app = create_app(config_name)

from sqlalchemy.exc import ProgrammingError
from flask import jsonify

@app.errorhandler(ProgrammingError)
def handle_programming_error(e):
    app.logger.error(f"Database Programming Error: {e}")
    return jsonify({
        "message": "An internal server error occurred due to a database issue. Please try again later. Ensure migrations have been applied."
    }), 500
