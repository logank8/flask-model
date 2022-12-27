import sqlite3

import click

## current_app points to Flask application handling the request
## g is a special object unique for each request
from flask import current_app, g

def get_db():
    if 'db' not in g:
        ## establishes connection to file pointed at by DATABASE config key
        
        g.db = sqlite3.connect(

            
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        ## tells connection to return rows that behave like dicts so columns can be accessed by name
        g.db.row_factory = sqlite3.Row

    return g.db

## checks if a connection was created by checking if g.db was set -  if so, closes it
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    ## runs sqlite3 script
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


## defines command line command called init-db and shows success message
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db) ## cleanup function
    app.cli.add_command(init_db_command) 

