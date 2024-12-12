'''
__str__(self): Defines the behavior of print().
__add__(self, other): Defines the behavior for + operator.
'''

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        
    def __str__(self):
        return f"'{self.title}' book with {self.pages} pages."
    
    def __add__(self, other):
        return self.pages + other.pages
    
book1 = Book("Python Basics", 300)
book2 = Book("Advanced Python", 400)

print(book1) # 'Python' book with 300 pages.

# Adding pages from both the books
total_pages = book1 + book2
print("Total pages:", total_pages) # 700