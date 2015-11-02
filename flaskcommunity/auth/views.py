

from flask import Blueprint, render_template

blueprint = Blueprint('auth', __name__, static_folder='../static', url_prefix='/auth')


@blueprint.route('/')
def login():
    return render_template('public/home.html')
