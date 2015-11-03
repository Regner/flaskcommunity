

import os


class AppConfig(object):
    DEBUG = True
    SITE_NAME = os.environ.get('FC_SITE_NAME', 'Flask Community')
    SECRET_KEY = os.environ.get('FC_SECRET_KEY', 'ThisIsJustTheDevKey')
    SQLALCHEMY_DATABASE_URI = os.environ.get('FC_SECRET_KEY', 'sqlite:///fc.db')
    AUTH_WHITELIST = [module for module in os.environ.get('FC_AUTH_WHITELIST', '').split(',')]
    AUTH_BLACKLIST = [module for module in os.environ.get('FC_AUTH_BLACKLIST', '').split(',')]

    # OAuth2 settings for auth backends
    EVEONLINE = {
        'consumer_key': '56ef03e322fd422aab074c3cc90c3d01',
        'consumer_secret': 'hfYxgV1EyYlH143bZcCBoXJw64v8u8AccAIBljQ4',
        'base_url': 'https://login.eveonline.com/oauth/',
        'access_token_url': 'https://login.eveonline.com/oauth/token',
        'access_token_method': 'POST',
        'authorize_url': 'https://login.eveonline.com/oauth/authorize',
    }



