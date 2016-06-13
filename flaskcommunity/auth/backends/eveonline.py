

from datetime import datetime

from flask import request, session

from flask.ext.login import login_user

from flaskcommunity.extentions import oauth, db
from flaskcommunity.auth.models import UserModel
from flaskcommunity.auth.backends.base import BaseAuthBackend


class EveOnlineAuthBackend(BaseAuthBackend):
    login_image = 'img/auth_backends/eveonline.png'
    app_name = 'eveonline'
    app_key = 'EVEONLINE'

    def handle_callback(self):
        resp = self.backend_oauth.authorized_response()

        if resp is None:
            return 'Access denied: reason=%s error=%s' % (
                request.args['error_reason'],
                request.args['error_description']
            )

        if isinstance(resp, Exception):
            return 'Access denied: error=%s' % str(resp)

        session['oauth_token'] = (resp['access_token'], '')
        verify = self.backend_oauth.get('oauth/verify')

        user = UserModel.query.filter_by(game='eveonline', character_id=verify.data['CharacterID']).first()

        if user is None:
            user = UserModel('eveonline', verify.data['CharacterID'], verify.data['CharacterName'])
            user.login_count = 0
            user.join_date = datetime.now()

        user.login_count += 1

        db.session.add(user)
        db.session.commit()

        login_user(user)
