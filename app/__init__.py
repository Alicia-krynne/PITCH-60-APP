from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options

db = SQLAlchemy()
bootstrap = Bootstrap()


# Initializing application
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    db.init_app(app)
    bootstrap.init_app(app)
    



    return app