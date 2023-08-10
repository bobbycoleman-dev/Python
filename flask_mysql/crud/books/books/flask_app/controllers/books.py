from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.book import Book
from flask_app.models import author
from flask_app.models import favorite


@app.route("/books")
def books():
    books = Book.get_all()
    return render_template("books.html", books=books)


@app.post("/books/create")
def create_book():
    Book.create(request.form)
    return redirect("/books")


@app.route("/book/<int:book_id>/details")
def book_details(book_id):
    book = Book.get_one(book_id)
    authors = author.Author.get_all()
    return render_template("book_detail.html", book=book, authors=authors)


@app.post("/add_favorited/<int:book_id>")
def add_favorited(book_id):
    author_id = request.form["author_id"]
    favorite.Favorite.add_favorite(author_id, book_id)
    return redirect(f"/book/{book_id}/details")
