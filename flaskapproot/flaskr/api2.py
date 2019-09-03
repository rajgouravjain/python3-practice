from flask_restplus import Api
from flask import Blueprint
import logging
import traceback
import settings
from sqlalchemy.orm.exc import NoResultFound

from apis.pet import ns as ns1
from apis.owner import ns as ns2

logger = logging.getLogger(__name__)

blueprint = Blueprint('api2', __name__, url_prefix='/api/2')
api = Api(blueprint,
    title='Pet Store api v2',
    version='2.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns1,path='/pet')
api.add_namespace(ns2,path='/owner')

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
