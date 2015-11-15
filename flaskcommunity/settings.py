

import os


class AppConfig(object):
    DEBUG = True
    SITE_NAME = os.environ.get('FC_SITE_NAME', 'Flask Community')
    SECRET_KEY = os.environ.get('FC_SECRET_KEY', 'ThisIsJustTheDevKey')
    SQLALCHEMY_DATABASE_URI = os.environ.get('FC_SQLA_URI', 'sqlite:///fc.db')
    AUTH_WHITELIST = [module for module in os.environ.get('FC_AUTH_WHITELIST', '').split(',')]
    AUTH_BLACKLIST = [module for module in os.environ.get('FC_AUTH_BLACKLIST', '').split(',')]
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # OAuth2 settings for auth backends
    EVEONLINE = {
        'consumer_key': os.environ.get('FC_AUTH_EVE_KEY'),
        'consumer_secret': os.environ.get('FC_AUTH_EVE_SECRET'),
        'base_url': 'https://login.eveonline.com/oauth/',
        'access_token_url': 'https://login.eveonline.com/oauth/token',
        'access_token_method': 'POST',
        'authorize_url': 'https://login.eveonline.com/oauth/authorize',
    }
