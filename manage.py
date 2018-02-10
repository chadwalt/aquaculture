import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from __init__ import db, app
from models import Fish, Supplier, Feed



migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    """Creates database with tables"""
    db.create_all()

@manager.command
def drop_db():
    """Deletes database"""
    db.drop_all()


if __name__ == '__main__':
    manager.run()