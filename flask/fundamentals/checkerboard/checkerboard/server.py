from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    x = 8
    y = 8
    color1 = "red"
    color2 = "black"
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2)


@app.route("/4")
def four():
    x = 4
    y = 4
    color1 = "red"
    color2 = "black"
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2)


@app.route("/<int:x>")
def only_x(x):
    y = 8
    color1 = "red"
    color2 = "black"
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2)


@app.route("/<int:x>/<int:y>")
def x_y(x, y):
    color1 = "red"
    color2 = "black"
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2)


@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def colors(x, y, color1, color2):
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2)


if __name__ == "__main__":
    app.run(debug=True)
