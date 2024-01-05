from . import db
from flask_login import UserMixin

class users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    photo = db.Column(db.String(200), nullable=False)
    mail = db.Column(db.String(30), nullable=False, unique=True)
    about = db.Column(db.String(200))
    def __repr__(self):
        return f'id:{self.id}, username:{self.username}, mail:{self.mail}'

class articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), db.ForeignKey('users.username'), nullable=False, unique=True)
    mail = db.Column(db.String(30), nullable=False, unique=True)
    title = db.Column(db.String(50), nullable=False)
    article_text = db.Column(db.Text, nullable=False)
    