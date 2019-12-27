from flask import Flask
from .blockchain import Blockchain
from uuid import uuid4

from .config import ProductionConfig, DevelopmentConfig

node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()

app = Flask(__name__, instance_relative_config=False)

def create_app():

    app.config.from_object(DevelopmentConfig)

    with app.app_context():

        from . import routes

        return app