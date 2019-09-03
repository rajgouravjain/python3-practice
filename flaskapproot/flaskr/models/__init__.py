from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = "Owner.login"

db = SQLAlchemy()

def reset_database():
    db.drop_all()
    db.create_all()
