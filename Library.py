"""
Create a Library class that represents a library. The class should have the following attributes and methods:
Attributes:

books (list): A list of books in the library.
Methods:
add_book(book): Adds a book to the library.
remove_book(book): Removes a book from the library.
get_books(): Returns the list of books in the library.
"""


class Library:
    books = [
        "Rich Dad Poor Dad by Robert T. Kiyosaki",
        "The Millionaire Next Door by The Surprising Secrets of America's Wealthy by Thomas J. Stanley and William D. Danko",
        "Think and Grow Rich by Napoleon Hill",
        "The Total Money Makeover: A Proven Plan for Financial Fitness by Dave Ramsey",
        "I Will Teach You to Be Rich by Ramit Sethi",
        "The Richest Man in Babylon by George S. Clason",
        "Your Money or Your Life: 9 Steps to Transforming Your Relationship with Money and Achieving Financial Independence by Vicki Robin and Joe Dominguez",
        "The Little Book of Common Sense Investing: The Only Way to Guarantee Your Fair Share of Stock Market Returns by John C. Bogle",
        "The Wealthy Barber: The Common Sense Guide to Successful Financial Planning by David Chilton",
        "Money: Master the Game: 7 Simple Steps to Financial Freedom by Tony Robbins",
    ]

    def __init__(self) -> None:
        pass

    def add_book(self):
        book_toAdd = input("Enter book title to add in list: ")
        self.books.append(book_toAdd)
        return f"Added {book_toAdd}"

    def remove_book(self):
        book_toRemove = input("Enter book name to remove from list:\n")
        for i, book in enumerate(self.books):
            if book_toRemove.lower == book.lower:
                self.books.pop(i)
                print("You have removed {self.books[i]} from list")

    def get_books(self):
        for x, y in enumerate(self.books, 1):
            print(f"{x} {y}")


aiu = Library()
aiu.get_books()
