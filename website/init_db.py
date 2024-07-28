from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy and assign it to the variable db
db = SQLAlchemy()

# Create the database for the application
def init_db(app):
    db.init_app(app)

    # Import all models from the models file to represent our tables in the db
    from .models import User

    # Create all tables for the database
    with app.app_context():
        db.create_all()
        db.session.commit()