from flask_app.config.mysql_connection import connect_to_mysql
from flask_app.models import author

DATABASE = "books_db"


class Book:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.authors = []

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO books (title, num_of_pages)
                VALUES ( %(title)s, %(num_of_pages)s );
                """
        results = connect_to_mysql(DATABASE).query_db(query, data)
        return results
