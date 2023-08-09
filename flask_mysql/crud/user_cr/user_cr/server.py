from flask import Flask, render_template, request, redirect

# import the class from friend.py
from user import User

app = Flask(__name__)


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    return render_template("index.html", users=users)


@app.route("/get_user/<int:user_id>")
def get_user(user_id):
    user = User.get_one(user_id)
    return render_template("user.html", user=user)


@app.route("/create")
def create():
    return render_template("create.html")


@app.route("/create_user", methods=["POST"])
def create_user():
    User.save(request.form)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
