
from flask import Flask, render_template, redirect, request
from flask import Blueprint
from repositories import author_repository
from repositories import book_repository
from models.book import Book

books_blueprint = Blueprint("books" , __name__)

@books_blueprint.route ("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html" , all_books = books)

