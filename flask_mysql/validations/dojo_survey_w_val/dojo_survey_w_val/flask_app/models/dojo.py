from flask_app.config.mysql_connection import connect_to_mysql
from flask import flash

DATABASE = "dojo_survey_schema"


class Dojo:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.love_code = data["love_code"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO dojos (name, location, language, comment, love_code)
                VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s, %(love_code)s );
                """
        results = connect_to_mysql(DATABASE).query_db(query, data)
        return results

    @classmethod
    def get_one(cls, dojo_id):
        query = "SELECT * FROM dojos WHERE id = %(dojo_id)s"
        data = {"dojo_id": dojo_id}
        results = connect_to_mysql(DATABASE).query_db(query, data)
        dojo = Dojo(results[0])
        return dojo

    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey["name"]) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if survey["location"] == "none":
            flash("Please select a Dojo Location.")
            is_valid = False
        if survey["language"] == "none":
            flash("Please select a Language.")
            is_valid = False
        if len(survey["comment"]) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        if len(survey["love_code"]) < 3:
            flash("Please select how much you love to code.")
            is_valid = False
        return is_valid
