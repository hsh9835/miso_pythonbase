from flask import Blueprint

from config.plugins.blueprint_autoset import bpName

bp = Blueprint(bpName(__file__), __name__)
