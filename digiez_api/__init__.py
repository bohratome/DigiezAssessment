import logging
from logging import FileHandler
from flask import Flask, request, json
from digiez_api.views import *
from digiez_api.extensions import db


def create_app(config_module):
    # Create app and set config
    app_ = Flask(__name__)
    app_.config.from_object(config_module)
    # Init DB
    db.init_app(app_)
    # Blueprints
    # TODO: automate blueprint loading ? (for loop with package attr)
    app_.register_blueprint(api_accounts.api_accounts)
    app_.register_blueprint(api_malls.api_malls)
    app_.register_blueprint(api_units.api_units)
    return app_


# Create Flask app
app = create_app('config')

@app.before_first_request
def setup_tables_db():
    db.create_all()
    db.session.commit()