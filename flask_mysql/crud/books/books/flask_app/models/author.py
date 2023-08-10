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

    # Create
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO authors (name)
                VALUES ( %(author_name)s );
                """
        results = connect_to_mysql(DATABASE).query_db(query, data)
        return results

    # Get One
    @classmethod
    def get_one(cls, author_id):
        query = """
                SELECT * FROM authors
                LEFT JOIN favorites ON favorites.author_id = authors.id
                LEFT JOIN books ON favorites.book_id = books.id
                WHERE authors.id = %(author_id)s;
                """
        data = {"author_id": author_id}
        results = connect_to_mysql(DATABASE).query_db(query, data)
        author = Author(results[0])

        for row in results:
            book_data = {
                "id": row["books.id"],
                "title": row["title"],
                "num_of_pages": row["num_of_pages"],
                "created_at": row["books.created_at"],
                "updated_at": row["books.updated_at"],
            }
            author.books.append(book.Book(book_data))

        return author

    # Get All
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connect_to_mysql(DATABASE).query_db(query)
        authors = []
        for dict in results:
            authors.append(Author(dict))
        return authors
