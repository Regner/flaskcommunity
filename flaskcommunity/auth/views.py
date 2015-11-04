

from flask import Blueprint, render_template, current_app, url_for

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
