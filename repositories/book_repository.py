from db.run_sql import run_sql

from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, author_id, blurb, price) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title , book.author.id, book.blurb, book.price]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []

    sql="SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'] , author, row['blurb'] , row['price'] , row['id'])

        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]

    result = run_sql(sql,values)[0]

    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['title'] , author, result['blurb'] , result['price'] , result['id'])
    return book

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    value = [id]
    run_sql(sql,value)

def update(book):
    sql = "UPDATE books SET (title,author_id, blurb, price) = (%s, %s, %s, %s) WHERE id = %s"
    values = [book.title , book.author.id , book.blurb , book.price , book.id]

    run_sql(sql, values)