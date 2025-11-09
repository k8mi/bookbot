from stats import get_word_count
from stats import get_character_count
from stats import sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def sort_on(dictionary):
    return dictionary["num"]
def main():
    # testing get_book_text function
    # frankenstein_text = get_book_text("books/frankenstein.txt")
    # print(frankenstein_text)
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_text = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + frankenstein_path + "...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(frankenstein_text)} total words")
    frankenstein_chars = get_character_count(frankenstein_text)
    sorted_frankenstein_chars = sort_dictionary(frankenstein_chars)
    print("--------- Character Count -------")

    for i in range(0,len(sorted_frankenstein_chars)-1):
        if sorted_frankenstein_chars[i]["char"].isalpha():
            print(sorted_frankenstein_chars[i]["char"] + ": " + str(sorted_frankenstein_chars[i]["num"]))
    print("============= END ===============")






main()