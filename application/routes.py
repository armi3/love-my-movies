"""Routes for logged-in application."""
from flask import Blueprint, render_template, session
from flask import current_app as app
from application import requester
from application import db


db = db.create_db()


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/list1")
def list1():
    info = requester.get_info.__func__(app, db, '124389')
    return render_template("list.html", info=info)


@app.route("/list2")
def list2():
    info = requester.get_info.__func__(app, db, '124464')
    return render_template("list.html", info=info)


@app.route("/list3")
def list3():
    info = requester.get_info.__func__(app, db, '124465')
    return render_template("list.html", info=info)