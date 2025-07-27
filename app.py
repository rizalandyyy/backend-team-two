import os
from models import *
from config.settings import create_app
from instance.database import db


app = create_app("config.local")
if __name__ == "__main__":
    app.run(debug=True)


app = create_app("config.local")

config_name = os.getenv("FLASK_CONFIG", "config.local")
app = create_app(config_name)
