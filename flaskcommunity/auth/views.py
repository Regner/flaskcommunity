

from flask import Blueprint, render_template, current_app, redirect, url_for, abort
from flask.ext.login import logout_user, login_required

from flaskcommunity.extentions import login_manager
from flaskcommunity.auth.models import UserModel
from flaskcommunity.auth.backends import possible_auth_backends

blueprint = Blueprint('auth', __name__, static_folder='../static', url_prefix='/auth')


@blueprint.route('/')
def base_login():
    context = {
        'login_info': [],
    }

    for backend_name, backend in possible_auth_backends.iteritems():
        context['login_info'].append({
            'name': backend_name,
            'image': backend.login_image,
        })

    return render_template('auth/login.html', context=context)


@blueprint.route('/<string:backend_name>/login')
def backend_login(backend_name):
    backend = get_auth_backend(backend_name)
    return backend.backend_oauth.authorize(callback=url_for('auth.callback', backend_name=backend_name, _external=True))


@blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('public.home'))


@blueprint.route('/<string:backend_name>/callback')
def callback(backend_name):
    backend = get_auth_backend(backend_name)
    backend.handle_callback()

    return redirect(url_for('public.home'))


@login_manager.user_loader
def load_user(user_id):
    """ Required callback for Flask-Login. Returns the user DB object or None. """

    user = UserModel.query.filter_by(game=user_id[0], character_id=user_id[1]).first()

    return user


def get_auth_backend(backend_name):
    print backend_name
    print current_app.config['AUTH_BACKENDS']
    # If FC_AUTH_BACKENDS isn't set we assume all backends are valid
    if current_app.config['AUTH_BACKENDS'] == [''] or backend_name in current_app.config['AUTH_BACKENDS']:
        print possible_auth_backends
        if backend_name not in possible_auth_backends:
            abort(404)

        return possible_auth_backends[backend_name]

    abort(404)
