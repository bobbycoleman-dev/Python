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

    # Create
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO books (title, num_of_pages)
                VALUES ( %(book_title)s, %(num_of_pages)s );
                """
        results = connect_to_mysql(DATABASE).query_db(query, data)
        return results

    # Get One
    @classmethod
    def get_one(cls, book_id):
        query = """
                SELECT * FROM books
                LEFT JOIN favorites ON favorites.book_id = books.id
                LEFT JOIN authors ON favorites.author_id = authors.id
                WHERE books.id = %(book_id)s;
                """
        data = {"book_id": book_id}
        results = connect_to_mysql(DATABASE).query_db(query, data)
        book = Book(results[0])

        for row in results:
            author_data = {
                "id": row["authors.id"],
                "name": row["name"],
                "created_at": row["authors.created_at"],
                "updated_at": row["authors.updated_at"],
            }
            book.authors.append(author.Author(author_data))

        return book

    # Get All
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connect_to_mysql(DATABASE).query_db(query)
        books = []
        for dict in results:
            books.append(Book(dict))
        return books
