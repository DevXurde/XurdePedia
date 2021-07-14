from flask import Blueprint
from . import open_settings

auth = Blueprint(name="auth", import_name=__name__)
settings = open_settings()
