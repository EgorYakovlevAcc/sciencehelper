from flask import Blueprint
from flask import render_template

controller = Blueprint('controller', __name__)


@controller.route('/')
@controller.route('/index')
def get_index():
    return render_template("index.html")


@controller.route('/workplace')
def get_workplace():
    return render_template("workplace.html")
