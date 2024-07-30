import os
from flask import Flask
from flask_login import LoginManager
from .init_db import db, init_db
from .config import DevelopmentConfig, TestingConfig, ProductionConfig
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap5

csrf = CSRFProtect()
bootstrap = Bootstrap5()
login_manager = LoginManager()

def create_app():
    # Create and configure the app
    app = Flask(__name__)
    csrf.init_app(app)
    bootstrap.init_app(app)
    # Choose configuration based on environment variable
    config_type = os.getenv('FLASK_CONFIG', 'development')
    if config_type == 'production':
        app.config.from_object('website.config.ProductionConfig')
    elif config_type == 'testing':
        app.config.from_object('website.config.TestingConfig')
    else:
        app.config.from_object('website.config.DevelopmentConfig')

    # Initialize the database
    #init_db(app)


    # Import the views in our app
    from .views import views
    from .auth import auth
    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    # Register the blueprints with our app with appropriate url_prefixes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()