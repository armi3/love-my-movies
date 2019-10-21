"""Routes for logged-in application."""
from flask import Blueprint, render_template, session
from flask import current_app as app


# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@main_bp.route('/')
def home():
    return render_template("home.html")


@main_bp.route("/list1")
def list1():
    return render_template("list.html")
