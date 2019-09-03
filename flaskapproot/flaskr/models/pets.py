from models import db
class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(64))
    breed = db.Column(db.String(10))


    def __init(self,name,breed):
        self.name = name
        self.breed = breed
    def __repr__(self):
        return {'name': self.name, 'breed': self.breed }
    def json(self):
        return {'name': self.name, 'breed' : self.breed }
