class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"{self.title}"

# performs insertion sort to sort an array of books


def insertion_sort(arr_of_books):
    # iterate through array
    # skip the first element
    # iterate ove rthe bookes or indices?
    # Need to have access to the book before the current book
    # need access to each index in order to facilitate this
    for i in range(1, len(arr_of_books)):
        curr_book = arr_of_books[i]
        # prev_book = arr_of_books[book_index - 1]
        # book_index will start at i, be updated as we swap
        book_index = i

        # compare curr_book with the previous book
        while book_index > 0 and curr_book.title < arr_of_books[book_index - 1].title:
            # swap them
            arr_of_books[book_index], arr_of_books[book_index -
                                                   1] = arr_of_books[book_index - 1], arr_of_books[book_index]
            # need to keep track of current book's changing index
            book_index -= 1

    return arr_of_books


arr_of_books = [
    Book("Harry Potter", "JK Rowling", "Children's Fantasy"),
    Book("Game of Thrones", "George RR Martin", "Adult Fantasy"),
    Book("John Adams", "David MucCullough", "Non-Fiction"),
    Book("Food", "Michael Pollen", "Cooking")
]

insertion_sort(arr_of_books)

# print(arr_of_books)
for book in arr_of_books:
    print(book)
