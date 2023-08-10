from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author
from flask_app.models import book
from flask_app.models import favorite


@app.route("/")
def home():
    return redirect("/authors")


@app.route("/authors")
def authors():
    authors = Author.get_all()
    return render_template("authors.html", authors=authors)


@app.post("/authors/create")
def create_author():
    Author.create(request.form)
    return redirect("/authors")


@app.route("/author/<int:author_id>/favorites")
def author_favorites(author_id):
    author = Author.get_one(author_id)
    books = book.Book.get_all()
    return render_template("favorites.html", author=author, books=books)


@app.post("/add_favorite/<int:author_id>")
def add_favorite(author_id):
    book_id = request.form["book_id"]
    favorite.Favorite.add_favorite(author_id, book_id)
    return redirect(f"/author/{author_id}/favorites")
