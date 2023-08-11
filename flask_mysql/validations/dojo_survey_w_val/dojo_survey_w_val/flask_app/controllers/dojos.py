from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo import Dojo


@app.route("/")
def index():
    return render_template("index.html")


@app.post("/process")
def process():
    print(request.form)
    if not Dojo.validate_survey(request.form):
        return redirect("/")

    love_code = ""

    if request.form["love_code"] == "hate":
        love_code = "hate's to code but is doing it anyways"
    elif request.form["love_code"] == "soso":
        love_code = "is confused but will push on"
    elif request.form["love_code"] == "love":
        love_code = "loves coding so much it hurts"

    data = {
        "name": request.form["name"],
        "location": request.form["location"].capitalize(),
        "language": request.form["language"].capitalize(),
        "comment": request.form["comment"],
        "love_code": love_code,
    }

    dojo_id = Dojo.create(data)
    return redirect(f"/result/{dojo_id}")


@app.route("/result/<int:dojo_id>")
def result(dojo_id):
    dojo = Dojo.get_one(dojo_id)
    return render_template("result.html", dojo=dojo)
