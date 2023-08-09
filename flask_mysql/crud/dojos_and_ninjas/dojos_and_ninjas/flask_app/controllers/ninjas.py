from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route("/ninja/new")
def new_ninja():
    """Render form page to create new ninja; calls get all on dojos to get the name and id"""
    dojos = Dojo.get_all()
    return render_template("ninja.html", dojos=dojos)


@app.post("/ninja/create")
def create_ninja():
    """Process the form data to create a new ninja; redirects to dojo the ninja was added to"""
    Ninja.create(request.form)
    return redirect(f"/dojo/{request.form['dojo_id']}")
