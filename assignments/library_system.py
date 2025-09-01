class Library:
    def __init__(self):
        self.books=[]
    
    def add_book(self,title,author):
        book={"title":title,"author":author}
        self.books.append(book)
        print(f"{title} by {author} is added to the library")
    
    def remove_book(self,title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print(f"{title} is removed from the library")
                return
        print(f"{title} is not found in the library")
    
    def search_book(self,title):
        for book in self.books:
            if title.lower() in book["title"].lower():
                print(f"found {book["title"]} by {book["author"]}")
                return
        print(f"book {title} not found")
    
    def display_book(self):
        if not self.books:
            print("library is empty")
        else:
            print("books in the library:")
            for book in self.books:
                print(f"{book['title']},by {book['author']}")


library = Library()

library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")

library.display_book()

library.search_book("1984")
library.search_book("Harry Potter")

library.remove_book("1984")
library.display_book()
