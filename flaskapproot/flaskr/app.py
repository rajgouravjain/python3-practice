from flask import Flask
from api1 import blueprint as api1
from api2 import blueprint as api2
from ui.owner import blueprint as owner
from ui.pet import blueprint as pet
from flask_migrate import Migrate
from models import db, login_manager
import settings
import logging.config
import os
import os.path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt import JWT
from security_check import authenticate,  identity

flask_app = Flask(__name__)


logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
flask_app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///' + os.path.join(basedir, 'data.sqlite')
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
flask_app.config['SECRET_KEY'] = 'mysecretkey'
def configure_app(flask_app):
    basedir = os.path.abspath(os.path.dirname(__file__))
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['SECRET_KEY'] = 'mysecretkey'
def initialize_app(flask_app):
    configure_app(flask_app)
    jwt = JWT(flask_app, authenticate, identity)
    flask_app.register_blueprint(api1)
    flask_app.register_blueprint(api2)
    flask_app.register_blueprint(owner)
    flask_app.register_blueprint(pet)
    db.init_app(flask_app)

    login_manager.init_app(flask_app)
    logger.info("Logger for flask initialized")
    #migrate = Migrate(app,db)



Migrate(flask_app,db)
if __name__ == '__main__':
    initialize_app(flask_app)
    flask_app.run(debug=True)
