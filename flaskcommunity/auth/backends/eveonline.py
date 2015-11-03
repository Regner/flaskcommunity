

from flask import Blueprint, redirect, url_for, request, session

from flaskcommunity.extentions import oauth

blueprint = Blueprint('eveonline', __name__, static_folder='../static', url_prefix='/auth/eveonline')
oauth = oauth.remote_app('eveonline', app_key='EVEONLINE')
login_image = 'eveonline.png'


@blueprint.route('/login')
def login():
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

    session['evesso_token'] = (resp['access_token'], '')
    verify = oauth.get('verify')

    user = UserModel.query.filter_by(id=verify.data['CharacterID']).first()

    if user is None:
        user = UserModel(verify.data['CharacterID'], verify.data['CharacterName'], verify.data['CharacterOwnerHash'])
        user.login_count = 0
        user.join_date   = datetime.now()

    user.login_count += 1

    db.session.add(user)
    db.session.commit()

    login_user(user)

    return redirect(url_for('public.home'))
