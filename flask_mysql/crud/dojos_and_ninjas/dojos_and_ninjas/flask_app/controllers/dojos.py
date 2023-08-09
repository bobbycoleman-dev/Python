from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo


@app.route("/")
def reroute():
    """Redirect from root to /dojos"""
    return redirect("/dojos")


@app.route("/dojos")
def index():
    """Call the get_all method to get all dojos"""
    dojos = Dojo.get_all()
    return render_template("index.html", dojos=dojos)


@app.post("/dojo/create")
def create_dojo():
    """Receive and process form to create new dojo location"""
    Dojo.create(request.form)
    return redirect("/")


@app.get("/dojo/<int:dojos_id>")
def display_dojo(dojos_id):
    """Call to get one dojo by id and display it along with its associated ninjas"""
    dojo = Dojo.get_one(dojos_id)
    return render_template("dojo.html", dojo=dojo)
