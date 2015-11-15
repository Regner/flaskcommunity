

from flaskcommunity.auth.backends import eveonline
from flaskcommunity.auth.models import UserModel
from flaskcommunity.extentions import login_manager


def configure_auth_backends(app):
    auth_backends = {
        'eveonline': eveonline,
    }

    if len(app.config['AUTH_WHITELIST']) > 1 and app.config['AUTH_WHITELIST'] is not '':
        for backend in auth_backends:
            if backend not in app.config['AUTH_WHITELIST']:
                del auth_backends[backend]

    if len(app.config['AUTH_BLACKLIST']) > 1 and app.config['AUTH_BLACKLIST'] is not '':
        for backend in app.config['AUTH_BLACKLIST']:
            if backend in auth_backends:
                del auth_backends[backend]

    app.config['auth_backends'] = auth_backends

    for name, backend in auth_backends.iteritems():
        app.register_blueprint(backend.blueprint)


@login_manager.user_loader
def load_user(user_id):
    """ Required callback for Flask-Login. Returns the user DB object or None. """

    user = UserModel.query.filter_by(game=user_id.game, character_id=user_id.character_id).first()

    return user