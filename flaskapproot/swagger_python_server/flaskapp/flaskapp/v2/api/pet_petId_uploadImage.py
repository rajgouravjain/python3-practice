# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class PetPetidUploadimage(Resource):

    def post(self, petId):
        print(g.form)

        return {}, 200, None