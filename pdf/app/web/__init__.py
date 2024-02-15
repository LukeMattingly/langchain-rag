from flask import Flask
from flask_cors import CORS

import os 
from app.web.db import db, init_db_command
from app.web.db import models
from app.celery import celery_init_app
from app.web.config import Config
from app.web.hooks import load_logged_in_user, handle_error, add_headers
from app.web.views import (
    auth_views,
    pdf_views,
    score_views,
    client_views,
    conversation_views,
)


def create_app():
    app = Flask(__name__, static_folder="../../client/build")
    app.url_map.strict_slashes = False
    app.config.from_object(Config)
    # Configure MIME types
    app.config['MIME_TYPES'] = {
        '.js': 'application/javascript',
        # Add other MIME types if needed
    }
    app.static_folder = '../../client/build/static'
    app.static_url_path = '/static'
    app.debug = True

    register_extensions(app)
    register_hooks(app)
    register_blueprints(app)
    # Check if REDIS_URI environment variable is set
    celery_init_app(app)

    return app


def register_extensions(app):
    db.init_app(app)
    app.cli.add_command(init_db_command)


def register_blueprints(app):
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(pdf_views.bp)
    app.register_blueprint(score_views.bp)
    app.register_blueprint(conversation_views.bp)
    app.register_blueprint(client_views.bp)


def register_hooks(app):
    CORS(app)
    app.before_request(load_logged_in_user)
    app.after_request(add_headers)
    app.register_error_handler(Exception, handle_error)
