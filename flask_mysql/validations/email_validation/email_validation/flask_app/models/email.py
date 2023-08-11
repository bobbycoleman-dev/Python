from flask_app.config.mysql_connection import connect_to_mysql
from flask import flash
import re

DATABASE = "email_validation_db"
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class Email:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO emails (email) VALUES ( %(email)s );"
        results = connect_to_mysql(DATABASE).query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails"
        results = connect_to_mysql(DATABASE).query_db(query)
        emails = []
        for dict in results:
            emails.append(Email(dict))
        return emails

    @classmethod
    def get_one(cls, email_id):
        query = "SELECT * FROM emails WHERE id = %(email_id)s;"
        data = {"email_id": email_id}
        results = connect_to_mysql(DATABASE).query_db(query, data)
        if len(results) == 0:
            return
        return Email(results[0])

    @classmethod
    def delete(cls, email_id):
        query = "DELETE FROM emails WHERE id = %(email_id)s"
        data = {"email_id": email_id}
        connect_to_mysql(DATABASE).query_db(query, data)
        return

    @staticmethod
    def validate_email(email):
        is_valid = True

        if len(email["email"].strip()) == 0:
            flash("Please enter an email address!")
            is_valid = False
        elif not EMAIL_REGEX.match(email["email"]):
            flash("Invalid email address!")
            is_valid = False

        emails_in_db = Email.get_all()
        for one_email in emails_in_db:
            if email["email"] == one_email.email:
                is_valid = False
                flash("Email already exists. Please enter a new email.")

        return is_valid
