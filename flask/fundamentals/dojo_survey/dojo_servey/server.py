from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "super secret key for my web app"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    session["dojoname"] = request.form["dojoname"].capitalize()
    session["location"] = request.form["location"].capitalize()
    session["language"] = request.form["language"].capitalize()
    session["comments"] = request.form["comments"].capitalize()

    if request.form["btnradio"] == "hate":
        session["btnradio"] = "hate's to code but is doing it anyways"
    elif request.form["btnradio"] == "soso":
        session["btnradio"] = "is confused but will push on"
    elif request.form["btnradio"] == "love":
        session["btnradio"] = "loves coding so much it hurts"

    return redirect("/result")


@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
