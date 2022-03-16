
from flask import Flask, render_template, redirect, request
from flask import Blueprint
from repositories import author_repository
from repositories import book_repository
from models.book import Book
from models.author import Author

books_blueprint = Blueprint("books" , __name__)

@books_blueprint.route ("/books")
def books():
    books = book_repository.select_all()
    authors = author_repository.select_all()
    return render_template("books/index.html" , all_books = books, all_authors = authors)

@books_blueprint.route("/books/<id>/delete" , methods = ['POST']) # Function to delete a book when a user presses delete button
def delete_book(id):
    book_repository.delete(id)
    return redirect ('/books') # Redirect user to the books index page
    
@books_blueprint.route("/books/<id>/" , methods=['GET']) # Function to display a specific book's details
def show_book(id):
    book = book_repository.select(id)
    return render_template('/books/show.html' , book = book)

@books_blueprint.route("/books/new_author" , methods = ['GET']) # Form to add a new author
def new_author():
    return render_template("books/new_author.html")

@books_blueprint.route ("/authors" , methods = ['POST']) # Add author submission to authors
def create_author():
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    author = Author(first_name , last_name) # Create author object
    author_repository.save(author)

    return redirect ('books') # Redirect to books index page

@books_blueprint.route("/books/new_book" , methods = ['GET']) # Form to add a new book 
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new_book.html", all_authors= authors)

@books_blueprint.route ("/books", methods = ["POST"]) # Add book submission to books
def create_book():
    title = request.form['title']
    author_id = request.form['author_id']
    blurb = request.form['blurb']
    price = request.form['price']

    author = author_repository.select(author_id) # Find author using their author id

    book = Book (title, author, blurb, price)
    book_repository.save(book)

    return redirect ('books') # Redirect to books index page

@books_blueprint.route("/books/<id>/edit_book" , methods = ['GET']) # Function to display & populate the edit book form
def edit_book(id):
    book = book_repository.select(id) # Find book to edit

    authors = author_repository.select_all() # Allow all authors to be selected from form

    return render_template('/books/edit_book.html' , book = book , all_authors = authors)

@books_blueprint.route('/books/<id>' , methods = ['POST']) # Function to update book from edit book page
def update_book(id):
    title = request.form['title']
    author_id = request.form['author_id']
    blurb = request.form['blurb']
    price = request.form['price']

    author = author_repository.select(author_id) # Find author using their author id

    book = Book (title, author, blurb, price, id)
    book_repository.update(book)

    return redirect ('/books') # Redirect to books index page