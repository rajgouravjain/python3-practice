from flask_restplus import Api
from flask import Blueprint
import traceback
import logging
import settings
from sqlalchemy.orm.exc import NoResultFound
from apis.pet_ns import ns as ns1


logger = logging.getLogger(__name__)

blueprint = Blueprint('api1', __name__, url_prefix='/api/1')
api = Api(blueprint,
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns1,path='/pet')

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A models result was required but none was found.'}, 404
