from stats import get_word_count
from stats import get_character_count
from stats import sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    # testing get_book_text function
    # frankenstein_text = get_book_text("books/frankenstein.txt")
    # print(frankenstein_text)
    frankenstein_text = get_book_text("books/frankenstein.txt")
    print(f"Found {get_word_count(frankenstein_text)} total words")
    frankenstein_chars = get_character_count(frankenstein_text)
    print(frankenstein_chars)

    sorted_frankenstein_chars = sort_dictionary(frankenstein_chars)
    print(sorted_frankenstein_chars)



main()