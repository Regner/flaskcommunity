

import os

from datetime import datetime

from flask import Blueprint, redirect, url_for, request, session, current_app

from flaskcommunity.extentions import oauth, db
from flaskcommunity.auth.models import UserModel

current_app.config['EVEONLINE'] = {
    'consumer_key': os.environ.get('FC_AUTH_EVE_KEY'),
    'consumer_secret': os.environ.get('FC_AUTH_EVE_SECRET'),
    'base_url': 'https://login.eveonline.com/oauth/',
    'access_token_url': 'https://login.eveonline.com/oauth/token',
    'access_token_method': 'POST',
    'authorize_url': 'https://login.eveonline.com/oauth/authorize',
}

blueprint = Blueprint('eveonline', __name__, static_folder='../static', url_prefix='/auth/eveonline')
oauth = oauth.remote_app('eveonline', app_key='EVEONLINE')
login_image = 'img/auth_backends/eveonline.png'


def get_image_server_link(character_id):
    return 'https://imageserver.eveonline.com/Character/{}_128.jpg'.format(character_id)


@blueprint.route('/login')
def login():
    print url_for('eveonline.callback', _external=True)
    return oauth.authorize(callback=url_for('eveonline.callback', _external=True))


@blueprint.route('/callback')
def callback():
    resp = oauth.authorized_response()

    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )

    if isinstance(resp, Exception):
        return 'Access denied: error=%s' % str(resp)

    session['oauth_token'] = (resp['access_token'], '')
    verify = oauth.get('verify')

    user = UserModel.query.filter_by(game='eveonline', character_id=verify.data['CharacterID']).first()

    if user is None:
        user = UserModel('eveonline', verify.data['CharacterID'], verify.data['CharacterName'])
        user.login_count = 0
        user.join_date = datetime.now()

    user.login_count += 1

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('public.home'))

@oauth.tokengetter
def get_evesso_oauth_token():
    return session.get('oauth_token')