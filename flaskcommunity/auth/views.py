

from flask import Blueprint, render_template, current_app, url_for
from flask.ext.login import login_user, logout_user

from flaskcommunity.extentions import login_manager
from flaskcommunity.auth.models import UserModel

blueprint = Blueprint('auth', __name__, static_folder='../static', url_prefix='/auth')


@blueprint.route('/')
def login():
    context = {
        'login_info': [],
    }

    for name, backend in current_app.config['auth_backends'].iteritems():
        context['login_info'].append({
            'link': '{}.login'.format(name),
            'image': backend.login_image,
        })

    return render_template('auth/login.html', context=context)


@login_manager.user_loader
def load_user(user_id):
    """ Required callback for Flask-Login. Returns the user DB object or None. """

    user = UserModel.query.filter_by(user_id=user_id).first()

    return user