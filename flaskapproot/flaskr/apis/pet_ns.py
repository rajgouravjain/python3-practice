from flask_restplus import Namespace, Resource, fields

from models.pets import Pet

ns = Namespace('pets', description='Pets related operations')

pet = ns.model('Pet', {
    'id': fields.String(required=True, description='The pet identifier'),
    'name': fields.String(required=True, description='The pet name'),
})

#PETS = [
#    {'id': 'felix', 'name': 'Felix'},
#]

@ns.route('/')
class PetListResource(Resource):
    @ns.doc('list_pets')
    @ns.marshal_list_with(pet)
    def get(self):
        '''List all pets'''
        PETS = Pet.query.all()
        return PETS

@ns.route('/<id>')
@ns.param('id', 'The pet identifier')
@ns.response(404, 'Pet not found')
class PetResource(Resource):
    @ns.doc('get_pet')
    @ns.marshal_with(pet)
    def get(self, id):
        '''Fetch a pet given its identifier'''
        cd
        ns.abort(404)
