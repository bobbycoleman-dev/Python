from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


@app.route("/dojo")
def dojo():
    return "Dojo!"


@app.route("/say/<string:name>")
def say(name):
    return f"Hi {name.capitalize()}"


@app.route("/repeat/<int:num>/<string:input>")
def repeat(num, input):
    return f"{input * num}"


@app.route("/<route>")
def wrong_route(route):
    if route != "dojo" or route != "say" or route != "repeat":
        return "Sorry! No response. Try again."


if __name__ == "__main__":
    app.run(debug=True)
