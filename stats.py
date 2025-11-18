# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_list(text):
    set_of_letters = set()
    count_of_letters = []

    text = text.lower()
    for letter in text:
        set_of_letters.add(letter)
    
    for letter in set_of_letters:
        count_of_letters.append({"char" : letter, "num" : text.count(letter)})

    count_of_letters.sort(reverse = True, key = sort_on)
    return count_of_letters
