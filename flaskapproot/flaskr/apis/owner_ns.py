from flask_restplus import Namespace, Resource, fields
from models.owners import Owner

ns = Namespace('Owners', description='Owners related operations')

owner = ns.model('Owner', {
    'id': fields.String(required=True, description='The owner identifier'),
    'name': fields.String(required=True, description='The owner name'),
})

#OWNERS = [
#    {'id': 'felix', 'name': 'Felix'},
#]

@ns.route('/')
class OwnerListResource(Resource):
    @ns.doc('list_owners')
    @ns.marshal_list_with(owner)
    def get(self):
        '''List all owners'''
        OWNERS = Owner.query.all()
        return OWNERS

@ns.route('/<id>')
@ns.param('id', 'The owner identifier')
@ns.response(404, 'Owners not found')
class OwnerResource(Resource):
    @ns.doc('get_owner')
    @ns.marshal_with(owner)
    def get(self, id):
        '''Fetch a owner given its identifier'''
        owner = Owner.query.filter_by(id=id).first()
        return owner
        ns.abort(404)
