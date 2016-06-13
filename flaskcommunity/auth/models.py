

from collections import namedtuple

from flaskcommunity.extentions import db


class UserModel(db.Model):
    """ Model for users. """

    __tablename__ = 'users'

    game = db.Column(db.String(length=64), primary_key=True, autoincrement=False)
    character_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(length=128))
    join_date = db.Column(db.DateTime)
    login_count = db.Column(db.Integer)

    def __init__(self, game, character_id, character_name):
        self.game = game
        self.character_id = character_id
        self.name = character_name

    def __repr__(self):
        return '<UserModel {}: {}>'.format(self.game, self.character_id)

    # Flask-Login integration
    @staticmethod
    def is_authenticated():
        return True

    # Flask-Login integration
    @staticmethod
    def is_active():
        return True

    # Flask-Login integration
    @staticmethod
    def is_anonymous():
        return False

    # Flask-Login integration
    def get_id(self):
        return self.game, self.character_id
