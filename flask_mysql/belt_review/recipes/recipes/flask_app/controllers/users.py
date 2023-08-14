from flask_app import app
from flask import flash, render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


bcrypt = Bcrypt(app)


@app.route("/")
def index():
    """Render the index route"""

    return render_template("index.html")


@app.post("/register/user")
def register():
    """Register the user with an account"""

    if not User.validate_registration(request.form):
        return redirect("/")

    pw_hash = bcrypt.generate_password_hash(request.form["password"])

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash,
    }

    user_id = User.create(data)
    session["user_id"] = user_id
    flash("Thank you for registering!")
    return redirect("/recipes")


@app.post("/login")
def login():
    """Login into an existing account"""

    if not User.validate_login(request.form):
        return redirect("/")

    user = User.get_by_email(request.form["email"])

    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        # if we get False after checking the password
        flash("Invalid Email/Password", "login")
        return redirect("/")
    # if the passwords matched, we set the user_id into session
    session["user_id"] = user.id
    flash("You are now signed in!")
    return redirect("/recipes")


@app.route("/recipes")
def dashboard():
    """Display the user's dashboard"""

    if "user_id" not in session:
        return redirect("/")
    user = User.get_one(session["user_id"])
    recipes = Recipe.get_all()
    return render_template("recipes.html", user=user, recipes=recipes)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
