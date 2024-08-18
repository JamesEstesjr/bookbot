def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as book:
        print(book.read())
main()