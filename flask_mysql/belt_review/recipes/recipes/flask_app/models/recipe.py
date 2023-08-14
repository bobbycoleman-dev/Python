from flask_app.config.mysql_connection import connect_to_mysql
from flask_app.models import user
from flask import flash

DATABASE = "recipes_db"


class Recipe:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.under_thirty = data["under_thirty"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = user.User.get_one(self.user_id)

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO recipes (name, description, instructions, date_made, under_thirty, user_id)
                VALUES ( %(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_thirty)s, %(user_id)s );
                """
        results = connect_to_mysql(DATABASE).query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM recipes
                JOIN users ON recipes.user_id = users.id 
                """
        results = connect_to_mysql(DATABASE).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(Recipe(recipe))
        return recipes

    @classmethod
    def get_one(cls, recipe_id):
        query = """
                SELECT * FROM recipes 
                JOIN users ON recipes.user_id = users.id 
                WHERE recipes.id = %(recipe_id)s;
                """
        data = {"recipe_id": recipe_id}
        results = connect_to_mysql(DATABASE).query_db(query, data)
        if len(results) == 0:
            return
        return Recipe(results[0])

    @classmethod
    def update(cls, data):
        query = """
                UPDATE recipes
                SET name = %(name)s, description = %(description)s, 
                instructions = %(instructions)s, date_made = %(date_made)s, under_thirty = %(under_thirty)s
                WHERE recipes.id = %(recipe_id)s;
                """
        connect_to_mysql(DATABASE).query_db(query, data)
        return

    @classmethod
    def delete(cls, recipe_id):
        query = "DELETE FROM recipes WHERE id = %(recipe_id)s;"
        data = {"recipe_id": recipe_id}
        connect_to_mysql(DATABASE).query_db(query, data)
        return

    @staticmethod
    def validate_form(form_data):
        is_valid = True

        # RECIPE NAME
        if len(form_data["name"].strip()) == 0:
            flash("Please enter a recipe name.", "recipe")
            is_valid = False
        elif len(form_data["name"].strip()) < 3:
            flash("Recipe name must be at least three characters.", "recipe")
            is_valid = False

        # RECIPE DESCRIPTION
        if len(form_data["description"].strip()) == 0:
            flash("Please enter a recipe description.", "recipe")
            is_valid = False
        elif len(form_data["description"].strip()) < 3:
            flash("Recipe description must be at least three characters.", "recipe")
            is_valid = False

        # RECIPE INSTRUCTIONS
        if len(form_data["instructions"].strip()) == 0:
            flash("Please enter a recipe instructions.", "recipe")
            is_valid = False
        elif len(form_data["instructions"].strip()) < 3:
            flash("Recipe instructions must be at least three characters.", "recipe")
            is_valid = False

        # RECIPE DATE MADE
        if len(form_data["date_made"].strip()) == 0:
            flash("Please enter a date.", "recipe")
            is_valid = False

        # RECIPE UNDER THIRTY
        if form_data["under_thirty"] == "2":
            flash(
                "Please select if recipe can be cooked in under 30 minutes.", "recipe"
            )
            is_valid = False

        return is_valid
