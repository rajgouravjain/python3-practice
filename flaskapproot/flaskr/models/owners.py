from models import db, login_manager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Owner.query.get(user_id)


class Owner(db.Model,UserMixin):
    __tablename__ = 'owners'
    id = db.Column(db.Integer(),primary_key=True)
    email = db.Column(db.String(60))
    name = db.Column(db.String(64))
    password = db.Column(db.String(128))


    def __init(self,name,email,password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
    def __repr__(self):
        return {'name': self.name, 'email' : self.email}
    def __str__(self):
        return f"User {self.name} has Email {self.email}"
    def json(self):
        return {'name': self.name, 'email' : self.email }
    def check_password(self,password):
        return check_password_hash(self.password, password)
