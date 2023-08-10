from flask_app.config.mysql_connection import connect_to_mysql
from flask_app.models import book

DATABASE = "books_db"


class Author:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.books = []
