class Book:
    def __init__(self, name, author, count):
        self.name = name
        self.author = author
        self.count = count

    def __str__(self):
        return f"{self.name} - {self.author} ({self.count})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name, author):
        for book in self.books:
            if book.name == name and book.author == author:
                book.count += 1
                return
        self.books.append(Book(name, author, 1))

    def show_books(self):
        for book in self.books:
            print(book)

lib = Library()

n = int(input("Скільки книг додати: "))

for i in range(n):
    name = input("Назва: ")
    author = input("Автор: ")
    lib.add_book(name, author)

lib.show_books()