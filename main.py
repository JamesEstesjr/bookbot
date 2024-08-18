#the main function that starts the chain of function calls later on
def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = word_count(text)
    letter_dict = letters(text)
    sorted_let = letter_counts(letter_dict)
    print(f"Report on {book_path}")
    print()
    print("The letter counts are:")
    for i in sorted_let:
        print(i)
        #print(book.read())

#should take the total of text and convert it into letters then make a dict that tells what amount of letters there are
def letters(text):
    letter_dicts = {}
    lower_case = text.lower()
    lower_letter = list(lower_case)
    for letter in lower_letter:
        if letter in letter_dicts:
            letter_dicts[letter] += 1
        else:
            letter_dicts[letter] = 0
            letter_dicts[letter] += 1

    return letter_dicts


#takes the book and returns the number of words in the book
def word_count(text):
    words = text.split()
    return len(words)

#opens book for duration of chain
def book_text(book_path):
    with open(book_path) as books:
        book = books.read()
        return book

def letter_counts(letter_dict):
    # Convert dictionary to a list of tuples (letter, count)
    unordered_letters = [(letter, count) for letter, count in letter_dict.items() if letter.isalpha()]
    
    # Sort the list by count in descending order
    sorted_letters = sorted(unordered_letters, key=lambda x: x[1], reverse=True)
    
    return sorted_letters
#should be the only thing to activate. calls on the main function at the top
main()