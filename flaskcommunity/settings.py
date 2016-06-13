

import os


class AppConfig(object):
    DEBUG = True
    SITE_NAME = os.environ.get('FC_SITE_NAME', 'Flask Community')
    SECRET_KEY = os.environ.get('FC_SECRET_KEY', 'ThisIsJustTheDevKey')
    SQLALCHEMY_DATABASE_URI = os.environ.get('FC_SQLA_URI', 'postgres://user:pass@192.168.99.100:32768/fc')
    AUTH_BACKENDS = [module for module in os.environ.get('FC_AUTH_BACKENDS', '').split(',')]
    DEBUG_TB_INTERCEPT_REDIRECTS = True

    # OAuth2 settings for auth backends
    EVEONLINE = {
        'consumer_key': os.environ.get('FC_AUTH_EVE_KEY'),
        'consumer_secret': os.environ.get('FC_AUTH_EVE_SECRET'),
        'base_url': 'https://login.eveonline.com/',
        'access_token_url': 'https://login.eveonline.com/oauth/token',
        'access_token_method': 'POST',
        'authorize_url': 'https://login.eveonline.com/oauth/authorize',
    }

    BATTLENET = {
        'consumer_key': os.environ.get('FC_AUTH_BATTLENET_KEY'),
        'consumer_secret': os.environ.get('FC_AUTH_BATTLENET_SECRET'),
        'base_url': 'https://eu.battle.net/',
        'access_token_url': 'https://eu.battle.net/oauth/token',
        'access_token_method': 'POST',
        'authorize_url': 'https://eu.battle.net/oauth/authorize',
    }
