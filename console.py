import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_repository.delete_all()
book_repository.delete_all()

author_1 = Author("Alix" , "Harrow")
author_repository.save(author_1)
author_2 = Author("Brianna" , "Wiest")
author_repository.save(author_2)

# author_repository.delete(author_2.id)

select_all_authors = author_repository.select_all()
for author in select_all_authors:
    print (author.__dict__)

select_one_author = author_repository.select(author_1.id)
print(select_one_author.__dict__)

book_1 = Book("101 Essays" , author_2 , "A delightful read" , 8.99)
book_repository.save (book_1)
book_2 = Book("10 Thousand Doors" , author_1 , "Shortlisted for the Hugo award" , 14.99)
book_repository.save (book_2)

select_all_books = book_repository.select_all()
for book in select_all_books:
    print(book.__dict__)

select_one_book = book_repository.select(book_1.id)
print(select_one_book.__dict__)





