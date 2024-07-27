import os
from flask import Flask
from .init_db import db, init_db
from .config import DevelopmentConfig, TestingConfig, ProductionConfig

def create_app():
    # Create and configure the app
    app = Flask(__name__)

    # Choose configuration based on environment variable
    config_type = os.getenv('FLASK_CONFIG', 'development')
    if config_type == 'production':
        app.config.from_object('LCMSE-Classes.config.ProductionConfig')
    elif config_type == 'testing':
        app.config.from_object('LCMSE-Classes.config.TestingConfig')
    else:
        app.config.from_object('LCMSE-Classes.config.DevelopmentConfig')

    # Initialize the database
    init_db(app)

    # Import the views in our app
    from .views import views
    from .auth import auth

    # Register the blueprints with our app with appropriate url_prefixes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app