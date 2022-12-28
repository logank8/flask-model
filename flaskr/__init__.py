from abc import abstractclassmethod
import os

from flask import Flask


### THINGS THAT STILL NEED TO BE DONE:
## Connect spotify data to app
## Connect model to app
## Make adapative list of previous predictions

## application factory function
def create_app(test_config=None):
    # create and configure app
    ## creates Flask instance
    ## instance_relative_config=True means configuration files are relative to the instance folder

    app = Flask(__name__, instance_relative_config=True)
    ## sets default configuration for SQLite database file (saved under app.instance_path)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load instance config
        ## overrides default config with values from config.py if exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load test config if passed in
        app.config.from_mapping(test_config)
    
    # ensure instance folder exists
    try:
        ## ensures that app.instance_path exists
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    ## creates simple route so you can see some things working
    @app.route("/hello")
    def hello():
        return "Hello World!"

    ## registers db commands with application instance
    from . import db
    db.init_app(app)

    ## registers about blueprint with application instance
    from . import abt
    app.register_blueprint(abt.bp)

    from . import page
    app.register_blueprint(page.bp)
    app.add_url_rule('/', endpoint='index')

    return app
