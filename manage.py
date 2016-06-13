

from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand, Migrate

from flaskcommunity.app import create_app
from flaskcommunity.extentions import db

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


manager.add_command('runserver', Server('localhost', port=8080, ssl_context='adhoc'))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
