

from flaskcommunity.extentions import oauth
from flaskcommunity.auth.backends.base import BaseAuthBackend


class EVEOnlineAuthBackend(BaseAuthBackend):
    """ EVE Online authentication implementation. """

    login_image = 'eveonline.png'

    def __init__(self):
        self.oauth = oauth.remote_app('eveonline', app_key='EVEONLINE')
