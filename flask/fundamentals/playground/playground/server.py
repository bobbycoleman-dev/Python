from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Route to /play to begin!</h1>"


@app.route("/play")
def play(x=3):
    return render_template("index.html", x=x)


@app.route("/play/<int:x>")
def play_x(x):
    return render_template("index.html", x=x)


@app.route("/play/<int:x>/<string:color>")
def play_color(x, color):
    return render_template("index.html", x=x, color=color)


if __name__ == "__main__":
    app.run(debug=True)
