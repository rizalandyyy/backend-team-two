from models import *
from config.settings import create_app
from instance.database import db
from route import register_routes
from route.product_routes import product_bp

app = create_app("config.local")
app.register_blueprint(product_bp)

if __name__ == "__main__":
    app.run(debug=True)

register_routes(app)