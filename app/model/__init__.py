import click
from flask.cli import with_appcontext
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()


def init_app(app):
    db.init_app(app)
    ma.init_app(app)
    app.cli.add_command(create_db)
    app.cli.add_command(delete_db)
    if app.config['ENABLE_MIGRATION']:
        migrate = Migrate(app, db)


@click.command('db-create')
@with_appcontext
def create_db():
    db.create_all()
    click.echo('DB created!')


@click.command('db-delete')
@with_appcontext
def delete_db():
    db.drop_all()
    click.echo('DB dropped!')