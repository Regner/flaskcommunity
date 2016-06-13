

import abc

from flask import session

from flaskcommunity.extentions import oauth


class BaseAuthBackend(object):
    """ Base class for all auth backends. """

    __metaclass__ = abc.ABCMeta

    login_image = 'base.jpg'

    app_name = None
    app_key = None

    def __init__(self):
        print self.app_name
        self.backend_oauth = oauth.remote_app(self.app_name, self.app_key)
        self.backend_oauth._tokengetter = self.tokengetter()

    @abc.abstractmethod
    def handle_callback(self):
        """  """
        return

    @staticmethod
    def tokengetter():
        return session.get('oauth_token')
