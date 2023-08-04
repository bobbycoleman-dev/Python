import random
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "this is my secret key for the great number game"


@app.route("/")
def index():
    if "rand_num" not in session:
        session["rand_num"] = random.randint(1, 100)

    return render_template("index.html")


@app.route("/input", methods=["POST"])
def input():
    if int(request.form["number"]) == session["rand_num"]:
        session["bg_color"] = "bg-success"
        session["result"] = "You Win!"
    elif int(request.form["number"]) > session["rand_num"]:
        session["bg_color"] = "bg-danger"
        session["result"] = "Too High!"
    elif int(request.form["number"]) < session["rand_num"]:
        session["bg_color"] = "bg-danger"
        session["result"] = "Too Low!"

    return redirect("/guess")


@app.route("/guess")
def guess():
    return render_template("guess.html")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
