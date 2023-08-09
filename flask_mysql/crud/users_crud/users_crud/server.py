from flask import Flask, render_template, request, redirect

# import the class from friend.py
from user import User

app = Flask(__name__)


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    return render_template("index.html", users=users)


@app.route("/create")
def create():
    return render_template("create.html")


@app.route("/create_user", methods=["POST"])
def create_user():
    User.save(request.form)
    return redirect("/")


@app.route("/show/<int:user_id>")
def show(user_id):
    user = User.get_one(user_id)
    return render_template("show.html", user=user)


@app.route("/update/<int:user_id>")
def update(user_id):
    user = User.get_one(user_id)
    return render_template("update.html", user=user)


@app.route("/update_user", methods=["POST"])
def update_user():
    id = request.form["id"]
    show = "show/" + id
    User.update(request.form)
    return redirect(show)


@app.route("/delete_user/<int:id>")
def delete_user(id):
    User.delete(id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
