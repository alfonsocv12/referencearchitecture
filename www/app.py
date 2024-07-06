import flask

from www.webapp.index import webapp


def create_app():
    flask_app = flask.Flask(__name__, template_folder='webapp/static', static_folder='webapp/static')

    flask_app.register_blueprint(webapp)

    return flask_app


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run()
