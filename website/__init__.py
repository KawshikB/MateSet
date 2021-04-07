from flask import Flask
from flask import Blueprint

def create_app():
    """To crate a Flask app

    Returns:
        app: a flask app
    """    
    # creating Flask app
    app = Flask(__name__)
    # confiuring app secret key
    app.config['SECRET_KEY'] = "Lucifer Morningstar"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # returning app
    return app