from flask import Flask
from werkzeug.utils import cached_property
from flask_restplus import Api, Resource, fields
from parsers import clinical_fields


flask_app = Flask(__name__)
api = Api(app =flask_app, version = '1.0', title="Previd - Diagnostico COVID-19",
        description = "modelo preditivo para detecção de COVID-19 a partir de exame de hemograma")
