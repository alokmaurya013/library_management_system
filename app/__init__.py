from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Migrate
from .config import Config

# Create instances of SQLAlchemy and Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    
    # Load configuration from Config class
    app.config.from_object(Config)
    
    # Initialize the database and migration objects with the app
    db.init_app(app)
    migrate.init_app(app, db)  # Bind Migrate to the app and db
    
    # Import and configure routes
    from .views import configure_routes
    configure_routes(app)
    
    # Return the app instance
    return app
