import flask

from www.webapp import webapp
from www.api.infraestructure.http_controllers import api


def create_app():
    flask_app = flask.Flask(
        __name__,
        template_folder='webapp/static',
        static_folder='webapp/static')

    flask_app.register_blueprint(webapp)
    flask_app.register_blueprint(api, url_prefix='/api/')

    return flask_app


flask_app = create_app()

if __name__ == '__main__':
    flask_app.run()
