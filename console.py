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
