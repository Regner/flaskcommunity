

import os


class AppConfig(object):
    DEBUG = True
    SITE_NAME = os.environ.get('FC_SITE_NAME', 'Flask Community')
    SECRET_KEY = os.environ.get('FC_SECRET_KEY', 'ThisIsJustTheDevKey')
    SQLALCHEMY_DATABASE_URI = os.environ.get('FC_SECRET_KEY', 'sqlite:///fc.db')
    AUTH_WHITELIST = [module for module in os.environ.get('FC_AUTH_WHITELIST', '').split(',')]
    AUTH_BLACKLIST = [module for module in os.environ.get('FC_AUTH_BLACKLIST', '').split(',')]



