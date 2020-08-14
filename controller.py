from flask import Blueprint
from flask import render_template

controller = Blueprint('controller', __name__)


@main_router.route('/')
@main_router.route('/index')
def get_index():
    return render_template("index.html")


@main_router.route('/workplace')
def get_workplace():
    return render_template("workplace.html")
