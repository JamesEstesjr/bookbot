#the main function that starts the chain of function calls later on
def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = word_count(text)  
    print (f"word_count {num_words}")  
        #print(book.read())


#takes the book and returns the number of words in the book
def word_count(text):
    words = text.split()
    return len(words)

#opens book for duration of chain
def book_text(book_path):
    with open(book_path) as books:
        book = books.read()
        return book
#should be the only thing to activate. calls on the main function at the top
main()