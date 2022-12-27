import os

from flask import Flask

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

    ## registers authentication blueprint with application instance
    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
