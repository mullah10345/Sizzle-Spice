from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    # ...

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    user = relationship("User", back_populates="reviews")
    item = relationship("MenuItem", back_populates="reviews")

class MenuItem(db.Model):
    # ...

    reviews = db.relationship("Review", back_populates="item")

from sqlalchemy import DateTime

class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    # Other fields as needed

#user roles
class User(db.Model):
    # ...

    role = db.Column(db.String(20), nullable=False, default='user')
