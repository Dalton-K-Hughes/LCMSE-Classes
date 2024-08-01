from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class_info.id'), nullable=False)
    admin = db.Column(db.Boolean, default=False)
    
class ClassInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    users = db.relationship('User', backref='class', lazy=True)
    content = db.relationship('Content', backref='class', lazy=True)
    assignments = db.relationship('Assignment', backref='class', lazy=True)
    

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class_info.id'))

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description=db.Column(db.Text, nullable=False)
    start_date=db.Column(db.DateTime, nullable=False)
    due_date=db.Column(db.DateTime, nullable=False)
    class_id =db.Column(db.Integer, db.ForeignKey('class_info.id'), nullable=False)
    
