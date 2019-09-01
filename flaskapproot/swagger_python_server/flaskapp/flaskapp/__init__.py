# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import v2


def create_app():
    ##def create_app(config_file):
    app = Flask(__name__, static_folder='static')
    ##app.config.from_pyfile(config_file)
    app.register_blueprint(v2.bp, url_prefix='/v2')
    return app

if __name__ == '__main__':
    create_app().run(debug=True)