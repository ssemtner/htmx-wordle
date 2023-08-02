import flask

import wordle.views as views

def create_app(config):
    app = flask.Flask(__name__)

    app.config['WORD'] = 'hello'
    
    app.register_blueprint(views.main_blueprint)
    app.register_blueprint(views.auth_blueprint)

    return app
