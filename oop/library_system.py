#Composition - Library:

#Attributes: books (a list to store instances of Book, EBook, and PrintBook).
#Methods:
#add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
#list_books(self): Prints details of each book in the library.
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
class EBook(Book):
    def __init__(self, title, author,file_size):
        super().__init__(title, author)  
        self.file_size =file_size      
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count= page_count    
books=Book()
    
        
