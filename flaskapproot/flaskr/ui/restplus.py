from flask import Blueprint

pet_blueprint = Blueprint(name='Pet', import_name='Pet',url_prefix='/pet',template_folder='ui/templates')


owner_blueprint = Blueprint(name='Owner', import_name='Owner',url_prefix='/owner',template_folder='ui/templates')
