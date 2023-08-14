import datetime
from flask_app import app
from flask import flash, render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask_app.models import user
from flask_app.models.recipe import Recipe


@app.template_filter("format_date")
def format_date(date):
    """Format dates to MMMM DD YYYY"""
    return date.strftime("%B %-d, %Y")


@app.route("/recipe/new")
def new_recipe():
    """Render the create template"""
    if "user_id" not in session:
        return redirect("/")
    current_user = user.User.get_one(session["user_id"])
    return render_template("create.html", current_user=current_user)


@app.post("/create_recipe")
def create_recipe():
    """Process form data to create new recipe"""
    print(request.form)
    if not Recipe.validate_form(request.form):
        return redirect("/recipe/new")

    Recipe.create(request.form)
    return redirect("/recipes")


@app.route("/recipes/<int:recipe_id>")
def view_recipe(recipe_id):
    """Render details template"""
    if "user_id" not in session:
        return redirect("/")
    current_user = user.User.get_one(session["user_id"])
    recipe = Recipe.get_one(recipe_id)
    return render_template("details.html", recipe=recipe, current_user=current_user)


@app.route("/recipes/<int:recipe_id>/edit")
def edit_recipe(recipe_id):
    """Render edit template"""
    if "user_id" not in session:
        return redirect("/")
    recipe = Recipe.get_one(recipe_id)
    return render_template("edit.html", recipe=recipe)


@app.post("/edit_recipe")
def edit():
    """Process form for updating recipe"""
    if not Recipe.validate_form(request.form):
        recipe_id = request.form["recipe_id"]
        return redirect(f"/recipes/{recipe_id}/edit")
    Recipe.update(request.form)
    return redirect("/recipes")


@app.route("/delete/<int:recipe_id>")
def delete(recipe_id):
    """Delete a recipe"""
    if "user_id" not in session:
        return redirect("/")
    Recipe.delete(recipe_id)
    return redirect("/recipes")
