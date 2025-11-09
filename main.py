from stats import get_word_count
from stats import get_character_count
from stats import sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def sort_on(dictionary):
    return dictionary["num"]
def main():

    if(len(sys.argv)<2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_path + "...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    book_chars = get_character_count(book_text)
    sorted_book_chars = sort_dictionary(book_chars)
    print("--------- Character Count -------")

    for i in range(0,len(sorted_book_chars)-1):
        if sorted_book_chars[i]["char"].isalpha():
            print(sorted_book_chars[i]["char"] + ": " + str(sorted_book_chars[i]["num"]))
    print("============= END ===============")






main()