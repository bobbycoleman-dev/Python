from flask_app.config.mysql_connection import connect_to_mysql
from flask_app.models import author
from flask_app.models import book

DATABASE = "books_db"


class Favorite:
    def __init__(self, data) -> None:
        self.author_id = data["author_id"]
        self.book_id = data["book_id"]

    @classmethod
    def add_favorite(cls, author_id, book_id):
        query = """
                INSERT INTO favorites (author_id, book_id)
                VALUES ( %(author_id)s, %(book_id)s );
                """
        data = {"author_id": author_id, "book_id": book_id}
        results = connect_to_mysql(DATABASE).query_db(query, data)
        return results
