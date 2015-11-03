

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.oauthlib.client import OAuth

db = SQLAlchemy()
login_manager = LoginManager()
debug_toolbar = DebugToolbarExtension()
oauth = OAuth()


def configure_extensions(app):
    """ Registers all relevant extensions. """

    db.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    oauth.init_app(app)

    return None
