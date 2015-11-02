

from flask import Flask

# Configuration
from flaskcommunity.settings import AppConfig
from flaskcommunity.extentions import configure_extensions
from flaskcommunity.utils.context_processors import configure_context_processors
from flaskcommunity.auth import configure_auth_backends

# Blueprints
from flaskcommunity.public import views as public_views
from flaskcommunity.auth import views as auth_views


def create_app():
    """ Creates the app. """

    app = Flask(__name__)
    app.config.from_object(AppConfig)

    configure_blueprints(app)
    configure_extensions(app)
    configure_context_processors(app)
    configure_auth_backends(app)

    return app


def configure_blueprints(app):
    """ Registers all relevant blueprints. """

    app.register_blueprint(public_views.blueprint)
    app.register_blueprint(auth_views.blueprint)

    return None
