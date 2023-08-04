from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "bobby's secret key"


@app.route("/")
def index():
    if "count" not in session:
        session["count"] = 0
    session["count"] += 1
    return render_template("index.html")


@app.route("/count")
def count():
    # session["count"] += 1
    return redirect("/")


@app.route("/two")
def two():
    session["count"] += 1
    return redirect("/")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


@app.route("/add", methods=["POST"])
def add():
    number = int(request.form["add"]) - 1
    session["count"] += number

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
