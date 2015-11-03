

from flask import Blueprint, render_template, current_app, url_for

blueprint = Blueprint('auth', __name__, static_folder='../static', url_prefix='/auth')


@blueprint.route('/')
def login():
    login_info = []

    for name, backend in current_app.config['auth_backends'].iteritems():
        login_info.append({
            'link': backend.oauth.authorize(callback=url_for('public.home', _external=True)),
            'image': url_for('static', filename='img/auth_backends/{}'.format(backend.login_image)),
        })

    context = {
        'login_info': login_info
    }

    return render_template('auth/login.html', context=context)
