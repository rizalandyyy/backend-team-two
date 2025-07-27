from models import *
from config.settings import create_app
from instance.database import db


app = create_app("config.local")
if __name__ == "__main__":
    app.run(debug=True)


app = create_app("config.local")
