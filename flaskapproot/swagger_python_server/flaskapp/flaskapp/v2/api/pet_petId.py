# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class PetPetid(Resource):

    def get(self, petId):

        return None, 404, None

    def post(self, petId):
        print(g.form)

        return None, 405, None

    def delete(self, petId):
        print(g.headers)

        return None, 404, None