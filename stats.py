def get_word_count(bookstring):
    wordlist = bookstring.split()
    return len(wordlist)

def get_character_count(bookstring):
    lowercase = bookstring.lower()
    character_dictionary = {}
    for character in lowercase:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    return character_dictionary

def sort_on(dictionary):
    return dictionary["num"]


def sort_dictionary(unsorted_dictionary):
    dictionary_list = [] 
    for key in unsorted_dictionary:
        dictionary_list.append({"char": key, "num": unsorted_dictionary[key]})
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list
