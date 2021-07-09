from flask import Flask
import json

def open_settings():
    with open("settings.json", "r") as file:
        args = json.load(file)
    return args

settings = open_settings()

host = settings["host"]
port = settings["port"]

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = settings["secret_key"]
    app.config["SERVER_NAME"] = f"{host}:{port}"

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app