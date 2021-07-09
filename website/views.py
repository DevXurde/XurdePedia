from flask import Blueprint, render_template
from . import open_settings

views = Blueprint(name="views", import_name=__name__)
settings = open_settings()

@views.route("/")
def home():
    return render_template("index.html", settings=settings)