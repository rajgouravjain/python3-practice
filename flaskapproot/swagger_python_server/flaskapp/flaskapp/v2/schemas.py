# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v2'


DefinitionsOrder = {'type': 'object', 'properties': {'quantity': {'type': 'integer', 'format': 'int32'}, 'complete': {'type': 'boolean', 'default': False}, 'shipDate': {'type': 'string', 'format': 'date-time'}, 'petId': {'type': 'integer', 'format': 'int64'}, 'id': {'type': 'integer', 'format': 'int64'}, 'status': {'type': 'string', 'enum': ['placed', 'approved', 'delivered'], 'description': 'Order Status'}}, 'xml': {'name': 'Order'}}
DefinitionsCategory = {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64'}, 'name': {'type': 'string'}}, 'xml': {'name': 'Category'}}
DefinitionsApiresponse = {'type': 'object', 'properties': {'code': {'type': 'integer', 'format': 'int32'}, 'message': {'type': 'string'}, 'type': {'type': 'string'}}}
DefinitionsTag = {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64'}, 'name': {'type': 'string'}}, 'xml': {'name': 'Tag'}}
DefinitionsUser = {'type': 'object', 'properties': {'password': {'type': 'string'}, 'phone': {'type': 'string'}, 'lastName': {'type': 'string'}, 'username': {'type': 'string'}, 'firstName': {'type': 'string'}, 'email': {'type': 'string'}, 'id': {'type': 'integer', 'format': 'int64'}, 'userStatus': {'description': 'User Status', 'type': 'integer', 'format': 'int32'}}, 'xml': {'name': 'User'}}
DefinitionsPet = {'required': ['name', 'photoUrls'], 'type': 'object', 'properties': {'tags': {'type': 'array', 'items': DefinitionsTag, 'xml': {'name': 'tag', 'wrapped': True}}, 'photoUrls': {'type': 'array', 'items': {'type': 'string'}, 'xml': {'name': 'photoUrl', 'wrapped': True}}, 'id': {'type': 'integer', 'format': 'int64'}, 'name': {'type': 'string', 'example': 'doggie'}, 'status': {'type': 'string', 'enum': ['available', 'pending', 'sold'], 'description': 'pet status in the store'}, 'category': DefinitionsCategory}, 'xml': {'name': 'Pet'}}

validators = {
    ('pet_petId_uploadImage', 'POST'): {'form': {'required': [], 'properties': {'file': {'required': False, 'description': 'file to upload', 'type': 'file'}, 'additionalMetadata': {'required': False, 'description': 'Additional data to pass to server', 'type': 'string'}}}},
    ('pet_findByStatus', 'GET'): {'args': {'required': ['status'], 'properties': {'status': {'type': 'array', 'items': {'type': 'string', 'default': 'available', 'enum': ['available', 'pending', 'sold']}, 'description': 'Status values that need to be considered for filter', 'collectionFormat': 'multi'}}}},
    ('user_createWithArray', 'POST'): {'json': {'type': 'array', 'items': DefinitionsUser}},
    ('user_createWithList', 'POST'): {'json': {'type': 'array', 'items': DefinitionsUser}},
    ('pet_findByTags', 'GET'): {'args': {'required': ['tags'], 'properties': {'tags': {'type': 'array', 'items': {'type': 'string'}, 'description': 'Tags to filter by', 'collectionFormat': 'multi'}}}},
    ('user_login', 'GET'): {'args': {'required': ['username', 'password'], 'properties': {'password': {'description': 'The password for login in clear text', 'type': 'string'}, 'username': {'description': 'The user name for login', 'type': 'string'}}}},
    ('user_username', 'PUT'): {'json': DefinitionsUser},
    ('pet_petId', 'POST'): {'form': {'required': [], 'properties': {'name': {'required': False, 'description': 'Updated name of the pet', 'type': 'string'}, 'status': {'required': False, 'description': 'Updated status of the pet', 'type': 'string'}}}},
    ('pet_petId', 'DELETE'): {'headers': {'required': [], 'properties': {'api_key': {'required': False, 'type': 'string'}}}},
    ('store_order', 'POST'): {'json': DefinitionsOrder},
    ('user', 'POST'): {'json': DefinitionsUser},
    ('pet', 'POST'): {'json': DefinitionsPet},
    ('pet', 'PUT'): {'json': DefinitionsPet},
}

filters = {
    ('user_logout', 'GET'): {},
    ('store_inventory', 'GET'): {200: {'schema': {'type': 'object', 'additionalProperties': {'type': 'integer', 'format': 'int32'}}, 'headers': None}},
    ('pet_petId_uploadImage', 'POST'): {200: {'schema': DefinitionsApiresponse, 'headers': None}},
    ('pet_findByStatus', 'GET'): {200: {'schema': {'type': 'array', 'items': DefinitionsPet}, 'headers': None}, 400: {'schema': None, 'headers': None}},
    ('store_order_orderId', 'GET'): {200: {'schema': DefinitionsOrder, 'headers': None}, 400: {'schema': None, 'headers': None}, 404: {'schema': None, 'headers': None}},
    ('store_order_orderId', 'DELETE'): {400: {'schema': None, 'headers': None}, 404: {'schema': None, 'headers': None}},
    ('user_createWithArray', 'POST'): {},
    ('user_createWithList', 'POST'): {},
    ('pet_findByTags', 'GET'): {200: {'schema': {'type': 'array', 'items': DefinitionsPet}, 'headers': None}, 400: {'schema': None, 'headers': None}},
    ('user_login', 'GET'): {200: {'schema': {'type': 'string'}, 'headers': {'X-Expires-After': {'description': 'date in UTC when token expires', 'type': 'string', 'format': 'date-time'}, 'X-Rate-Limit': {'description': 'calls per hour allowed by the user', 'type': 'integer', 'format': 'int32'}}}, 400: {'schema': None, 'headers': None}},
    ('user_username', 'GET'): {200: {'schema': DefinitionsUser, 'headers': None}, 400: {'schema': None, 'headers': None}, 404: {'schema': None, 'headers': None}},
    ('user_username', 'DELETE'): {400: {'schema': None, 'headers': None}, 404: {'schema': None, 'headers': None}},
    ('user_username', 'PUT'): {400: {'schema': None, 'headers': None}, 404: {'schema': None, 'headers': None}},
    ('pet_petId', 'POST'): {405: {'schema': None, 'headers': None}},
    ('pet_petId', 'GET'): {200: {'schema': DefinitionsPet, 'headers': None}, 400: {'schema': None, 'headers': None}, 404: {'schema': None, 'headers': None}},
    ('pet_petId', 'DELETE'): {400: {'schema': None, 'headers': None}, 404: {'schema': None, 'headers': None}},
    ('store_order', 'POST'): {200: {'schema': DefinitionsOrder, 'headers': None}, 400: {'schema': None, 'headers': None}},
    ('user', 'POST'): {},
    ('pet', 'POST'): {405: {'schema': None, 'headers': None}},
    ('pet', 'PUT'): {400: {'schema': None, 'headers': None}, 404: {'schema': None, 'headers': None}, 405: {'schema': None, 'headers': None}},
}

scopes = {
    ('store_inventory', 'GET'): [],
    ('pet_petId_uploadImage', 'POST'): ['write:pets', 'read:pets'],
    ('pet_findByStatus', 'GET'): ['write:pets', 'read:pets'],
    ('pet_findByTags', 'GET'): ['write:pets', 'read:pets'],
    ('pet_petId', 'POST'): ['write:pets', 'read:pets'],
    ('pet_petId', 'GET'): [],
    ('pet_petId', 'DELETE'): ['write:pets', 'read:pets'],
    ('pet', 'POST'): ['write:pets', 'read:pets'],
    ('pet', 'PUT'): ['write:pets', 'read:pets'],
}


class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None):

    import six

    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, dict):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize(schema, data):
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
        }
        type_ = schema.get('type', 'object')
        if not type_ in funcs:
            type_ = 'default'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors

