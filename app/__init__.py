from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import multiply_route
    app.register_blueprint(multiply_route)

    return app