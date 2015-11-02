

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.debugtoolbar import DebugToolbarExtension

db = SQLAlchemy()
login_manager = LoginManager()
debug_toolbar = DebugToolbarExtension()


def configure_extensions(app):
    """ Registers all relevant extensions. """

    db.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)

    return None
