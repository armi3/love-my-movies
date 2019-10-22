"""Routes for logged-in application."""
from flask import Blueprint, render_template, session
from flask import current_app as app
from application import requester
from application import db


# Blueprint Configuration
# main_bp = Blueprint('main_bp', __name__,
#                     template_folder='templates',
#                     static_folder='static')
db = db.create_db()


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/list1")
def list1():
    info = requester.get_list.__func__(app, 'https://api.themoviedb.org/3/list/124389?api_key=')
    return render_template("list.html", info=info)
