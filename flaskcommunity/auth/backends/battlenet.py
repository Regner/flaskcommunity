

from datetime import datetime

from flask import Blueprint, redirect, url_for, request, session

from flask.ext.login import login_user

from flaskcommunity.extentions import oauth, db
from flaskcommunity.auth.models import UserModel

blueprint = Blueprint('battlenet', __name__, static_folder='../static', url_prefix='/auth/battlenet')
oauth = oauth.remote_app('battlenet', app_key='BATTLENET')
login_image = 'img/auth_backends/battlenet.png'


@blueprint.route('/login')
def login():
    return oauth.authorize(callback=url_for('battlenet.callback', _external=True))


@blueprint.route('/callback')
def callback():
    resp = oauth.authorized_response()

    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error'],
            request.args['error_description']
        )

    if isinstance(resp, Exception):
        return 'Access denied: error=%s' % str(resp)

    session['oauth_token'] = (resp['access_token'], '')

    fetch_all_names()
    #
    # user = UserModel.query.filter_by(game='eveonline', character_id=verify.data['CharacterID']).first()
    #
    # if user is None:
    #     user = UserModel('eveonline', verify.data['CharacterID'], verify.data['CharacterName'])
    #     user.login_count = 0
    #     user.join_date = datetime.now()
    #
    # user.login_count += 1
    #
    # db.session.add(user)
    # db.session.commit()
    #
    # login_user(user)

    # return redirect(url_for('public.home'))
    pass

@oauth.tokengetter
def get_evesso_oauth_token():
    return session.get('oauth_token')


def fetch_all_names():
    # Account info is global, so lets just go with EU because it's close
    # https://localhost:8080/auth/battlenet/login
    oauth.base_url = 'https://eu.api.battle.net'
    account_data = oauth.get('account/user')
