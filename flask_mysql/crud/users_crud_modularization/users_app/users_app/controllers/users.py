from users_app import app
from flask import render_template, redirect, request, session, flash
from users_app.models.user import User


@app.route("/")
def index():
    """call the get_all classmethod to get all friends"""
    users = User.get_all()
    return render_template("index.html", users=users)


# Show the Create User template
@app.route("/create")
def create():
    """Redirect to the Create User template"""
    return render_template("create.html")


# POST method for creating a user, redirect to root
@app.route("/create_user", methods=["POST"])
def create_user():
    """Create a new User"""
    User.save(request.form)
    return redirect("/")


# Show the Show User template
@app.route("/show/<int:user_id>")
def show(user_id):
    """Redirect to the Show User template"""
    user = User.get_one(user_id)
    return render_template("show.html", user=user)


# Show the Update User form template
@app.route("/update/<int:user_id>")
def update(user_id):
    """Redirect to the Update User template"""
    user = User.get_one(user_id)
    return render_template("update.html", user=user)


# POST method for updating user information, redirect to Show User
@app.route("/update_user", methods=["POST"])
def update_user():
    """Update User information and return back to the Show User template"""

    User.update(request.form)
    return redirect(f"show/{request.form['id']}")


# Delete a User method, redirect back to root
@app.route("/delete_user/<int:id>")
def delete_user(id):
    """Delete a User from the db"""
    User.delete(id)
    return redirect("/")
