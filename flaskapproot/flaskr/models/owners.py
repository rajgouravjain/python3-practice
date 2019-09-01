from models import db
from flask_sqlalchemy import SQLAlchemy


class Owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(64))


    def __init(self,name):
        self.name = name
    def __repr__(self):
        return {'name': self.name}
    def json(self):
        return {'name': self.name }
