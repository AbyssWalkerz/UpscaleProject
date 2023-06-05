from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .api.routes import api
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        """
        Hello World first API for testing

        Returns:
            str: simply hello world message
        """
        return 'Hello, World!'

    app.register_blueprint(api)
    
    return app
